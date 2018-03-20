import unittest

class TS(unittest.TestCase):
    def test_2x2(self):
        self.assertEqual(2 * 2, 4)

if __name__ == '__main__':
    unittest.main()
