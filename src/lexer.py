import re

class Lexer: 
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        token_specification = [
            ('NUMBER', r'\d+'),          # 숫자 (정수)
            ('IDENT', r'[a-zA-Z_]\w*'),  # 변수, 함수 이름
            ('STRING', r'"[^"]*"'),      # 문자열
            ('ASSIGN', r'='),            # 할당 연산자
            ('LPAREN', r'\('),           # 왼쪽 괄호
            ('RPAREN', r'\)'),           # 오른쪽 괄호
            ('LBRACE', r'\{'),           # 왼쪽 중괄호
            ('RBRACE', r'\}'),           # 오른쪽 중괄호
            ('SEMICOLON', r';'),         # 세미콜론
            ('PRINT', r'print'),         # print 키워드
            ('IF', r'if'),               # if 키워드
            ('ELSE', r'else'),           # else 키워드
            ('FOR', r'for'),             # for 키워드
            ('WHILE', r'while'),         # while 키워드
            ('IN', r'in'),               # in 키워드
            ('RANGE', r'range'),         # range 키워드
            ('FN', r'fn'),               # fn 키워드
            ('RETURN',r'return'),        # return 키워드
            ('WHITESPACE', r'\s+'),      # 공백 (무시)
        ]
        token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification) 
        for match in re.finditer(token_regex, self.source_code):
            kind = match.lastgroup
            value = match.group(kind)
            if kind != 'WHITESPACE':
                self.tokens.append((kind, value))
        return self.tokens
    
if __name__ == "__main__":
    code = 'let name = "Alice"; print(name);'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print(tokens)