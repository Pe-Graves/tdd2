import funcs
import unittest

class TestFuncs(unittest.TestCase):
    
    def testDerivee(self):
        self.assertEqual(funcs.derivee([2.0,1.0,4.0,3.0]),[-0.5,1.5,-0.5])
        self.assertEqual(funcs.derivee([]),[0.0])
        self.assertEqual(funcs.derivee([2.0,2.0,1.0]),[0.0,-0.5])
        self.assertEqual(funcs.derivee([0.0]),[0.0])
        self.assertEqual(funcs.derivee([0.0,0.0]),[0.0])
        self.assertEqual(funcs.derivee([0.0,1.0]),[0.5])
        self.assertEqual(funcs.derivee(["a","b","d","zd"]),[0.0])
        self.assertEqual(funcs.derivee([1,2,3,4,4]),[0.0])
        self.assertEqual(funcs.derivee(['a','b','m']),[0.0])



if __name__ == '__main__':
	unittest.main()