import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def repl():
    print("🔥 MyLang REPL (Type 'exit' to quit) 🔥")
    
    while True:
        try:
          code = input(">>> ")
          if code.strip().lower() == 'exit':
             print('Exiting MyLang REPL. GoodBye!')
             break
          
          lexer = Lexer(code)
          tokens = lexer.tokenize()

          parser = Parser(tokens)
          ast = parser.parse()

          interpreter = Interpreter(ast)
          interpreter.run()
        
        except Exception as e:
           print(f"Error: {e}")

if __name__ == "__main__":
    repl()