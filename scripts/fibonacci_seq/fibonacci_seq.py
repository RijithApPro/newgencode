def fibonacci_recursive(n):
    """
    Generates the Fibonacci sequence up to n terms using recursion.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, starting from 0 and 1.

    Args:
        n (int): The number of terms to generate in the sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to n terms.
    """
    def fib_helper(k):
        # Base cases: return k if k is 0 or 1
        if k == 0:
            return 0
        elif k == 1:
            return 1
        else:
            # Recursive case: sum of the two preceding numbers
            return fib_helper(k - 1) + fib_helper(k - 2)

    sequence = []  # Initialize an empty list to store the sequence
    for i in range(n):
        sequence.append(fib_helper(i))  # Append the ith Fibonacci number
    return sequence

# Example usage:
print(fibonacci_recursive(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]