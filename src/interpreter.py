from stdlib import StdLib

class Interpreter:
    def __init__(self,ast):
        self.ast = ast
        self.variables = {}
        self.functions = {}
        self.builtins = {
            'length': StdLib.length,
            "uppercase": StdLib.uppercase,
            "lowercase": StdLib.lowercase,
            "sqrt": StdLib.sqrt,
            "abs": StdLib.abs,
            "pow": StdLib.pow,
            "time": StdLib.time,
            "sleep": StdLib.sleep
        }
    
    def run(self):
        """AST를 실행"""
        for node in self.ast:
            self.evaluate(node)
        
    def evaluate(self, node):
        """각 노드를 해석하고 실행"""
        if node["type"] == "ASSIGNMENT":
            var_name = node["name"]
            value_type = node["value"]["type"]

            if value_type == "ARRAY":
                self.variables[var_name] = [int(elem[1]) if elem[0] == "NUMBER" else elem[1] for elem in node["value"]["elements"]]
            elif value_type == "OBJECT":
                self.variables[var_name] = node["value"]["pairs"]
            else:
                value_type, value = node["value"]
                self.variables[var_name] = int(value) if value_type == "NUMBER" else value
        
        elif node["type"] == "FUNCTION":
            func = self.functions.get(node["name"])
            if not func:
                raise Exception(f"Undefined function {node['name']}")
            params = func["params"]
            args = node["args"]
            local_vars = {}
            for i in range(len(params)):
                local_vars[params[i]] = args[i][1]
            for stmt in func["body"]:
                if stmt["type"] == "RETURN":
                    return_value_type, return_value = stmt["value"]
                    print(return_value)
                    return return_value
                self.evaluate(stmt)
        
        elif node["type"] == "RETURN":
            value_type, value = node["value"]
            return value    
        
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
        
        elif node["type"] == "FOR":
            loop_var = node["loop_var"]
            range_type, range_value = node["range"]
            for i in range(int(range_value)):
                self.variables[loop_var] = i
                for stmt in node["body"]:
                    self.evaluate(stmt)
        
        elif node["type"] == "WHILE":
            condition_type, condition_value = node["condition"]
            while int(self.variables.get(condition_value, 0)):  # 값이 0이 아닐 때 실행
                for stmt in node["body"]:
                    self.evaluate(stmt)
        
        elif node["type"] == "EXPRESSION":
            left_type, left_value = node["left"]
            operator_type, operator_value = node["operator"]
            right_type, right_value = node["right"]

            left = int(self.variables.get(left_value, left_value)) if left_type == "IDENT" else int(left_value)
            right = int(self.variables.get(right_value, right_value)) if right_type == "IDENT" else int(right_value)

            if operator_type == "PLUS":
                result = left + right
            elif operator_type == "MINUS":
                result = left - right
            elif operator_type == "MULTIPLY":
                result = left * right
            elif operator_type == "DIVIDE":
                result = left / right
            elif operator_type == "EQ":
                result = left == right
            elif operator_type == "NEQ":
                result = left != right
            elif operator_type == "LT":
                result = left < right
            elif operator_type == "GT":
                result = left > right
            elif operator_type == "AND":
                result = left and right
            elif operator_type == "OR":
                result = left or right
            else:
                raise Exception(f"Unknown operator {operator_value}")

            print(result)
        
        elif node["type"] == "ARRAY_ACCESS":
            """배열 요소 접근"""
            array_name = node["array_name"]
            index_type, index_value = node["index"]
            index = int(self.variables.get(index_value, index_value)) if index_type == "IDENT" else int(index_value)

            if array_name in self.variables and isinstance(self.variables[array_name], list):
                print(self.variables[array_name][index])  # 배열 요소 출력
            else:
                raise Exception(f"Undefined array {array_name}")
        
        elif node["type"] == "FUNCTION_CALL":
            func_name = node["name"]
            args = [arg[1] for arg in node["args"]]

            if func_name in self.builtins:  # 표준 라이브러리 함수 실행
                result = self.builtins[func_name](*args)
                print(result)
            elif func_name in self.functions:  # 사용자 정의 함수 실행
                func = self.functions[func_name]
                local_vars = dict(zip(func["params"], args))
                for stmt in func["body"]:
                    if stmt["type"] == "RETURN":
                        return self.evaluate(stmt["value"])
                    self.evaluate(stmt)
            else:
                raise Exception(f"Undefined function {func_name}")
        

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