import unittest

def max_integer(list=[]):
    if not list:
        return None
    return max(list)

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_max_integer_exceptions(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

if __name__ == '__main__':
    unittest.main()

