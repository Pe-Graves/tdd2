import funcs
import unittest
import math

class TestFuncs(unittest.TestCase):
    
    def testApproximationFunction(self):

        self.assertEqual(funcs.approximation(funcs.fonction1,0.01,0),0)
        self.assertEqual(funcs.approximation(funcs.fonction1,0.01,0.0),0)
        self.assertEqual(funcs.approximation(funcs.fonction1,0.001,0.4253),0.904)
        self.assertEqual(funcs.approximation(funcs.fonction1,0.1,1.23),7.5)

        self.assertEqual(funcs.approximation(funcs.fonction2,0.01,0),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,0.01,0.0),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,0.01,0.4253),1.27)
        self.assertEqual(funcs.approximation(funcs.fonction2,0.1,1.23),3.6)

        self.assertEqual(funcs.approximation(funcs.fonction3,0.01,0),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,0.01,0.0),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,0.01,0.4253),2.35)
        self.assertEqual(funcs.approximation(funcs.fonction3,0.1,1.23),0.8)

        self.assertEqual(funcs.approximation(funcs.fonction1,1,1.1),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,1,1.1),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,1,1.1),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,0.1,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,0.1,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,0.1,1),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,1.0,1.0),5.0)
        self.assertEqual(funcs.approximation(funcs.fonction2,1.0,1.0),3.0)
        self.assertEqual(funcs.approximation(funcs.fonction3,1.0,1.0),1.0)

        self.assertEqual(funcs.approximation(funcs.fonction1,0.23,1.0),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,0.654,1.0),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,0.876,1.0),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,1.23,1.1),5*1.1**2)
        self.assertEqual(funcs.approximation(funcs.fonction2,1.23,1.1),3*1.1)
        self.assertEqual(funcs.approximation(funcs.fonction3,1.23,1.1),1/1.1)

        self.assertEqual(funcs.approximation(funcs.fonction1,-1.23,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,-1.23,1),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,-1.23,1),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,"-1.23",1),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,"-1.23",1),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,"-1.23",1),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,'-1.23',1),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,'-1.23',1),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,'-1.23',1),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,-1.23,"1"),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,-1.23,"1"),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,-1.23,"1"),0)

        self.assertEqual(funcs.approximation(funcs.fonction1,-1.23,'1'),0)
        self.assertEqual(funcs.approximation(funcs.fonction2,-1.23,'1'),0)
        self.assertEqual(funcs.approximation(funcs.fonction3,-1.23,'1'),0)

        #Fonction trigonométrique sin et cos 

        self.assertEqual(funcs.approximation(funcs.fonction4,0.001,math.pi/2),1.0)
        self.assertEqual(funcs.approximation(funcs.fonction5,0.001,math.pi/2),0.0)
        self.assertEqual(funcs.approximation(funcs.fonction4,0.001,math.pi),0.0)
        self.assertEqual(funcs.approximation(funcs.fonction5,0.001,math.pi),-1.0)
        self.assertEqual(funcs.approximation(funcs.fonction4,0.001,0.0),0.0)
        self.assertEqual(funcs.approximation(funcs.fonction5,0.001,0.0),1.0)

        self.assertEqual(funcs.approximation(funcs.fonction4,-1.23,'1'),0)
        self.assertEqual(funcs.approximation(funcs.fonction5,-1.23,'1'),0)
        self.assertEqual(funcs.approximation(funcs.fonction4,'-1.23',1),0)
        self.assertEqual(funcs.approximation(funcs.fonction5,'-1.23',1),0)

if __name__ == '__main__':
	unittest.main()