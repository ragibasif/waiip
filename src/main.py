# main.py

from token import Token, TokenTypes
from lexer import Lexer

def TestToken():
    my_token = Token()
    my_token.t_type = "test type"
    my_token.t_literal = "test literal"
    print(f"Initial value: {my_token.t_type}")
    print(f"Initial value: {my_token.t_literal}")

    my_token2 = Token()
    print(f"Initial value: {my_token2.t_type}")
    print(f"Initial value: {my_token2.t_literal}")



def TestNextToken():
    test_input = "=+(){},;"
    token_types = [TokenTypes.ASSIGN, TokenTypes.PLUS , TokenTypes.LPAREN,
                   TokenTypes.RPAREN, TokenTypes.LBRACE, TokenTypes.RBRACE,
                   TokenTypes.COMMA, TokenTypes.SEMICOLON, TokenTypes.EOF]
    expected_tokens = []
    for i in range(len(token_types)):
        token = Token(token_types[i].name ,token_types[i].value)
        expected_tokens.append(token)
    l = Lexer()
    l.New(test_input)
    for i, tt in enumerate(expected_tokens):
        tok = l.NextToken()
        if not tok.t_type == tt.t_type:
            print(f"Error: tok.t_type is {tok.t_type}. Expected {tt.t_type}")
        if not tok.t_literal == tt.t_literal:
            print(f"Error: tok.t_literal is {tok.t_literal}. Expected {tt.t_literal}")



def main():
    TestToken()
    TestNextToken()

if __name__ == "__main__":
    main()
