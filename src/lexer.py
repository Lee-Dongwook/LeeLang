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
            ('LBRACKET', r'\['),         # 왼쪽 대괄호 (배열)
            ('RBRACKET', r'\]'),         # 오른쪽 대괄호 (배열)
            ('EQ', r'=='),               # 비교 연산자 (==)
            ('NEQ', r'!='),              # 비교 연산자 (!=)
            ('LT', r'<'),                # 비교 연산자 (<)
            ('GT', r'>'),                # 비교 연산자 (>)
            ('AND', r'&&'),              # 논리 연산자 (&&)
            ('OR', r'\|\|'),             # 논리 연산자 (||)
            ('PLUS', r'\+'),             # 산술 연산자 (+)
            ('MINUS', r'-'),             # 산술 연산자 (-)
            ('MULTIPLY', r'\*'),         # 산술 연산자 (*)
            ('DIVIDE', r'/'),            # 산술 연산자 (/)
            ('LPAREN', r'\('),           # 왼쪽 괄호
            ('RPAREN', r'\)'),           # 오른쪽 괄호
            ('LBRACE', r'\{'),           # 왼쪽 중괄호
            ('RBRACE', r'\}'),           # 오른쪽 중괄호
            ('COMMA', r','),             # 쉼표 (배열, 객체에서 사용)
            ('COLON', r':'),             # 콜론 (객체에서 키-값 구분)
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