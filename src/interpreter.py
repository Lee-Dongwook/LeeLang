class Interpreter:
    def __init__(self,ast):
        self.ast = ast
        self.variables = {}
    
    def run(self):
        """AST를 실행"""
        for node in self.ast:
            self.evaluate(node)
        
    def evaluate(self, node):
        """각 노드를 해석하고 실행"""
        if node["type"] == "ASSIGNMENT":
            var_name = node["name"]
            value_type, value = node["value"]
            self.variables[var_name] = value
        elif node["type"] == "PRINT":
            value_type, value = node["value"]
            if value_type == "IDENT":
                print(self.variables.get(value,"Undefined variable"))
            else:
                print(value)
        elif node["type"] == 'IF':
            condition_type,condition_value = node["condition"]
            condition_result = self.variables.get(condition_value, False) if condition_type == "IDENT" else int(condition_value)

            if condition_result:
                for stmt in node["if_body"]:
                    self.evaluate(stmt)
            elif node["else_body"]:
                for stmt in node["else_body"]:
                    self.evaluate(stmt)

if __name__ == "__main__":
    from lexer import Lexer
    from parser import Parser

    code = """
    let age = 20;
    if (age > 18) {
        print("Adult");
    } else {
        print("Minor");
    }
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter(ast)
    interpreter.run()