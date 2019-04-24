import unittest
from interfaz import interfaz


class test_hexa_interfaz_1(unittest.TestCase):
    def test_factorial_1(self):
        result = interfaz(17)
        self.assertEqual(result, '011')

class test_hexa_interfaz_2(unittest.TestCase):
    def test_factorial_1(self):
        result = interfaz(-17)
        self.assertEqual(result, 'Ingrese un  numero positivo')

class test_hexa_interfaz_3(unittest.TestCase):
    def test_factorial_1(self):
        result = interfaz('afasf')
        self.assertEqual(result, 'Ingrese un numero')

class test_hexa_interfaz_4(unittest.TestCase):
    def test_factorial_1(self):
        result = interfaz('')
        self.assertEqual(result, 'Ingrese un numero')

if __name__ == '__main__':
    unittest.main()