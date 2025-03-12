# waiip.py
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
    """A simple class example."""

    def __init__(self, type: str, literal: str) -> None:
        """Initialize the class with a type and literal."""
        self.type = type
        self.literal = literal

    def get_type(self) -> str:
        """Return the stored type."""
        return self.type

    def set_type(self, type: str) -> None:
        """Set a new type."""
        self.type = type
        ...
    def get_literal(self) -> str:
        """Return the stored literal."""
        return self.literal

    def set_literal(self, literal: str) -> None:
        """Set a new literal."""
        self.literal = literal
