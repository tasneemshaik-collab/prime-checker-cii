import unittest
from prime import is_prime

class TestPrimeFunction(unittest.TestCase):

    def test_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(97))

    def test_non_primes(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(100))

if __name__ == '__main__':
    unittest.main()
