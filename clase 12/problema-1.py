import unittest
from collections import defaultdict

# n número total de perfiles. 
# m número total de amistades
def count_double_profiles(n, m, friendships):

    pass


class TestDoubleProfiles(unittest.TestCase):

    def test_no_friendships(self):
        self.assertEqual(count_double_profiles(5, 0, []), 0)

    def test_simple_case(self):
        self.assertEqual(count_double_profiles(4, 2, [(1 ,2), (3, 4)]), 0)

    def test_all_connected_to_one(self):
        friendships = [(1, 2), (1, 3), (1, 4), (1, 5)]
        self.assertEqual(count_double_profiles(5, 4, friendships), 3)

    def test_unique_friendsets(self):
        friendships = [(1, 2), (2, 3), (3, 4), (4, 5)]
        self.assertEqual(count_double_profiles(5, 4, friendships), 0)

    def test_all_friends(self):
        n = 4
        friendships = [(1, 2), (1, 3), (1, 4),
                       (2, 3), (2, 4),
                       (3, 4)]
        self.assertEqual(count_double_profiles(n, len(friendships), friendships), 0)


if __name__ == '__main__':
    unittest.main()
