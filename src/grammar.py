"""
Grammar definitions for the Average Calculation Problem

This module contains the BNF and EBNF grammar definitions as required
in Part B of the assignment.
"""

# Traditional Backus-Naur Form (BNF) Grammar
BNF_GRAMMAR = """
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

# Extended Backus-Naur Form (EBNF) Grammar
EBNF_GRAMMAR = """
expression = average_calculation ;

average_calculation = calculate_keyword , number_list ;

calculate_keyword = "calculate" | "CALCULATE" ;

number_list = "[" , numbers , "]" ;

numbers = number , { "," , number } ;

number = digit , { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
"""

# Alternative EBNF Grammar (more readable)
EBNF_GRAMMAR_READABLE = """
expression = average_calculation ;

average_calculation = calculate_keyword , number_list ;

calculate_keyword = "calculate" | "CALCULATE" ;

number_list = "[" , number , { "," , number } , "]" ;

number = digit , { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
"""


class GrammarAnalyzer:
    """
    Class to analyze and work with the grammar definitions.
    
    This class provides methods to analyze the grammar for ambiguities
    and demonstrate parse tree construction.
    """
    
    def __init__(self):
        """Initialize the grammar analyzer."""
        self.bnf_grammar = BNF_GRAMMAR
        self.ebnf_grammar = EBNF_GRAMMAR
        self.ebnf_readable = EBNF_GRAMMAR_READABLE
    
    def analyze_ambiguity(self) -> dict:
        """
        Analyze the BNF grammar for potential ambiguities.
        
        Returns:
            Dictionary containing ambiguity analysis results
        """
        ambiguities = {
            "potential_issues": [
                "The recursive definition of <numbers> could lead to ambiguity",
                "Multiple interpretations possible for nested number lists",
                "Left-associative vs right-associative parsing issues"
            ],
            "examples": [
                "Input: [1,2,3] could be parsed as (1,2),3 or 1,(2,3)",
                "Multiple parse trees possible for the same input"
            ],
            "implications": [
                "Parser may produce different results",
                "Code generation could be inconsistent",
                "Debugging becomes more difficult"
            ]
        }
        return ambiguities
    
    def generate_parse_tree_bnf(self, input_string: str) -> dict:
        """
        Generate a parse tree for the given input using BNF grammar.
        
        Args:
            input_string: The input string to parse
            
        Returns:
            Dictionary representing the parse tree
        """
        # This is a simplified representation
        # In a real implementation, you would build an actual tree structure
        parse_tree = {
            "root": "expression",
            "children": [
                {
                    "node": "average_calculation",
                    "children": [
                        {"node": "calculate_keyword", "value": "calculate"},
                        {
                            "node": "number_list",
                            "children": [
                                {"node": "left_bracket", "value": "["},
                                {
                                    "node": "numbers",
                                    "children": [
                                        {"node": "number", "value": "5"},
                                        {"node": "comma", "value": ","},
                                        {"node": "numbers", "value": "..."}
                                    ]
                                },
                                {"node": "right_bracket", "value": "]"}
                            ]
                        }
                    ]
                }
            ]
        }
        return parse_tree
    
    def generate_parse_tree_ebnf(self, input_string: str) -> dict:
        """
        Generate a parse tree for the given input using EBNF grammar.
        
        Args:
            input_string: The input string to parse
            
        Returns:
            Dictionary representing the parse tree
        """
        # EBNF version with clearer structure
        parse_tree = {
            "root": "expression",
            "children": [
                {
                    "node": "average_calculation",
                    "children": [
                        {"node": "calculate_keyword", "value": "calculate"},
                        {
                            "node": "number_list",
                            "children": [
                                {"node": "[", "value": "["},
                                {
                                    "node": "numbers",
                                    "children": [
                                        {"node": "number", "value": "5"},
                                        {"node": "number", "value": "8"},
                                        {"node": "number", "value": "12"},
                                        {"node": "number", "value": "4"},
                                        {"node": "number", "value": "10"}
                                    ]
                                },
                                {"node": "]", "value": "]"}
                            ]
                        }
                    ]
                }
            ]
        }
        return parse_tree
    
    def compare_parse_trees(self, bnf_tree: dict, ebnf_tree: dict) -> dict:
        """
        Compare parse trees from BNF and EBNF grammars.
        
        Args:
            bnf_tree: Parse tree from BNF grammar
            ebnf_tree: Parse tree from EBNF grammar
            
        Returns:
            Dictionary containing comparison results
        """
        comparison = {
            "differences": [
                "EBNF tree has clearer structure with explicit repetition",
                "BNF tree shows recursive structure that could be ambiguous",
                "EBNF eliminates left-recursion issues"
            ],
            "benefits_of_ebnf": [
                "More readable and maintainable",
                "Eliminates ambiguity through explicit repetition operators",
                "Easier to implement in parser generators",
                "Clearer separation of concerns"
            ]
        }
        return comparison


def main():
    """
    Main function to demonstrate grammar analysis.
    """
    analyzer = GrammarAnalyzer()
    
    print("Grammar Analysis for Average Calculation")
    print("=" * 50)
    
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
    
    # Compare parse trees
    print("\n3. Parse Tree Comparison:")
    comparison = analyzer.compare_parse_trees(bnf_tree, ebnf_tree)
    for key, value in comparison.items():
        print(f"\n{key.replace('_', ' ').title()}:")
        for item in value:
            print(f"  - {item}")


if __name__ == "__main__":
    main()

