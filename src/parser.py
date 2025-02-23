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
        elif token_type == 'FN':
            return self.parse_function()
        elif token_type == 'IDENT' and self.position + 1 < len(self.tokens) and self.tokens[self.position + 1][0] == 'LPAREN':
            return self.parse_function_call()
        elif token_type == 'RETURN':
            return self.parse_return()
        elif token_type == 'FOR':
            return self.parse_for()
        elif token_type == 'WHILE':
            return self.parse_while()
        elif token_type == 'IDENT' and token_value == 'print':
            return self.parse_print()
        elif token_type == 'IDENT':
            return self.parse_assignment()

        return None
    
    def parse_function(self):
        """함수 정의 파싱"""
        self.position += 1  # 'fn' 스킵
        func_name = self.tokens[self.position][1]  # 함수 이름
        self.position += 1  # 함수 이름 스킵
        self.position += 1  # '(' 스킵

        params = []
        while self.tokens[self.position][0] != 'RPAREN':
            param_name = self.tokens[self.position][1]
            params.append(param_name)
            self.position += 1  # 변수 이동
            if self.tokens[self.position][0] == 'RPAREN':
                break
            self.position += 1  # ',' 스킵

        self.position += 1  # ')' 스킵
        self.position += 1  # '{' 스킵

        body = []
        while self.tokens[self.position][0] != 'RBRACE':
            body.append(self.parse_statement())
        self.position += 1  # '}' 스킵

        return {'type': 'FUNCTION', 'name': func_name, 'params': params, 'body': body}

    def parse_function_call(self):
        """함수 호출 파싱"""
        func_name = self.tokens[self.position][1]
        self.position += 1  # 함수 이름 스킵
        self.position += 1  # '(' 스킵

        args = []
        while self.tokens[self.position][0] != 'RPAREN':
            arg = self.tokens[self.position]
            args.append(arg)
            self.position += 1
            if self.tokens[self.position][0] == 'RPAREN':
                break
            self.position += 1  # ',' 스킵

        self.position += 1  # ')' 스킵
        self.position += 1  # ';' 스킵

        return {'type': 'FUNCTION_CALL', 'name': func_name, 'args': args}

    def parse_return(self):
        """return 문 파싱"""
        self.position += 1  # 'return' 스킵
        return_value = self.tokens[self.position]
        self.position += 1  # 값 이동
        self.position += 1  # ';' 스킵
        return {'type': 'RETURN', 'value': return_value}

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
    
    def parse_for(self):
        """for 문을 파싱"""
        self.position += 1
        loop_var = self.tokens[self.position][1]
        self.position += 2
        self.position += 1
        self.position += 1
        range_value = self.tokens[self.position]
        self.position += 2
        self.position += 1

        body = []
        while self.tokens[self.position][0] != 'RBRACE':
            body.append(self.parse_statement())
        self.position += 1

        return {'type':'FOR', 'loop_var':loop_var, 'range':range_value, 'body':body}
    
    def parse_while(self):
        """while 문을 파싱"""
        self.position += 1 
        self.position += 1 
        condition = self.tokens[self.position] 
        self.position += 1  
        self.position += 1  
        self.position += 1  

        body = []
        while self.tokens[self.position][0] != 'RBRACE':
            body.append(self.parse_statement())
        self.position += 1  

        return {'type': 'WHILE', 'condition': condition, 'body': body}

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