import unittest
from mathfunc import *
import HTMLTestRunner

class TestMathFunc(unittest.TestCase):
    def add(a, b):
        return a + b

    def test_01(self):
        self.assertEqual(3, self.add(1, 4))

    def test_02(self):
        self.assertEqual(5, self.add(1, 4))

if __name__ == '__main__':
    filepath = 'D://Cathcybk_test_report.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunc('test_01'))
    suite.addTest(TestMathFunc('test_02'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='Cathaybk test report')
    runner.run(suite)
    unittest.main()