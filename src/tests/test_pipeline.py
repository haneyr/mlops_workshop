
import unittest
from pipeline import concat, reverse, basic_pipeline

class TestBasicPipeline(unittest.TestCase):
    # def setUp(self):
        # Get relevant component
    
    def test_concat_component(self):
        self.assertEqual(concat.python_func(3, 3), 6)

    def test_reverse(self):
        self.assertEqual(reverse.python_func("stressed")[1], "desserts")

    def test_pipeline(self):
        pass

if __name__ == '__main__':
    unittest.main()
