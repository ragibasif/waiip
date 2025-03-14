# lexer.py
# TODO: modularize this file

from token import Token, TokenTypes

class Lexer:
    """Lexer class"""

    def __init__(self) -> None:
        """Initialize the class with input"""
        self.l_input = ""
        self.l_position = 0
        self.l_readPosition = 0
        self.l_ch = ''

    def New(self, l_input: str) -> None:
        self.l_input = l_input
        self.readChar()

    def readChar(self) -> None:
        """Give the next character and advance the position of the input
        string."""
        if self.l_readPosition >= len(self.l_input):
            self.l_ch = ''
        else:
            self.l_ch = self.l_input[self.l_readPosition]
        self.l_position = self.l_readPosition
        self.l_readPosition += 1

    def readIdentifier(self) -> str:
        if isLetter(self.l_ch):
            self.readChar()
        return self.l_input[self.l_position]


    def newToken(self,tokenType: TokenTypes, ch: str) -> Token:
        tok = Token(t_type=tokenType, t_literal=ch)
        return tok

    def NextToken(self) -> Token:
        tok = Token("","")

        match self.l_ch:
            case '=':
                tok = self.newToken(TokenTypes.ASSIGN.name, self.l_ch)
            case ';':
                tok = self.newToken(TokenTypes.SEMICOLON.name, self.l_ch)
            case '(':
                tok = self.newToken(TokenTypes.LPAREN.name, self.l_ch)
            case ')':
                tok = self.newToken(TokenTypes.RPAREN.name, self.l_ch)
            case ',':
                tok = self.newToken(TokenTypes.COMMA.name, self.l_ch)
            case '+':
                tok = self.newToken(TokenTypes.PLUS.name, self.l_ch)
            case '{':
                tok = self.newToken(TokenTypes.LBRACE.name, self.l_ch)
            case '}':
                tok = self.newToken(TokenTypes.RBRACE.name, self.l_ch)
            case '':
                tok.t_type = TokenTypes.EOF.name
                tok.t_literal = TokenTypes.EOF.value
            case _:
                if isLetter(self.l_ch):
                    tok.t_literal = self.readIdentifier()
                    return tok
                else:
                    tok = self.newToken(TokenTypes.ILLEGAL.name, self.l_ch)

        self.readChar()
        return tok


def isLetter(ch:str) -> bool:
    """Helper function to check if a character is in the alphabet"""
    return 'a' <= ch and ch <= 'z' or 'A' <= ch and ch <= 'Z' or ch == '_'
