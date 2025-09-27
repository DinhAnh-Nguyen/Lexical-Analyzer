# Lexical Analyzer for Average Calculation Problem

A comprehensive Python implementation of a lexical analyzer for processing average calculation input, developed as part of the Advanced Programming Language Concepts course assignment.

## Project Overview

This project implements a lexical analyzer that processes input related to calculating the average of a set of numbers. It includes both traditional Backus-Naur Form (BNF) and Extended Backus-Naur Form (EBNF) grammar definitions, along with a complete lexical analyzer implementation.

## Assignment Requirements

### Part B: Syntax Description
- **Problem Statement**: Finding the average of a set of numbers
- **Pseudo Code**: Algorithm implementation with descriptive variable names
- **BNF Grammar**: Traditional grammar definition
- **Parse Tree Analysis**: Visualization and ambiguity detection
- **EBNF Grammar**: Enhanced grammar with improved readability
- **Ambiguity Resolution**: Comparison between BNF and EBNF approaches

### Part C: Lexical Analyzer
- **Input Processing**: Accept user inputs with error handling
- **Tokenization**: Convert input strings into tokens
- **Error Handling**: Manage incorrect inputs with appropriate messages
- **Testing**: Comprehensive test cases including edge cases

## Project Structure

```
Lexical-Analyzer/
├── src/                          # Source code directory
│   ├── lexical_analyzer.py      # Main lexical analyzer implementation
│   ├── grammar.py               # BNF and EBNF grammar definitions
│   ├── pseudocode.py            # Pseudo code and algorithm implementation
│   ├── utils.py                 # Utility functions and helpers
│   └── config.py                # Configuration settings
├── tests/                       # Test directory
│   └── test_lexical_analyzer.py # Unit tests and examples
├── main.py                      # Main entry point
├── run_tests.py                 # Test runner script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Features

### Lexical Analyzer
- **Token Recognition**: Identifies numbers, brackets, commas, and keywords
- **Input Validation**: Validates input format and handles errors gracefully
- **Error Messages**: Provides clear, descriptive error messages
- **Interactive Mode**: User-friendly command-line interface

### Grammar Analysis
- **BNF Grammar**: Traditional grammar definition with potential ambiguities
- **EBNF Grammar**: Enhanced grammar with improved readability
- **Parse Tree Generation**: Visual representation of syntax structure
- **Ambiguity Analysis**: Identifies and resolves grammar ambiguities

### Algorithm Implementation
- **Pseudo Code**: Step-by-step algorithm with descriptive variable names
- **Python Implementation**: Working implementation of the average calculation
- **Error Handling**: Comprehensive error handling for edge cases
- **Testing**: Multiple test cases and examples

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Setup Instructions

1. **Clone or Download** the project to your local machine
2. **Navigate** to the project directory:
   ```bash
   cd Lexical-Analyzer
   ```
3. **Verify Python Installation**:
   ```bash
   python --version
   ```

## Usage

### Running the Main Program

#### Interactive Mode (Recommended)
```bash
python main.py
```
This will show an interactive menu where you can select different components to run.

#### Command Line Options
```bash
# Run lexical analyzer
python main.py --lexical

# Run grammar analysis
python main.py --grammar

# Run pseudo code demonstration
python main.py --pseudocode

# Run utilities demonstration
python main.py --utils

# Run all tests
python main.py --tests

# Show project information
python main.py --info
```

### Running Individual Components

#### Lexical Analyzer
```bash
python src/lexical_analyzer.py
```

#### Grammar Analysis
```bash
python src/grammar.py
```

#### Pseudo Code Demonstration
```bash
python src/pseudocode.py
```

#### Utilities
```bash
python src/utils.py
```

### Running Tests

#### Run All Tests
```bash
python run_tests.py
```

#### Run Specific Test Components
```bash
python run_tests.py --all          # Run all tests
python run_tests.py --individual   # Run individual test modules
python run_tests.py --demos        # Run demonstration modules
python run_tests.py --everything   # Run everything
```

## Input Format

The lexical analyzer accepts input in the following formats:

### Valid Input Examples
```
calculate [5, 8, 12, 4, 10]
[1, 2, 3, 4, 5]
CALCULATE [100, 200, 300]
[0.5, 1.5, 2.5]
[42]
```

### Invalid Input Examples
```
calculate [5, 8, abc, 4, 10]    # Invalid character
[1, 2, 3                       # Missing closing bracket
calc [1, 2, 3]                 # Invalid keyword
1.2.3                          # Invalid number format
[1, 2, 3,]                     # Trailing comma
```

## Grammar Definitions

### BNF Grammar
```
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
```

### EBNF Grammar
```
expression = average_calculation ;

average_calculation = calculate_keyword , number_list ;

calculate_keyword = "calculate" | "CALCULATE" ;

number_list = "[" , number , { "," , number } , "]" ;

number = digit , { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

## Testing

The project includes comprehensive test cases covering:

### Unit Tests
- Valid input tokenization
- Invalid input handling
- Edge cases and boundary conditions
- Whitespace handling
- Number format validation

### Integration Tests
- End-to-end functionality
- Error handling scenarios
- User interaction flows

### Test Cases
- **Valid Inputs**: Various formats of valid number lists
- **Invalid Inputs**: Malformed input with appropriate error messages
- **Edge Cases**: Empty lists, single numbers, large numbers
- **Error Scenarios**: Invalid characters, missing brackets, syntax errors

## Error Handling

The lexical analyzer provides comprehensive error handling:

### Error Types
- **Invalid Input Format**: Malformed input strings
- **Invalid Characters**: Non-numeric characters in number lists
- **Syntax Errors**: Missing brackets, invalid separators
- **Empty Input**: Handling of empty or whitespace-only input

### Error Messages
- Clear, descriptive error messages
- Position information for syntax errors
- Suggestions for correcting common mistakes

## Development Notes

### Code Organization
- **Modular Design**: Separate modules for different functionalities
- **Clear Separation**: Grammar definitions, lexical analysis, and utilities
- **Comprehensive Comments**: Detailed documentation throughout
- **Type Hints**: Python type annotations for better code clarity

### Extensibility
- **Configurable Patterns**: Easy to modify token patterns
- **Pluggable Components**: Modular design allows easy extension
- **Test Framework**: Comprehensive testing infrastructure

## Assignment Completion Checklist

### Part B: Syntax Description
- [x] Problem statement analysis
- [x] Pseudo code development
- [x] BNF grammar definition
- [x] Parse tree construction
- [x] Ambiguity analysis
- [x] EBNF grammar definition
- [x] Ambiguity resolution
- [x] Parse tree comparison

### Part C: Lexical Analyzer
- [x] Lexical analyzer implementation
- [x] User input handling
- [x] Error handling and messages
- [x] Comprehensive testing
- [x] Edge case handling
- [x] Code documentation

## Future Enhancements

Potential improvements for the project:

1. **Parser Implementation**: Complete parser based on the grammar
2. **AST Generation**: Abstract Syntax Tree construction
3. **Code Generation**: Generate executable code from parsed input
4. **GUI Interface**: Graphical user interface for better user experience
5. **Performance Optimization**: Optimize for large input processing
6. **Additional Grammar Support**: Support for more complex expressions

## Contributing

This is an academic project, but suggestions for improvements are welcome:

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is developed for educational purposes as part of the Advanced Programming Language Concepts course.

## Contact

For questions or issues related to this project, please contact the course instructor or refer to the course materials.

---

**Note**: This project is designed to be a learning tool for understanding lexical analysis, grammar definitions, and parser implementation. It provides a solid foundation for further study in compiler design and language processing.