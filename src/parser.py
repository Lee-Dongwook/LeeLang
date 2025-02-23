class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        """AST를 생성하는 함수"""
        ast = []
        while self.position < len(self.tokens):
            node = self.parse_statement()
            if node:
                ast.append(node)
        return ast
    
    def parse_statement(self):
        """각 코드 문장을 해석"""
        token_type, token_value = self.tokens[self.position]

        if token_type == 'IF':
            return self.parse_if()
        elif token_type == 'IDENT' and token_value == 'print':
            return self.parse_print()
        elif token_type == 'IDENT':
            return self.parse_assignment()

        return None
    
    def parse_if(self):
        """if 조건문을 파싱"""
        self.position += 1
        self.position += 1
        condition = self.tokens[self.position]
        self.position += 1
        self.position += 1
        self.position += 1

        if_body = []
        while self.tokens[self.position][0] != 'RBRACE':
            if_body.append(self.parse_statement())
        self.position += 1

        else_body = None
        if self.position < len(self.tokens) and self.tokens[self.position][0] == 'ELSE':
            self.position += 1
            self.position += 1
            else_body = []
            while self.tokens[self.position][0] != 'RBRACE':
                else_body.append(self.parse_statement())
            self.position += 1

        return  {'type':'IF', 'condition':condition, 'if_body':if_body, 'else_body':else_body}

    def parse_print(self):
        """print 문을 파싱"""
        self.position += 1
        self.position += 1
        expr = self.tokens[self.position]
        self.position += 1
        self.position += 1
        self.position += 1
        return {'type':'PRINT', 'value': expr}
    
    def parse_assignment(self):
        """변수 할당"""
        var_name = self.tokens[self.position][1]
        self.position += 1 
        self.position += 1 
        value = self.tokens[self.position]  
        self.position += 1  
        self.position += 1  
        return {'type': 'ASSIGNMENT', 'name': var_name, 'value': value}

if __name__ == "__main__":
    from lexer import Lexer

    code = 'let name = "Alice"; print(name);'
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    print(ast) 