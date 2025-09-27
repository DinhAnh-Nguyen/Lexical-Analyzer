"""
Pseudo code for the Average Calculation Problem

This module contains the pseudo code implementation as required in Part B
of the assignment, with descriptive variable names and comments.
"""

def calculate_average_pseudocode():
    """
    Pseudo code for finding the average of a set of numbers.
    
    This pseudo code demonstrates the algorithm for calculating the average
    with descriptive variable names and detailed comments.
    """
    
    # Pseudo code for Average Calculation Algorithm
    
    """
    ALGORITHM: Calculate Average of Numbers
    
    INPUT: A list of numbers (number_list)
    OUTPUT: The average of all numbers (average_value)
    
    BEGIN
        1. Initialize variables:
           - number_list = [5, 8, 12, 4, 10]  // Input list of numbers
           - sum_of_numbers = 0               // Running sum of all numbers
           - count_of_numbers = 0            // Count of numbers in the list
           - average_value = 0               // Final average result
           - current_number = 0              // Current number being processed
           - index = 0                       // Index for iteration
        
        2. Validate input:
           IF number_list is empty THEN
               DISPLAY "Error: Cannot calculate average of empty list"
               RETURN error
           END IF
        
        3. Calculate sum and count:
           FOR each current_number in number_list DO
               sum_of_numbers = sum_of_numbers + current_number
               count_of_numbers = count_of_numbers + 1
           END FOR
        
        4. Calculate average:
           IF count_of_numbers > 0 THEN
               average_value = sum_of_numbers / count_of_numbers
           ELSE
               DISPLAY "Error: Division by zero"
               RETURN error
           END IF
        
        5. Display results:
           DISPLAY "Numbers: " + number_list
           DISPLAY "Sum: " + sum_of_numbers
           DISPLAY "Count: " + count_of_numbers
           DISPLAY "Average: " + average_value
        
        6. Return result:
           RETURN average_value
    
    END
    """


def calculate_average_implementation(numbers):
    """
    Python implementation of the average calculation algorithm.
    
    Args:
        numbers: List of numbers to calculate average for
        
    Returns:
        float: The average of the numbers
        
    Raises:
        ValueError: If the input list is empty or contains invalid values
    """
    
    # Step 1: Initialize variables
    sum_of_numbers = 0
    count_of_numbers = 0
    average_value = 0.0
    
    # Step 2: Validate input
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    # Step 3: Calculate sum and count
    for current_number in numbers:
        try:
            # Convert to float to handle both integers and floats
            numeric_value = float(current_number)
            sum_of_numbers += numeric_value
            count_of_numbers += 1
        except (ValueError, TypeError):
            raise ValueError(f"Invalid number: {current_number}")
    
    # Step 4: Calculate average
    if count_of_numbers > 0:
        average_value = sum_of_numbers / count_of_numbers
    else:
        raise ValueError("Division by zero - no valid numbers found")
    
    # Step 5: Display results (optional - for demonstration)
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum_of_numbers}")
    print(f"Count: {count_of_numbers}")
    print(f"Average: {average_value:.2f}")
    
    # Step 6: Return result
    return average_value


def demonstrate_algorithm():
    """
    Demonstrate the average calculation algorithm with examples.
    """
    
    print("Average Calculation Algorithm Demonstration")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        [5, 8, 12, 4, 10],  # Original example
        [1, 2, 3, 4, 5],    # Simple case
        [100, 200, 300],    # Large numbers
        [0.5, 1.5, 2.5],    # Decimal numbers
        [42],               # Single number
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],  # Many numbers
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        try:
            result = calculate_average_implementation(test_case)
            print(f"✓ Successfully calculated average: {result:.2f}")
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    # Test error cases
    print(f"\nError Handling Tests:")
    error_cases = [
        [],  # Empty list
        ["abc", "def"],  # Non-numeric values
        [1, 2, "three", 4],  # Mixed valid and invalid
    ]
    
    for i, error_case in enumerate(error_cases, 1):
        print(f"\nError Test {i}: {error_case}")
        try:
            result = calculate_average_implementation(error_case)
            print(f"✓ Unexpectedly succeeded: {result:.2f}")
        except ValueError as e:
            print(f"✗ Expected error: {e}")


if __name__ == "__main__":
    demonstrate_algorithm()

