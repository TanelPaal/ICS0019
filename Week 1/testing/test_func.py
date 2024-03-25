# Executing: python -m unittest
import pytest
import unittest
from calculator import calculate as c


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(c(3, 4), 7)
        self.assertNotEqual(c(3, 5), 7)


if __name__ == '__main__':
    unittest.main()
