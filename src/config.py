"""
Configuration file for the Lexical Analyzer project.

This module contains configuration settings and constants used throughout
the project.
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
TESTS_DIR = PROJECT_ROOT / "tests"
DOCS_DIR = PROJECT_ROOT / "docs"

# File paths
GRAMMAR_FILE = SRC_DIR / "grammar.py"
LEXICAL_ANALYZER_FILE = SRC_DIR / "lexical_analyzer.py"
PSEUDOCODE_FILE = SRC_DIR / "pseudocode.py"
UTILS_FILE = SRC_DIR / "utils.py"

# Test configuration
TEST_INPUTS = [
    "calculate [5, 8, 12, 4, 10]",
    "[1, 2, 3, 4, 5]",
    "CALCULATE [100, 200, 300]",
    "[0.5, 1.5, 2.5]",
    "[42]",
]

ERROR_INPUTS = [
    "calculate [5, 8, abc, 4, 10]",
    "[1, 2, 3",
    "calc [1, 2, 3]",
    "1.2.3",
    "[1, 2, 3,]",
]

# Token patterns for lexical analyzer
TOKEN_PATTERNS = {
    "NUMBER": r'\d+(\.\d+)?',
    "COMMA": r',',
    "LEFT_BRACKET": r'\[',
    "RIGHT_BRACKET": r'\]',
    "AVERAGE_KEYWORD": r'average|AVERAGE',
    "CALCULATE_KEYWORD": r'calculate|CALCULATE',
    "WHITESPACE": r'\s+',
}

# Grammar definitions
BNF_GRAMMAR_DEFINITION = """
<expression> ::= <average_calculation>
<average_calculation> ::= <calculate_keyword> <number_list>
<calculate_keyword> ::= "calculate" | "CALCULATE"
<number_list> ::= <left_bracket> <numbers> <right_bracket>
<left_bracket> ::= "["
<right_bracket> ::= "]"
<numbers> ::= <number> | <number> <comma> <numbers>
<number> ::= <digit> | <digit> <number>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<comma> ::= ","
"""

EBNF_GRAMMAR_DEFINITION = """
expression = average_calculation ;

average_calculation = calculate_keyword , number_list ;

calculate_keyword = "calculate" | "CALCULATE" ;

number_list = "[" , number , { "," , number } , "]" ;

number = digit , { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
"""

# Error messages
ERROR_MESSAGES = {
    "INVALID_INPUT": "Invalid input format. Please provide a valid list of numbers.",
    "EMPTY_LIST": "Cannot calculate average of an empty list.",
    "NON_NUMERIC": "All values must be numeric.",
    "SYNTAX_ERROR": "Syntax error in input.",
    "PARSING_ERROR": "Error parsing input.",
    "INVALID_CHARACTER": "Invalid character found in input.",
    "MISSING_BRACKET": "Missing opening or closing bracket.",
    "INVALID_NUMBER_FORMAT": "Invalid number format.",
}

# Display settings
DISPLAY_SETTINGS = {
    "DECIMAL_PLACES": 2,
    "MAX_NUMBERS_DISPLAY": 10,
    "SEPARATOR": ", ",
    "BRACKET_LEFT": "[",
    "BRACKET_RIGHT": "]",
}

# Logging configuration
LOGGING_CONFIG = {
    "LEVEL": "INFO",
    "FORMAT": "[%(asctime)s] %(levelname)s: %(message)s",
    "DATE_FORMAT": "%Y-%m-%d %H:%M:%S",
}

# Test configuration
TEST_CONFIG = {
    "VERBOSE": True,
    "STOP_ON_FIRST_FAILURE": False,
    "INCLUDE_ERROR_TESTS": True,
    "GENERATE_REPORTS": True,
}

def get_project_info():
    """
    Get project information.
    
    Returns:
        Dictionary containing project information
    """
    return {
        "name": "Lexical Analyzer for Average Calculation",
        "version": "1.0.0",
        "description": "A lexical analyzer implementation for processing average calculation input",
        "author": "Student",
        "course": "Advanced Programming Language Concepts",
        "assignment": "Lexical Analyzer - Part B & C",
    }

def get_grammar_info():
    """
    Get grammar information.
    
    Returns:
        Dictionary containing grammar information
    """
    return {
        "bnf_grammar": BNF_GRAMMAR_DEFINITION,
        "ebnf_grammar": EBNF_GRAMMAR_DEFINITION,
        "ambiguities": [
            "Recursive definition of numbers could lead to ambiguity",
            "Multiple interpretations possible for nested structures",
            "Left-associative vs right-associative parsing issues"
        ],
        "benefits_of_ebnf": [
            "More readable and maintainable",
            "Eliminates ambiguity through explicit repetition operators",
            "Easier to implement in parser generators",
            "Clearer separation of concerns"
        ]
    }

def validate_config():
    """
    Validate configuration settings.
    
    Returns:
        True if configuration is valid, False otherwise
    """
    # Check if required directories exist
    required_dirs = [SRC_DIR, TESTS_DIR]
    for directory in required_dirs:
        if not directory.exists():
            print(f"Warning: Directory {directory} does not exist")
            return False
    
    # Check if required files exist
    required_files = [GRAMMAR_FILE, LEXICAL_ANALYZER_FILE]
    for file_path in required_files:
        if not file_path.exists():
            print(f"Warning: File {file_path} does not exist")
            return False
    
    return True

if __name__ == "__main__":
    print("Configuration Information")
    print("=" * 30)
    
    # Display project info
    project_info = get_project_info()
    print("\nProject Information:")
    for key, value in project_info.items():
        print(f"  {key}: {value}")
    
    # Display grammar info
    grammar_info = get_grammar_info()
    print(f"\nGrammar Information:")
    print(f"  BNF Grammar: {len(grammar_info['bnf_grammar'])} characters")
    print(f"  EBNF Grammar: {len(grammar_info['ebnf_grammar'])} characters")
    print(f"  Identified Ambiguities: {len(grammar_info['ambiguities'])}")
    print(f"  EBNF Benefits: {len(grammar_info['benefits_of_ebnf'])}")
    
    # Validate configuration
    print(f"\nConfiguration Validation:")
    is_valid = validate_config()
    print(f"  Configuration valid: {is_valid}")
    
    # Display test configuration
    print(f"\nTest Configuration:")
    for key, value in TEST_CONFIG.items():
        print(f"  {key}: {value}")
    
    # Display display settings
    print(f"\nDisplay Settings:")
    for key, value in DISPLAY_SETTINGS.items():
        print(f"  {key}: {value}")

