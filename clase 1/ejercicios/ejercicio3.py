# Find the First Occurrence of an Element in an Array

## Problem Description

def find_first_occurrence(arr, element):
    """
    Finds the position of the first occurrence of an element in an array of strings.
    
    :param arr: List[str] - The array of strings to search through
    :param element: str - The element to find in the array
    :return: int - The position of the first occurrence, or -1 if not found
    """
    # Implement the algorithm to find the first occurrence here
    pass

# Test Cases
def test_find_first_occurrence():
    test_cases = [
        (["apple", "banana", "cherry"], "banana", 1),
        (["dog", "cat", "dog", "bird"], "dog", 0),
        (["red", "blue", "green", "blue"], "blue", 1),
        (["one", "two", "three"], "four", -1),
        ([], "anything", -1),
        (["a", "b", "c"], "c", 2),
    ]
    
    for i, (input_array, element, expected) in enumerate(test_cases):
        result = find_first_occurrence(input_array, element)
        assert result == expected, f"FAILED on case {i + 1}: expected {expected}, but got {result}"
    print("All tests PASSED.")

# Run Tests
if __name__ == "__main__":
    test_find_first_occurrence()
