import unittest

def find_content_children(greed, cookies):
    greed.sort()
    cookies.sort()
   
    pass



class TestFindContentChildren(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_content_children([1, 2, 3], [1, 1]), 1)

    def test_all_children_satisfied(self):
        self.assertEqual(find_content_children([1, 2], [2, 3]), 2)

    def test_no_cookie_big_enough(self):
        self.assertEqual(find_content_children([5, 6, 7], [1, 2, 3]), 0)

    def test_empty_greed(self):
        self.assertEqual(find_content_children([], [1, 2, 3]), 0)

    def test_empty_cookies(self):
        self.assertEqual(find_content_children([1, 2, 3], []), 0)

    def test_exact_matches(self):
        self.assertEqual(find_content_children([1, 2, 3], [1, 2, 3]), 3)

    def test_more_cookies_than_children(self):
        self.assertEqual(find_content_children([2, 3], [1, 2, 3, 4]), 2)

    def test_more_children_than_cookies(self):
        self.assertEqual(find_content_children([1, 2, 3, 4], [1, 2]), 2)

if __name__ == '__main__':
    unittest.main()
