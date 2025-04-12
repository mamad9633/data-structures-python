import unittest
from data_structures import Array

class TestArray(unittest.TestCase):
    def setUp(self):
        self.array = Array()

    def test_insert(self):
        self.array.insert(5)
        self.array.insert(10)
        self.assertEqual(self.array.get(0), 5)
        self.assertEqual(self.array.get(1), 10)

    def test_delete(self):
        self.array.insert(5)
        self.array.insert(10)
        self.array.delete(0)
        self.assertEqual(self.array.get(0), 10)

    def test_visualize(self):
        self.array.insert(5)
        self.array.insert(10)
        # This test checks if visualize runs without error
        try:
            self.array.visualize()
        except Exception as e:
            self.fail(f"Visualization failed with error: {e}")

if __name__ == '__main__':
    unittest.main()