import unittest

def fact(n):
    f = 1
    if n > 1:
        for i in range(1, n + 1):
            f *= i
    return f

class TestFactorial(unittest.TestCase):
    def test_fact_0(self):
        self.assertEquals(fact(0), 1)
    def test_fact_1(self):
        self.assertEquals(fact(1), 1)
    def test_fact_neg(self):
        self.assertEquals(fact(-1), 1)
    def test_fact_5(self):
        self.assertEquals(fact(5), 120)

    def setUp(self):
        print('Setting up...')
    def tearDown(self):
        print('Tearing down...')

if __name__ == '__main__':
    unittest.main()