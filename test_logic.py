import unittest
from finance import savings, interest

class TestFinance(unittest.TestCase):

    def test_savings(self):
        self.assertEqual(savings(100, 5), 500)

    def test_interest(self):
        self.assertEqual(interest(1000, 10), 100)

if __name__ == "__main__":
    unittest.main()