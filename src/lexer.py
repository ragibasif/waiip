# lexer.py

import token


class Lexer:
    """Lexer class"""

    def __init__(self) -> None:
        """Initialize the class with input"""
        self.l_input = ""
        self.l_position = 0
        self.l_readPosition = 0
        self.l_ch = ""

    def New(self, l_input: str) -> None:
        self.l_input = l_input
        self.readChar()

    def readChar(self) -> None:
        """Give the next character and advance the position of the input
        string."""
        if self.l_readPosition >= len(self.l_input):
            self.l_ch = ""
        else:
            self.l_ch = self.l_input[self.l_readPosition]
        self.l_position = self.l_readPosition
        self.l_readPosition += 1

    def readIdentifier(self) -> str:
        if isLetter(self.l_ch):
            self.readChar()
        return self.l_input[self.l_position]

    def newToken(self, tokenType: token.TokenTypes, ch: str) -> token.Token:
        tok = token.Token(t_type=tokenType, t_literal=ch)
        return tok

    def skipWhitespace(self) -> None:
        if (
            self.l_ch == " "
            or self.l_ch == "\t"
            or self.l_ch == "\n"
            or self.l_ch == "\r"
        ):
            self.readChar()

    def NextToken(self) -> token.Token:
        tok = token.Token("", "")

        match self.l_ch:
            case "=":
                tok = self.newToken(token.TokenTypes.ASSIGN.name, self.l_ch)
            case ";":
                tok = self.newToken(token.TokenTypes.SEMICOLON.name, self.l_ch)
            case "(":
                tok = self.newToken(token.TokenTypes.LPAREN.name, self.l_ch)
            case ")":
                tok = self.newToken(token.TokenTypes.RPAREN.name, self.l_ch)
            case ",":
                tok = self.newToken(token.TokenTypes.COMMA.name, self.l_ch)
            case "+":
                tok = self.newToken(token.TokenTypes.PLUS.name, self.l_ch)
            case "{":
                tok = self.newToken(token.TokenTypes.LBRACE.name, self.l_ch)
            case "}":
                tok = self.newToken(token.TokenTypes.RBRACE.name, self.l_ch)
            case "":
                tok.t_type = token.TokenTypes.EOF.name
                tok.t_literal = token.TokenTypes.EOF.value
            case _:
                if isLetter(self.l_ch):
                    tok.t_literal = self.readIdentifier()
                    tok.t_type = token.LookupIdent(tok.t_literal)
                    return tok
                else:
                    tok = self.newToken(token.TokenTypes.ILLEGAL.name, self.l_ch)

        self.readChar()
        return tok


def isLetter(ch: str) -> bool:
    """Helper function to check if a character is in the alphabet"""
    return "a" <= ch and ch <= "z" or "A" <= ch and ch <= "Z" or ch == "_"
