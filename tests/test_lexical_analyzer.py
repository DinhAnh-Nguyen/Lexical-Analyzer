"""
Test cases and examples for the Lexical Analyzer

This module contains test cases and examples for testing the lexical analyzer
with different types of inputs including edge cases and invalid inputs.
"""

import unittest
from src.lexical_analyzer import LexicalAnalyzer, TokenType, Token


class TestLexicalAnalyzer(unittest.TestCase):
    """Test cases for the LexicalAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = LexicalAnalyzer()
    
    def test_valid_number_tokenization(self):
        """Test tokenization of valid number inputs."""
        test_cases = [
            ("123", [TokenType.NUMBER]),
            ("45.67", [TokenType.NUMBER]),
            ("0", [TokenType.NUMBER]),
            ("999.999", [TokenType.NUMBER])
        ]
        
        for input_str, expected_types in test_cases:
            with self.subTest(input=input_str):
                tokens = self.analyzer.tokenize(input_str)
                self.assertEqual(len(tokens), 2)  # Number + EOF
                self.assertEqual(tokens[0].type, expected_types[0])
    
    def test_valid_list_tokenization(self):
        """Test tokenization of valid list inputs."""
        input_str = "[1, 2, 3]"
        tokens = self.analyzer.tokenize(input_str)
        
        expected_types = [
            TokenType.LEFT_BRACKET,
            TokenType.NUMBER,
            TokenType.COMMA,
            TokenType.NUMBER,
            TokenType.COMMA,
            TokenType.NUMBER,
            TokenType.RIGHT_BRACKET,
            TokenType.EOF
        ]
        
        self.assertEqual(len(tokens), len(expected_types))
        for i, expected_type in enumerate(expected_types):
            self.assertEqual(tokens[i].type, expected_type)
    
    def test_invalid_input_handling(self):
        """Test handling of invalid inputs."""
        invalid_inputs = [
            "abc",  # Invalid characters
            "[1, 2, abc]",  # Invalid characters in list
            "1.2.3",  # Invalid number format
            "[1, 2, 3",  # Missing closing bracket
        ]
        
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(ValueError):
                    self.analyzer.tokenize(invalid_input)
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        edge_cases = [
            ("", [TokenType.EOF]),  # Empty input
            ("   ", [TokenType.EOF]),  # Only whitespace
            ("[1]", [TokenType.LEFT_BRACKET, TokenType.NUMBER, TokenType.RIGHT_BRACKET, TokenType.EOF]),  # Single number
            ("[1,2,3,4,5,6,7,8,9,10]", None),  # Long list
        ]
        
        for input_str, expected_types in edge_cases:
            with self.subTest(input=input_str):
                if expected_types:
                    tokens = self.analyzer.tokenize(input_str)
                    self.assertEqual(len(tokens), len(expected_types))
                    for i, expected_type in enumerate(expected_types):
                        self.assertEqual(tokens[i].type, expected_type)
                else:
                    # Just ensure it doesn't raise an exception
                    tokens = self.analyzer.tokenize(input_str)
                    self.assertIsInstance(tokens, list)
    
    def test_whitespace_handling(self):
        """Test proper handling of whitespace."""
        inputs_with_whitespace = [
            "  [1, 2, 3]  ",
            "[ 1 , 2 , 3 ]",
            "\t[1,\t2,\t3]\n",
        ]
        
        for input_str in inputs_with_whitespace:
            with self.subTest(input=input_str):
                tokens = self.analyzer.tokenize(input_str)
                # Should not contain whitespace tokens
                whitespace_tokens = [t for t in tokens if t.type == TokenType.WHITESPACE]
                self.assertEqual(len(whitespace_tokens), 0)


class TestExamples:
    """Examples and demonstration cases for the lexical analyzer."""
    
    def __init__(self):
        self.analyzer = LexicalAnalyzer()
    
    def run_examples(self):
        """Run example cases to demonstrate the lexical analyzer."""
        examples = [
            "calculate [5, 8, 12, 4, 10]",
            "[1, 2, 3, 4, 5]",
            "CALCULATE [100, 200, 300]",
            "[0.5, 1.5, 2.5]",
            "[42]",
        ]
        
        print("Lexical Analyzer Examples")
        print("=" * 30)
        
        for example in examples:
            print(f"\nInput: {example}")
            try:
                tokens = self.analyzer.tokenize(example)
                print("Tokens:")
                for token in tokens:
                    print(f"  {token}")
            except ValueError as e:
                print(f"Error: {e}")
    
    def run_error_examples(self):
        """Run examples that should produce errors."""
        error_examples = [
            "calculate [5, 8, abc, 4, 10]",  # Invalid character
            "[1, 2, 3",  # Missing closing bracket
            "calc [1, 2, 3]",  # Invalid keyword
            "1.2.3",  # Invalid number format
            "[1, 2, 3,]",  # Trailing comma
        ]
        
        print("\nError Handling Examples")
        print("=" * 30)
        
        for example in error_examples:
            print(f"\nInput: {example}")
            try:
                tokens = self.analyzer.tokenize(example)
                print("Unexpectedly succeeded!")
            except ValueError as e:
                print(f"Expected error: {e}")


def run_tests():
    """Run all test cases."""
    print("Running Lexical Analyzer Tests")
    print("=" * 40)
    
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run examples
    examples = TestExamples()
    examples.run_examples()
    examples.run_error_examples()


if __name__ == "__main__":
    run_tests()

