from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from grammar.RubyLexer import RubyLexer
from grammar.RubyParser import RubyParser
from grammar.RubyVisitor import RubyVisitor
import PySimpleGUI as sg


class GUIErrorListener(ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"ANTLR syntax error at {line}:{column} - {msg}"
        raise ValueError(error_message)


def main():
    sg.theme('DarkGreen3')
    layout = [
        [sg.Text("Select a file to convert:", font='Helvetica 13')],
        [sg.Input(key="-FILE-"), sg.FileBrowse(font='Helvetica 11')],
        [sg.Text("Output Filename:", font='Helvetica 13')],
        [sg.Input(key="-OUTPUT-", font='Helvetica 11')],
        [sg.Button("Convert", key="-CONVERT-", font='Helvetica 11'),
         sg.Button("Quit", key="-QUIT-", font='Helvetica 11')],
        [sg.Output(size=(60, 20), key="-OUTPUT_LOG-")]
    ]
    window = sg.Window("Ruby to Python Converter", layout)
    output_element = window["-OUTPUT_LOG-"]
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "-QUIT-":
            break
        if event == "-CONVERT-":
            file_path = values["-FILE-"]
            output_filename = values["-OUTPUT-"]
            if file_path:
                if output_filename:
                    try:
                        inp = FileStream(file_path)
                        lexer = RubyLexer(inp)
                        stream = CommonTokenStream(lexer)
                        parser = RubyParser(stream)
                        parser.addErrorListener(GUIErrorListener())
                        tree = parser.program()
                        visitor = RubyVisitor()
                        res = visitor.visit(tree)
                        if visitor.errors:
                            for error in visitor.errors:
                                output_element.print(f"Error: {error}")
                            output_element.print("Conversion aborted due to errors. Fix errors and try again.")
                        else:
                            output_filename = str(output_filename) + ".py"
                            output = open(output_filename, "w")
                            output.write(res)
                            output.close()
                            output_element.update(res)
                    except ValueError as e:
                        output_element.print("")
                else:
                    output_element.print("Enter a filename to save the output!")
            else:
                output_element.print("Select a file to convert!")
    window.close()


if __name__ == '__main__':
    main()
