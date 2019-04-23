import unittest
from decimal_to_hexa import decimal_to_hexadecimal


class test_decimal_to_hexadecimal_1(unittest.TestCase):
    def test_factorial_1(self):
        result = decimal_to_hexadecimal(17)
        self.assertEqual(result, '011')

if __name__ == '__main__':
    unittest.main()
   

