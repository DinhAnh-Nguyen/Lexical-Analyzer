"""
Utility functions and helper classes for the Lexical Analyzer project.

This module contains utility functions that can be used across different
parts of the project.
"""

import re
from typing import List, Dict, Any


def parse_number_list(input_string: str) -> List[float]:
    """
    Parse a string representation of a number list into a list of floats.
    
    Args:
        input_string: String like "[1, 2, 3]" or "1,2,3"
        
    Returns:
        List of float numbers
        
    Raises:
        ValueError: If the input format is invalid
    """
    # Remove brackets if present
    cleaned_input = input_string.strip()
    if cleaned_input.startswith('[') and cleaned_input.endswith(']'):
        cleaned_input = cleaned_input[1:-1]
    
    # Split by comma and convert to floats
    try:
        numbers = [float(x.strip()) for x in cleaned_input.split(',') if x.strip()]
        return numbers
    except ValueError as e:
        raise ValueError(f"Invalid number format in input: {e}")


def format_output(numbers: List[float], average: float) -> str:
    """
    Format the output for display.
    
    Args:
        numbers: List of numbers
        average: Calculated average
        
    Returns:
        Formatted string for display
    """
    numbers_str = ", ".join(map(str, numbers))
    return f"Numbers: [{numbers_str}]\nAverage: {average:.2f}"


def validate_number_list(numbers: List[Any]) -> bool:
    """
    Validate that a list contains only numeric values.
    
    Args:
        numbers: List to validate
        
    Returns:
        True if all elements are numeric, False otherwise
    """
    try:
        for num in numbers:
            float(num)
        return True
    except (ValueError, TypeError):
        return False


def extract_numbers_from_text(text: str) -> List[float]:
    """
    Extract all numbers from a text string using regex.
    
    Args:
        text: Input text to extract numbers from
        
    Returns:
        List of extracted numbers as floats
    """
    # Pattern to match integers and floats
    number_pattern = r'-?\d+\.?\d*'
    matches = re.findall(number_pattern, text)
    
    try:
        return [float(match) for match in matches]
    except ValueError:
        return []


def create_error_message(error_type: str, details: str = "") -> str:
    """
    Create standardized error messages.
    
    Args:
        error_type: Type of error
        details: Additional error details
        
    Returns:
        Formatted error message
    """
    error_messages = {
        "invalid_input": "Invalid input format. Please provide a valid list of numbers.",
        "empty_list": "Cannot calculate average of an empty list.",
        "non_numeric": "All values must be numeric.",
        "syntax_error": "Syntax error in input.",
        "parsing_error": "Error parsing input."
    }
    
    base_message = error_messages.get(error_type, "Unknown error occurred.")
    
    if details:
        return f"{base_message} Details: {details}"
    return base_message


def log_operation(operation: str, input_data: Any, result: Any = None, error: str = None) -> None:
    """
    Log operations for debugging purposes.
    
    Args:
        operation: Name of the operation
        input_data: Input data for the operation
        result: Result of the operation (if successful)
        error: Error message (if failed)
    """
    print(f"[LOG] Operation: {operation}")
    print(f"[LOG] Input: {input_data}")
    
    if error:
        print(f"[LOG] Error: {error}")
    else:
        print(f"[LOG] Result: {result}")
    
    print("[LOG] " + "-" * 40)


class InputValidator:
    """
    Class for validating different types of input.
    """
    
    @staticmethod
    def validate_list_format(input_string: str) -> bool:
        """
        Validate that input string is in proper list format.
        
        Args:
            input_string: String to validate
            
        Returns:
            True if format is valid, False otherwise
        """
        # Check for proper bracket structure
        if not (input_string.strip().startswith('[') and input_string.strip().endswith(']')):
            return False
        
        # Check for balanced brackets
        bracket_count = 0
        for char in input_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count < 0:
                    return False
        
        return bracket_count == 0
    
    @staticmethod
    def validate_number_format(number_string: str) -> bool:
        """
        Validate that a string represents a valid number.
        
        Args:
            number_string: String to validate
            
        Returns:
            True if valid number, False otherwise
        """
        try:
            float(number_string.strip())
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_comma_separation(input_string: str) -> bool:
        """
        Validate proper comma separation in list.
        
        Args:
            input_string: String to validate
            
        Returns:
            True if comma separation is valid, False otherwise
        """
        # Remove brackets
        content = input_string.strip()[1:-1]
        
        # Check for proper comma usage
        parts = content.split(',')
        
        # Each part should be a valid number
        for part in parts:
            if not InputValidator.validate_number_format(part):
                return False
        
        return True


def main():
    """
    Demonstrate utility functions.
    """
    print("Utility Functions Demonstration")
    print("=" * 40)
    
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
    
    # Test InputValidator
    print("\n2. Testing InputValidator:")
    validator = InputValidator()
    
    validation_tests = [
        "[1, 2, 3]",
        "[1, 2, abc]",
        "1, 2, 3",
        "[1, 2, 3, 4, 5]"
    ]
    
    for test_input in validation_tests:
        list_valid = validator.validate_list_format(test_input)
        print(f"  {test_input}: List format valid = {list_valid}")
    
    # Test extract_numbers_from_text
    print("\n3. Testing extract_numbers_from_text:")
    text_samples = [
        "The numbers are 5, 8, 12, 4, and 10",
        "calculate [1, 2, 3]",
        "Average of 100.5 and 200.7",
        "No numbers here"
    ]
    
    for text in text_samples:
        numbers = extract_numbers_from_text(text)
        print(f"  Text: '{text}' -> Numbers: {numbers}")


if __name__ == "__main__":
    main()

