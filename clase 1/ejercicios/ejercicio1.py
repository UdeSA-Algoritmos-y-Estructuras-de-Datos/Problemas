def sort_string_array(arr):
    """
    Sorts an array of strings in alphabetical order.
    The algorithm should sort the array in-place, meaning no additional arrays should be created.
    
    :param arr: List[str] - List of strings to be sorted
    :return: None - The array is modified in-place
    """
    # Implement the sorting algorithm here
    pass
            

# Test Cases
def test_sort_string_array():
    test_cases = [
        (["pear", "apple", "banana"], ["apple", "banana", "pear"]),
        (["fox", "cat", "elephant", "dolphin"], ["cat", "dolphin", "elephant", "fox"]),
        (["python", "java", "c++", "ruby"], ["c++", "java", "python", "ruby"]),
        (["sun", "moon", "star"], ["moon", "star", "sun"]),
        (["a", "b", "c"], ["a", "b", "c"]),
        ([], []),
        (["one"], ["one"]),
        (["ccc", "aaa", "bbb"], ["aaa", "bbb", "ccc"]),
    ]
    
    for i, (input_array, expected) in enumerate(test_cases):
        sort_string_array(input_array)
        assert input_array == expected, f"FAILED on case {i + 1}: expected {expected}, but got {input_array}"
    print("All tests PASSED.")

# Run Tests
if __name__ == "__main__":
    test_sort_string_array()
