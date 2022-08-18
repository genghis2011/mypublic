import unittest
from IsAnagram import IsAnagram


class AnagramTestCase(unittest.TestCase):


    def test_function1(self):
        result = IsAnagram("anagram", "nagaram")
        self.assertEqual(result, True)

    def test_function2(self):
        result = IsAnagram("rat", "car")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()