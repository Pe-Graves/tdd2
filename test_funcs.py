import funcs
import unittest

class TestFuncs(unittest.TestCase):
    
    def testApproximationFunction(self):
        self.assertEqual(funcs.approximation(funcs.fonction,0.4253,0.01),7.96)
        self.assertEqual(funcs.approximation(funcs.fonction,0.234,0.001),4.92)
        self.assertEqual(funcs.approximation(funcs.fonction,1,1),25)
        self.assertEqual(funcs.approximation(funcs.fonction,0,0.001),0)
        self.assertEqual(funcs.approximation(funcs.fonction,0.234,0),0)



if __name__ == '__main__':
	unittest.main()