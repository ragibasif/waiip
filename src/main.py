# main.py

from token import Token, TokenTypes
from lexer import Lexer

def TestToken():
    print("TestToken")
    my_token = Token("hello", "world")
    my_token.t_type = "test type"
    my_token.t_literal = "test literal"
    print(f"Initial value: {my_token.t_type}")
    print(f"Initial value: {my_token.t_literal}")

    my_token2 = Token(TokenTypes.ASSIGN.name, "=")
    print(f"Initial value: {my_token2.t_type}")
    print(f"Initial value: {my_token2.t_literal}")



def TestNextToken_zero():
    print("TestNextToken_zero")
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
        print("tt",tt)
        print("tt.t_type",tt.t_type)
        print("tt.t_literal",tt.t_literal)
        tok = l.NextToken()
        print("tok",tok)
        print("tok.t_type",tok.t_type)
        print("tok.t_literal",tok.t_literal)
        if not tok.t_type == tt.t_type:
            print(f"Error: tok.t_type is {tok.t_type}. Expected {tt.t_type}")
        if not tok.t_literal == tt.t_literal:
            print(f"Error: tok.t_literal is {tok.t_literal}. Expected {tt.t_literal}")

def TestNextToken_one():
    print("TestNextToken_one")
    test_input = """
        let five = 5;
        let ten = 10;
        let add = fn(x, y) {
            x + y;
        };
        let result = add(five, ten);
    """
    token_types = [TokenTypes.LET, TokenTypes.IDENT, TokenTypes.ASSIGN, TokenTypes.INT, TokenTypes.SEMICOLON, TokenTypes.LET, TokenTypes.IDENT, TokenTypes.ASSIGN, TokenTypes.INT, TokenTypes.SEMICOLON, TokenTypes.LET, TokenTypes.IDENT, TokenTypes.ASSIGN, TokenTypes.FUNCTION, TokenTypes.LPAREN, TokenTypes.IDENT, TokenTypes.COMMA, TokenTypes.IDENT, TokenTypes.RPAREN, TokenTypes.LBRACE, TokenTypes.IDENT, TokenTypes.PLUS, TokenTypes.IDENT, TokenTypes.SEMICOLON, TokenTypes.RBRACE, TokenTypes.SEMICOLON, TokenTypes.LET, TokenTypes.IDENT, TokenTypes.ASSIGN, TokenTypes.IDENT, TokenTypes.LPAREN, TokenTypes.IDENT, TokenTypes.COMMA, TokenTypes.IDENT, TokenTypes.RPAREN, TokenTypes.SEMICOLON, TokenTypes.EOF]
    expected_tokens = []
    for i in range(len(token_types)):
        token = Token(token_types[i].name ,token_types[i].value)
        expected_tokens.append(token)
    l = Lexer()
    l.New(test_input)
    print(l.l_input)
    print(l.l_ch)
    for i, tt in enumerate(expected_tokens):
        print("tt",tt)
        print("tt.t_type",tt.t_type)
        print("tt.t_literal",tt.t_literal)
        tok = l.NextToken()
        print("tok",tok)
        print("tok.t_type",tok.t_type)
        print("tok.t_literal",tok.t_literal)

        tok = l.NextToken()
        if not tok.t_type == tt.t_type:
            print(f"Error: tok.t_type is {tok.t_type}. Expected {tt.t_type}")
        if not tok.t_literal == tt.t_literal:
            print(f"Error: tok.t_literal is {tok.t_literal}. Expected {tt.t_literal}")




def main():
    # TestToken()
    # TestNextToken_zero()
    TestNextToken_one()

if __name__ == "__main__":
    main()
