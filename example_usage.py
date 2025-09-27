"""
Example usage script for the Lexical Analyzer project.

This script demonstrates how to use the different components of the project.
"""

import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from lexical_analyzer import LexicalAnalyzer
from grammar import GrammarAnalyzer
from pseudocode import calculate_average_implementation
from utils import parse_number_list, format_output


def demonstrate_lexical_analyzer():
    """Demonstrate the lexical analyzer functionality."""
    print("Lexical Analyzer Demonstration")
    print("=" * 35)
    
    analyzer = LexicalAnalyzer()
    
    # Test cases
    test_inputs = [
        "calculate [5, 8, 12, 4, 10]",
        "[1, 2, 3, 4, 5]",
        "CALCULATE [100, 200, 300]",
        "[0.5, 1.5, 2.5]",
        "[42]",
    ]
    
    for i, test_input in enumerate(test_inputs, 1):
        print(f"\nTest Case {i}: {test_input}")
        try:
            tokens = analyzer.tokenize(test_input)
            print("Tokens:")
            for token in tokens:
                print(f"  {token}")
        except ValueError as e:
            print(f"Error: {e}")


def demonstrate_grammar_analysis():
    """Demonstrate the grammar analysis functionality."""
    print("\nGrammar Analysis Demonstration")
    print("=" * 40)
    
    analyzer = GrammarAnalyzer()
    
    # Analyze ambiguities
    print("\n1. BNF Grammar Ambiguity Analysis:")
    ambiguities = analyzer.analyze_ambiguity()
    for key, value in ambiguities.items():
        print(f"\n{key.replace('_', ' ').title()}:")
        for item in value:
            print(f"  - {item}")
    
    # Generate parse trees
    print("\n2. Parse Tree Generation:")
    test_input = "calculate [5, 8, 12, 4, 10]"
    
    print(f"\nInput: {test_input}")
    print("\nBNF Parse Tree:")
    bnf_tree = analyzer.generate_parse_tree_bnf(test_input)
    print(f"  {bnf_tree}")
    
    print("\nEBNF Parse Tree:")
    ebnf_tree = analyzer.generate_parse_tree_ebnf(test_input)
    print(f"  {ebnf_tree}")


def demonstrate_average_calculation():
    """Demonstrate the average calculation functionality."""
    print("\nAverage Calculation Demonstration")
    print("=" * 40)
    
    # Test cases
    test_cases = [
        [5, 8, 12, 4, 10],  # Original example
        [1, 2, 3, 4, 5],    # Simple case
        [100, 200, 300],    # Large numbers
        [0.5, 1.5, 2.5],    # Decimal numbers
        [42],               # Single number
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_case}")
        try:
            result = calculate_average_implementation(test_case)
            print(f"✓ Successfully calculated average: {result:.2f}")
        except ValueError as e:
            print(f"✗ Error: {e}")


def demonstrate_utilities():
    """Demonstrate the utility functions."""
    print("\nUtilities Demonstration")
    print("=" * 30)
    
    # Test parse_number_list
    test_inputs = [
        "[1, 2, 3, 4, 5]",
        "1,2,3,4,5",
        "[5.5, 8.2, 12.7]",
        "100,200,300"
    ]
    
    print("\n1. Testing parse_number_list:")
    for test_input in test_inputs:
        try:
            result = parse_number_list(test_input)
            print(f"  Input: {test_input} -> Output: {result}")
        except ValueError as e:
            print(f"  Input: {test_input} -> Error: {e}")
    
    # Test format_output
    print("\n2. Testing format_output:")
    numbers = [5, 8, 12, 4, 10]
    average = sum(numbers) / len(numbers)
    formatted = format_output(numbers, average)
    print(f"  {formatted}")


def demonstrate_error_handling():
    """Demonstrate error handling capabilities."""
    print("\nError Handling Demonstration")
    print("=" * 35)
    
    analyzer = LexicalAnalyzer()
    
    # Error cases
    error_cases = [
        "calculate [5, 8, abc, 4, 10]",  # Invalid character
        "[1, 2, 3",                      # Missing closing bracket
        "calc [1, 2, 3]",                # Invalid keyword
        "1.2.3",                         # Invalid number format
        "[1, 2, 3,]",                    # Trailing comma
    ]
    
    for i, error_case in enumerate(error_cases, 1):
        print(f"\nError Test {i}: {error_case}")
        try:
            tokens = analyzer.tokenize(error_case)
            print("Unexpectedly succeeded!")
        except ValueError as e:
            print(f"Expected error: {e}")


def main():
    """Main demonstration function."""
    print("Lexical Analyzer Project Demonstration")
    print("=" * 50)
    print("This script demonstrates all the key components of the project.")
    print()
    
    # Run all demonstrations
    demonstrate_lexical_analyzer()
    demonstrate_grammar_analysis()
    demonstrate_average_calculation()
    demonstrate_utilities()
    demonstrate_error_handling()
    
    print("\n" + "=" * 50)
    print("Demonstration completed!")
    print("You can now explore the individual components in more detail.")
    print("Run 'python main.py' for the interactive menu.")


if __name__ == "__main__":
    main()

