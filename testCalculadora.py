import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

	def test_suma_dos_mas_dos(self):
		calc = Calculadora()
		self.assertEquals(4, calc.suma(2, 2))

	def test_suma_dos_mas_tres(self):
		calc = Calculadora()
		self.assertEquals(5, calc.suma(2, 3))


if __name__ == '__main__':
    unittest.main()