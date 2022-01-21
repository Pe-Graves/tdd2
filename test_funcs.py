import funcs
import unittest

class TestFuncs(unittest.TestCase):
    
    def testDeriveeSeconde(self):
        self.assertEqual(funcs.deriveeSeconde([]),[0.0])
        self.assertEqual(funcs.deriveeSeconde([0.0]),[0.0])
        self.assertEqual(funcs.deriveeSeconde([0.0,0.0]),[0.0])
        self.assertEqual(funcs.deriveeSeconde([0.0,0.0,0.0]),[0.0])
        self.assertEqual(funcs.deriveeSeconde([0.0,0.0,0.0]),[0.0])
        self.assertEqual(funcs.deriveeSeconde(["adad","azfdnaf","zfh","ozlad"]),[0.0])
        self.assertEqual(funcs.deriveeSeconde(['a','b','r','i']),[0.0])
        self.assertEqual(funcs.deriveeSeconde([1,2,3,4,5]),[0.0])
        self.assertEqual(funcs.deriveeSeconde([1.0,1.0,1.0,1.0]),[0.0,0.0])
        self.assertEqual(funcs.deriveeSeconde([1.0,2.0,2.0,4.0]),[-0.25,0.5])


if __name__ == '__main__':
	unittest.main()