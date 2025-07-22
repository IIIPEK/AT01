import unittest
from main import add, subtract, multiply, divide, modulo, is_even

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertNotEqual(add(1, 2), 4)

    def test_subtract(self):
        self.assertNotEqual(subtract(2, 1), 0)
        self.assertEqual(subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertNotEqual(multiply(2, 3), 7)

    def test_divide(self):
        self.assertEqual(divide(2, 2), 1)
        self.assertEqual(divide(2, 3), 0.6666666666666666)
        self.assertRaises(ValueError, divide, 2, 0)


    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(not is_even(5))

    def test_modulo(self):
        self.assertEqual(modulo(2, 2), 0)
        self.assertEqual(modulo(2, 3), 2)
        self.assertRaises(ValueError, modulo, 2, 0)




if __name__ == '__main__':
    unittest.main()
