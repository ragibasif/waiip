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
    def NextToken(self) -> Token:
        tok = Token()

        match self.l_ch:
            case '=':
                tok = newToken(TokenTypes.ASSIGN, self.l_ch)
            case ';':
                tok = newToken(TokenTypes.SEMICOLON, self.l_ch)
            case '(':
                tok = newToken(TokenTypes.LPAREN, self.l_ch)
            case ')':
                tok = newToken(TokenTypes.RPAREN, self.l_ch)
            case ',':
                tok = newToken(TokenTypes.COMMA, self.l_ch)
            case '+':
                tok = newToken(TokenTypes.PLUS, self.l_ch)
            case '{':
                tok = newToken(TokenTypes.LBRACE, self.l_ch)
            case '}':
                tok = newToken(TokenTypes.RBRACE, self.l_ch)
            case '':
                tok.t_literal = ""
                tok.t_type = TokenTypes.EOF.name

        self.readChar()
        return tok

def newToken(tokenType: TokenTypes, ch: str) -> Token:
    return Token(t_type=tokenType.name, t_literal=ch)


