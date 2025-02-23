#!/usr/bin/env python3
import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_file(filename):
    """.myl 파일을 실행하는 함수"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            code = file.read()

        lexer = Lexer(code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter(ast)
        interpreter.run()

    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: mylang <filename>.myl")
    else:
        run_file(sys.argv[1])
