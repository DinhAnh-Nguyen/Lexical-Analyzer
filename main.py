"""
Main entry point for the Lexical Analyzer project.

This module provides a unified interface to run different parts of the
lexical analyzer assignment.
"""

import sys
import argparse
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from lexical_analyzer import LexicalAnalyzer
from grammar import GrammarAnalyzer
from pseudocode import demonstrate_algorithm
from utils import main as utils_main
from config import get_project_info


def run_lexical_analyzer():
    """Run the lexical analyzer demonstration."""
    print("Running Lexical Analyzer")
    print("=" * 30)
    
    analyzer = LexicalAnalyzer()
    analyzer.main()


def run_grammar_analysis():
    """Run the grammar analysis demonstration."""
    print("Running Grammar Analysis")
    print("=" * 30)
    
    analyzer = GrammarAnalyzer()
    analyzer.main()


def run_pseudocode_demo():
    """Run the pseudo code demonstration."""
    print("Running Pseudo Code Demonstration")
    print("=" * 40)
    
    demonstrate_algorithm()


def run_utils_demo():
    """Run the utilities demonstration."""
    print("Running Utilities Demonstration")
    print("=" * 35)
    
    utils_main()


def run_tests():
    """Run all tests."""
    print("Running Tests")
    print("=" * 15)
    
    # Import and run tests
    sys.path.insert(0, str(Path(__file__).parent / "tests"))
    from test_lexical_analyzer import run_tests as run_lexical_tests
    
    run_lexical_tests()


def show_project_info():
    """Display project information."""
    project_info = get_project_info()
    
    print("Project Information")
    print("=" * 20)
    for key, value in project_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\nAvailable Components:")
    print("  1. Lexical Analyzer - Main tokenization functionality")
    print("  2. Grammar Analysis - BNF/EBNF grammar analysis")
    print("  3. Pseudo Code - Algorithm demonstration")
    print("  4. Utilities - Helper functions")
    print("  5. Tests - Unit tests and examples")
    print("  6. Project Info - This information")


def main():
    """Main entry point with command line interface."""
    parser = argparse.ArgumentParser(
        description="Lexical Analyzer for Average Calculation Problem",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Run interactive menu
  python main.py --lexical          # Run lexical analyzer
  python main.py --grammar          # Run grammar analysis
  python main.py --pseudocode       # Run pseudo code demo
  python main.py --utils            # Run utilities demo
  python main.py --tests            # Run all tests
  python main.py --info             # Show project information
        """
    )
    
    parser.add_argument(
        "--lexical",
        action="store_true",
        help="Run lexical analyzer demonstration"
    )
    parser.add_argument(
        "--grammar",
        action="store_true",
        help="Run grammar analysis demonstration"
    )
    parser.add_argument(
        "--pseudocode",
        action="store_true",
        help="Run pseudo code demonstration"
    )
    parser.add_argument(
        "--utils",
        action="store_true",
        help="Run utilities demonstration"
    )
    parser.add_argument(
        "--tests",
        action="store_true",
        help="Run all tests"
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show project information"
    )
    
    args = parser.parse_args()
    
    # If no arguments provided, show interactive menu
    if not any(vars(args).values()):
        show_interactive_menu()
    else:
        # Run specified components
        if args.lexical:
            run_lexical_analyzer()
        if args.grammar:
            run_grammar_analysis()
        if args.pseudocode:
            run_pseudocode_demo()
        if args.utils:
            run_utils_demo()
        if args.tests:
            run_tests()
        if args.info:
            show_project_info()


def show_interactive_menu():
    """Show interactive menu for user selection."""
    while True:
        print("\n" + "=" * 50)
        print("Lexical Analyzer for Average Calculation")
        print("=" * 50)
        print("Select an option:")
        print("1. Run Lexical Analyzer")
        print("2. Run Grammar Analysis")
        print("3. Run Pseudo Code Demonstration")
        print("4. Run Utilities Demonstration")
        print("5. Run Tests")
        print("6. Show Project Information")
        print("0. Exit")
        print("-" * 50)
        
        try:
            choice = input("Enter your choice (0-6): ").strip()
            
            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                run_lexical_analyzer()
            elif choice == "2":
                run_grammar_analysis()
            elif choice == "3":
                run_pseudocode_demo()
            elif choice == "4":
                run_utils_demo()
            elif choice == "5":
                run_tests()
            elif choice == "6":
                show_project_info()
            else:
                print("Invalid choice. Please enter a number between 0-6.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

