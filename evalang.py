print("Hello World")

########Constants#########

digits = '0123456789'

########Custom Errors

class Errors:
    def __init__(self,error_name,error_details,position_start,position_end):
        
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.error_details = error_details
    def as_string(self):
        result = f'{self.error_name}: {self.error_details}'
        result += f'File {self.position_start.file_name} , line{self.position_start.ln + 1}'
        return result
class IllegalCharError(Errors):
    def __init__(self, error_details,position_start,position_end):
        super().__init__('illegal Character: ',error_details,position_start,position_end)

############################
##########Positions#########
############################
class Position:
    def __init__(self,idx,ln,col,file_name,file_text):
        self.file_name = file_name
        self.file_text = file_text
        self.idx = idx
        self.ln = ln
        self.col = col
    def advance (self, current_char):
        self.idx +=1
        self.col +=1

        if current_char == '\n':
            self.ln +=1
            self.col = 0
        return self
    def copy(self):
        return Position(self.idx,self.ln,self.col,self.file_name,self.file_text)
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
    def __init__(self,fn,value): ########### none to value
        self.fn = fn
        self.value = value
        self.pos = Position(-1,0,-1,fn,value)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.value[self.pos.idx] if self.pos.idx < len(self.value) else None    

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(PLUS_TOKEN,None))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(MINUS_TOKEN,None))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(MUL_TOKEN,None))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(DIV_TOKEN,None))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(LPAREN_TOKEN,None))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(RPAREN_TOKEN,None))
                self.advance()
            else:
                start_position = self.pos.copy()
                character = self.current_char
                self.advance()
                return [], IllegalCharError(start_position,self.pos,"'" + character + "'")

        return tokens, None
    
    def make_number(self):
        number_string = ''
        dot_count = 0
        while self.current_char != None and self.current_char in digits + '.':
            if self.current_char == '.':
                if dot_count ==1: break
                dot_count +=1
                number_string += '.'
            else:
                number_string += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(INT_TOKEN,int(number_string))
        else:
            return Token(FLOAT_TOKEN,float(number_string))

##################RUN##############

def Run(fileName,Text):
    lexer = Lexer(fileName,Text)
    tokens, errors = lexer.make_tokens()
    return tokens,errors