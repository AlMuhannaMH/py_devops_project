import unittest    
from main import add, subtract, multiply, divide    

class TestMain(unittest.TestCase):    
    def test_add(self):    
        self.assertEqual(add(2, 3), 5)    
        self.assertEqual(add(-1, 1), 0)    
        self.assertEqual(add(-1, -1), -2)    

    def test_subtract(self):    
        self.assertEqual(subtract(5, 2), 3)    
        self.assertEqual(subtract(-1, 1), -2)    
        self.assertEqual(subtract(-1, -1), 0)    

    def test_multiply(self):    
        self.assertEqual(multiply(3, 4), 12)    
        self.assertEqual(multiply(-1, 1), -1)    
        self.assertEqual(multiply(-1, -1), 1)    

    def test_divide(self):    
        self.assertEqual(divide(10, 2), 5)    
        with self.assertRaises(ValueError):    
            divide(10, 0)    

if __name__ == "__main__":    
    unittest.main(argv=[''], verbosity=2, exit=False)    
