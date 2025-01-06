print("Hello World")

########Constants#########

digits = '0123456789'


#######Tokenization########
INT_TOKEN = 'INT'
FLOAT_TOKEN = 'FLOAT'
PLUS_TOKEN = 'PLUS'
MINUS_TOKEN = 'MINUS'
MUL_TOKEN = 'MUL'
DIV_TOKEN = 'DIV'
LPAREN_TOKEN = 'LPAREN'
RPAREN_TOKEN = 'RPAREN'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#########Lexer##########

class Lexer:
    def __init__(self,text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None    

    def make_tokens(self):
        tokens = []

        while self.current_char != none:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(PLUS_TOKEN))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(MINUS_TOKEN))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(MUL_TOKEN))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(DIV_TOKEN))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(LPAREN_TOKEN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(RPAREN_TOKEN))
                self.advance()

        return tokens

