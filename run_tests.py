"""
Test runner script for the Lexical Analyzer project.

This script provides an easy way to run all tests and demonstrations.
"""

import sys
import unittest
from pathlib import Path

# Add project directories to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root / "tests"))


def run_all_tests():
    """Run all test suites."""
    print("Running All Tests")
    print("=" * 20)
    
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = str(project_root / "tests")
    suite = loader.discover(start_dir, pattern="test_*.py")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\nTest Summary:")
    print(f"  Tests run: {result.testsRun}")
    print(f"  Failures: {len(result.failures)}")
    print(f"  Errors: {len(result.errors)}")
    print(f"  Skipped: {len(result.skipped)}")
    
    if result.failures:
        print(f"\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print(f"\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    return result.wasSuccessful()


def run_individual_tests():
    """Run individual test modules."""
    print("Running Individual Test Modules")
    print("=" * 35)
    
    test_modules = [
        "test_lexical_analyzer",
    ]
    
    for module_name in test_modules:
        print(f"\nRunning {module_name}:")
        try:
            module = __import__(module_name)
            if hasattr(module, 'run_tests'):
                module.run_tests()
            else:
                print(f"  No run_tests function found in {module_name}")
        except ImportError as e:
            print(f"  Error importing {module_name}: {e}")
        except Exception as e:
            print(f"  Error running {module_name}: {e}")


def run_demonstrations():
    """Run demonstration modules."""
    print("Running Demonstrations")
    print("=" * 25)
    
    demo_modules = [
        ("lexical_analyzer", "Lexical Analyzer"),
        ("grammar", "Grammar Analysis"),
        ("pseudocode", "Pseudo Code"),
        ("utils", "Utilities"),
    ]
    
    for module_name, display_name in demo_modules:
        print(f"\n{display_name} Demonstration:")
        try:
            module = __import__(module_name)
            if hasattr(module, 'main'):
                module.main()
            else:
                print(f"  No main function found in {module_name}")
        except ImportError as e:
            print(f"  Error importing {module_name}: {e}")
        except Exception as e:
            print(f"  Error running {module_name}: {e}")


def main():
    """Main test runner function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test runner for Lexical Analyzer project")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all tests"
    )
    parser.add_argument(
        "--individual",
        action="store_true",
        help="Run individual test modules"
    )
    parser.add_argument(
        "--demos",
        action="store_true",
        help="Run demonstration modules"
    )
    parser.add_argument(
        "--everything",
        action="store_true",
        help="Run everything (tests + demos)"
    )
    
    args = parser.parse_args()
    
    if args.everything or (not any(vars(args).values())):
        # Run everything by default
        print("Running Everything")
        print("=" * 20)
        
        # Run tests
        success = run_all_tests()
        
        # Run demonstrations
        run_demonstrations()
        
        if success:
            print("\n✓ All tests passed!")
        else:
            print("\n✗ Some tests failed!")
            
    else:
        if args.all:
            run_all_tests()
        if args.individual:
            run_individual_tests()
        if args.demos:
            run_demonstrations()


if __name__ == "__main__":
    main()

