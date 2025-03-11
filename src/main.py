# main.py

import waiip

def main():
    # Example usage of the `MyClass` class
    my_token = waiip.Token("type", "litral")
    print(f"Initial value: {my_token.get_type()}")
    print(f"Initial value: {my_token.get_literal()}")

if __name__ == "__main__":
    main()
