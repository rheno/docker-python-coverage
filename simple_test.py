import unittest
from simple import Simple

class SimpleTestCase(unittest.TestCase):
	def setUp(self):
		self.simple = Simple(3, 4)

	def test_pythagoras(self):
		self.assertEqual(self.simple.pythagoras(), 5)


if __name__ == '__main__':
    unittest.main()
