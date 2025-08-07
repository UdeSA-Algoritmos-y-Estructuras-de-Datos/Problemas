import heapq

def find_top_k(arr, k):
    # TODO
    pass

# TESTS
def run_tests():
    arr1 = [5, 2, 1, 7, 5, 3]
    k1 = 3
    print("Test 1")
    print("Top", k1, "elements:", find_top_k(arr1, k1))
    print("Expected Output: [7, 5, 5]\n")

    arr2 = [10, 20, 30, 40, 50]
    k2 = 2
    print("Test 2")
    print("Top", k2, "elements:", find_top_k(arr2, k2))
    print("Expected Output: [50, 40]\n")

    arr3 = [1, 3, 3, 6, 7, 8, 9]
    k3 = 4
    print("Test 3")
    print("Top", k3, "elements:", find_top_k(arr3, k3))
    print("Expected Output: [9, 8, 7, 6]\n")


if __name__ == "__main__":
    run_tests()
