import funcs
import unittest

class TestFuncs(unittest.TestCase):
    
    def testApproximationFunction(self):

        self.assertEqual(funcs.approximation(funcs.fonction1,0.01,0),0)
        self.assertEqual(funcs.approximation(funcs.fonction1,0.001,0.4253),0.904)
        self.assertEqual(funcs.approximation(funcs.fonction1,0.1,1.23),7.5)

        self.assertEqual(funcs.approximation(funcs.fonction2,0.01,0),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,0.01,0.4253),1.27)
        self.assertEqual(funcs.approximation(funcs.fonction2,0.1,1.23),3.6)

        self.assertEqual(funcs.approximation(funcs.fonction3,0.01,0),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,0.01,0.4253),2.35)
        self.assertEqual(funcs.approximation(funcs.fonction3,0.1,1.23),0.8)

        self.assertEqual(funcs.approximation(funcs.fonction1,0,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,0,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,0,1),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,1,1),5)
        self.assertEqual(funcs.approximation(funcs.fonction2,1,1),3)
        self.assertEqual(funcs.approximation(funcs.fonction3,1,1),1)

        self.assertEqual(funcs.approximation(funcs.fonction1,1.23,1),5)
        self.assertEqual(funcs.approximation(funcs.fonction2,1.23,1),3)
        self.assertEqual(funcs.approximation(funcs.fonction3,1.23,1),1)

        self.assertEqual(funcs.approximation(funcs.fonction1,-1.23,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,-1.23,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,-1.23,1),0)



if __name__ == '__main__':
	unittest.main()