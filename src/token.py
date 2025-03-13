# token.py

from enum import Enum

class TokenTypes(Enum) :
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"
    IDENT = "IDENT"
    INT = "INT"
    ASSIGN = "="
    PLUS = "+"
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    FUNCTION = "FUNCTION"
    LET = "LET"


class Token:
    """Token class."""

    def __init__(self, t_type: str , t_literal: str ) -> None:
        """Initialize the class with a type and literal."""
        self.t_type = t_type
        self.t_literal = t_literal

