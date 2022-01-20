import funcs
import unittest

class TestFuncs(unittest.TestCase):
    
    def testMirroir(self):
        self.assertEqual(funcs.miroir("azerty",3),"azerreza")
        self.assertEqual(funcs.miroir("123456789",5),"1234554321")
        self.assertEqual(funcs.miroir("a",2),"")
        self.assertEqual(funcs.miroir(" ",10)," ")
        self.assertEqual(funcs.miroir("",10),"")


if __name__ == '__main__':
	unittest.main()