import funcs
import unittest

class TestFuncs(unittest.TestCase):
    
    def testMirroir(self):
        self.assertEqual(funcs.miroir("azerty",3),"azerreza")
        self.assertEqual(funcs.miroir("123456789",5),"123456654321")
        self.assertEqual(funcs.miroir("a",2),"")
        self.assertEqual(funcs.miroir(" ",10),"")
        self.assertEqual(funcs.miroir("",10),"")
        self.assertEqual(funcs.miroir("&",0),"&&")
        self.assertEqual(funcs.miroir('a',0),'aa')

        self.assertEqual(funcs.miroir(123,0),"")
        self.assertEqual(funcs.miroir(1.2,0),"")
        self.assertEqual(funcs.miroir(True,0),"")
        self.assertEqual(funcs.miroir(False,0),"")




if __name__ == '__main__':
	unittest.main()