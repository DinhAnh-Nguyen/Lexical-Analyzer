"""
Setup script for the Lexical Analyzer project.

This script helps initialize the project and verify that everything is working correctly.
"""

import sys
import os
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required.")
        print(f"   Current version: {sys.version}")
        return False
    else:
        print(f"✅ Python version: {sys.version}")
        return True


def check_project_structure():
    """Check if project structure is correct."""
    print("\nChecking project structure...")
    
    required_dirs = ["src", "tests"]
    required_files = [
        "src/lexical_analyzer.py",
        "src/grammar.py",
        "src/pseudocode.py",
        "src/utils.py",
        "src/config.py",
        "tests/test_lexical_analyzer.py",
        "main.py",
        "run_tests.py",
        "requirements.txt",
        "README.md"
    ]
    
    all_good = True
    
    # Check directories
    for directory in required_dirs:
        if Path(directory).exists():
            print(f"✅ Directory exists: {directory}")
        else:
            print(f"❌ Missing directory: {directory}")
            all_good = False
    
    # Check files
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ File exists: {file_path}")
        else:
            print(f"❌ Missing file: {file_path}")
            all_good = False
    
    return all_good


def test_imports():
    """Test if all modules can be imported correctly."""
    print("\nTesting imports...")
    
    # Add src to Python path
    sys.path.insert(0, str(Path("src")))
    
    modules_to_test = [
        "lexical_analyzer",
        "grammar",
        "pseudocode",
        "utils",
        "config"
    ]
    
    all_good = True
    
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✅ Successfully imported: {module_name}")
        except ImportError as e:
            print(f"❌ Failed to import {module_name}: {e}")
            all_good = False
    
    return all_good


def run_basic_tests():
    """Run basic functionality tests."""
    print("\nRunning basic tests...")
    
    try:
        # Test lexical analyzer
        from lexical_analyzer import LexicalAnalyzer
        analyzer = LexicalAnalyzer()
        
        # Test tokenization
        tokens = analyzer.tokenize("[1, 2, 3]")
        if len(tokens) > 0:
            print("✅ Lexical analyzer tokenization works")
        else:
            print("❌ Lexical analyzer tokenization failed")
            return False
        
        # Test grammar analysis
        from grammar import GrammarAnalyzer
        grammar_analyzer = GrammarAnalyzer()
        ambiguities = grammar_analyzer.analyze_ambiguity()
        if ambiguities:
            print("✅ Grammar analysis works")
        else:
            print("❌ Grammar analysis failed")
            return False
        
        # Test average calculation
        from pseudocode import calculate_average_implementation
        result = calculate_average_implementation([1, 2, 3, 4, 5])
        if result == 3.0:
            print("✅ Average calculation works")
        else:
            print("❌ Average calculation failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Basic tests failed: {e}")
        return False


def show_next_steps():
    """Show next steps for the user."""
    print("\n" + "=" * 50)
    print("Next Steps:")
    print("=" * 50)
    print("1. Run the main program:")
    print("   python main.py")
    print()
    print("2. Run the example demonstration:")
    print("   python example_usage.py")
    print()
    print("3. Run all tests:")
    print("   python run_tests.py")
    print()
    print("4. Explore individual components:")
    print("   python src/lexical_analyzer.py")
    print("   python src/grammar.py")
    print("   python src/pseudocode.py")
    print("   python src/utils.py")
    print()
    print("5. Read the README.md for detailed documentation")
    print()
    print("6. Start implementing your own enhancements!")


def main():
    """Main setup function."""
    print("Lexical Analyzer Project Setup")
    print("=" * 40)
    print("This script will verify that your project is set up correctly.")
    print()
    
    # Run all checks
    checks = [
        check_python_version(),
        check_project_structure(),
        test_imports(),
        run_basic_tests()
    ]
    
    # Summary
    print("\n" + "=" * 40)
    print("Setup Summary:")
    print("=" * 40)
    
    if all(checks):
        print("✅ All checks passed! Your project is ready to use.")
        show_next_steps()
    else:
        print("❌ Some checks failed. Please review the errors above.")
        print("Make sure all files are present and Python version is compatible.")


if __name__ == "__main__":
    main()

