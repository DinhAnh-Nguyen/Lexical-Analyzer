"""
Lexical Analyzer for Average Calculation Problem

This module contains the main lexical analyzer implementation for processing
input based on the problem statement defined in Part B of the assignment.
"""

import re
from typing import List, Tuple, Union
from enum import Enum


class TokenType(Enum):
    """Enumeration of token types for the lexical analyzer."""
    NUMBER = "NUMBER"
    COMMA = "COMMA"
    LEFT_BRACKET = "LEFT_BRACKET"
    RIGHT_BRACKET = "RIGHT_BRACKET"
    AVERAGE_KEYWORD = "AVERAGE_KEYWORD"
    CALCULATE_KEYWORD = "CALCULATE_KEYWORD"
    WHITESPACE = "WHITESPACE"
    EOF = "EOF"
    INVALID = "INVALID"


class Token:
    """Represents a token with its type and value."""
    
    def __init__(self, token_type: TokenType, value: str, position: int = 0):
        self.type = token_type
        self.value = value
        self.position = position
    
    def __repr__(self):
        return f"Token({self.type.value}, '{self.value}', pos={self.position})"


class LexicalAnalyzer:
    """
    Lexical analyzer for processing input related to average calculation.
    
    This class tokenizes input strings and provides error handling for
    invalid inputs based on the grammar defined in Part B.
    """
    
    def __init__(self):
        """Initialize the lexical analyzer with token patterns."""
        # Define token patterns using regular expressions
        self.token_patterns = [
            (TokenType.NUMBER, r'\d+(\.\d+)?'),  # Numbers (integers and floats)
            (TokenType.COMMA, r','),             # Comma separator
            (TokenType.LEFT_BRACKET, r'\['),     # Left bracket
            (TokenType.RIGHT_BRACKET, r'\]'),    # Right bracket
            (TokenType.AVERAGE_KEYWORD, r'average|AVERAGE'),  # Average keyword
            (TokenType.CALCULATE_KEYWORD, r'calculate|CALCULATE'),  # Calculate keyword
            (TokenType.WHITESPACE, r'\s+'),      # Whitespace
        ]
    
    def tokenize(self, input_string: str) -> List[Token]:
        """
        Tokenize the input string into a list of tokens.
        
        Args:
            input_string: The input string to tokenize
            
        Returns:
            List of Token objects
            
        Raises:
            ValueError: If invalid input is detected
        """
        tokens = []
        position = 0
        
        while position < len(input_string):
            matched = False
            
            for token_type, pattern in self.token_patterns:
                regex = re.compile(pattern)
                match = regex.match(input_string, position)
                
                if match:
                    value = match.group(0)
                    # Skip whitespace tokens but don't add them to the token list
                    if token_type != TokenType.WHITESPACE:
                        tokens.append(Token(token_type, value, position))
                    position = match.end()
                    matched = True
                    break
            
            if not matched:
                # Invalid character found
                invalid_char = input_string[position]
                error_msg = f"Invalid character '{invalid_char}' at position {position}"
                raise ValueError(error_msg)
        
        # Add EOF token
        tokens.append(Token(TokenType.EOF, '', position))
        return tokens
    
    def validate_input(self, input_string: str) -> bool:
        """
        Validate the input string for basic syntax errors.
        
        Args:
            input_string: The input string to validate
            
        Returns:
            True if input is valid, False otherwise
        """
        try:
            tokens = self.tokenize(input_string)
            # Add your validation logic here
            # This is a placeholder - implement based on your grammar
            return True
        except ValueError:
            return False
    
    def get_user_input(self) -> str:
        """
        Get input from the user with error handling.
        
        Returns:
            The user input string
        """
        while True:
            try:
                user_input = input("Enter numbers to calculate average (e.g., [5, 8, 12, 4, 10]): ")
                if self.validate_input(user_input):
                    return user_input
                else:
                    print("Error: Invalid input format. Please try again.")
            except KeyboardInterrupt:
                print("\nProgram interrupted by user.")
                return ""
            except Exception as e:
                print(f"Error: {e}")
                print("Please try again.")


def main():
    """
    Main function to demonstrate the lexical analyzer.
    
    This function provides a basic interface for testing the lexical analyzer
    with different types of inputs.
    """
    analyzer = LexicalAnalyzer()
    
    print("Lexical Analyzer for Average Calculation")
    print("=" * 50)
    print("Enter 'quit' to exit the program.")
    print()
    
    while True:
        try:
            user_input = analyzer.get_user_input()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Tokenize the input
            tokens = analyzer.tokenize(user_input)
            
            print(f"\nInput: {user_input}")
            print("Tokens:")
            for token in tokens:
                print(f"  {token}")
            print()
            
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

