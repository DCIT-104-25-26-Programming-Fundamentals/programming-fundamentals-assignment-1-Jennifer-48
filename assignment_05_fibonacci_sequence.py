# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================

# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
def generate_fibonacci(n):
    """Generates and prints the first N terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return

    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    # Print terms separated by spaces on a single line
    print("Fibonacci sequence:", " ".join(str(num) for num in fib_sequence))


# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
def is_fibonacci_number(target):
    """Checks if a non-negative number belongs to the Fibonacci sequence."""
    if target < 0:
        return False

    a, b = 0, 1
    # Loop until the current term reaches or exceeds the target
    while a < target:
        a, b = b, a + b

    # If 'a' matches target, it is in the sequence
    return a == target


# -----------------------------------------------------------------------------
# MAIN PROGRAM DRIVER
# -----------------------------------------------------------------------------
def main():
    print("=== FIBONACCI SEQUENCE GENERATOR ===\n")

    # --- PART A DEMO ---
    print("--- PART A: Generate N Terms ---")
    try:
        n = int(input("How many terms? "))
        generate_fibonacci(n)
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")

    print("\n" + "-" * 40 + "\n")

    # --- PART B DEMO ---
    print("--- PART B: Fibonacci Membership Check ---")
    try:
        target = int(input("Enter a number to check: "))
        if target < 0:
            print(f"{target} is NOT a Fibonacci number.")
        elif is_fibonacci_number(target):
            print(f"{target} is a Fibonacci number.")
        else:
            print(f"{target} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()