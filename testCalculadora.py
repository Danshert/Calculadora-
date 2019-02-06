import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

	def test_suma_2_mas_dos(self):
		calc = Calculadora()
		self.assertEquals(4, calc.suma(2, 2))

if __name__ == '__main__':
    unittest.main()