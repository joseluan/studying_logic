from lisp import valid
import unittest


class ParenthesisCases(unittest.TestCase):                
                
    def test_case_1(self):        
        self.assertTrue(valid('()'))
    
    def test_case_2(self):        
        self.assertTrue(valid('(())'))

    def test_case_3(self):        
        self.assertFalse(valid('())'))
    
    def test_case_4(self):        
        self.assertFalse(valid('())('))
    
    def test_case_5(self):        
        self.assertTrue(valid('()()'))
        
    def test_case_6(self):        
        self.assertFalse(valid(')()('))


class SquareBracketsCases(unittest.TestCase):                
                
    def test_case_1(self):        
        self.assertTrue(valid('[]'))
    
    def test_case_2(self):        
        self.assertTrue(valid('[[]]'))
    
    def test_case_3(self):        
        self.assertTrue(valid('[][]'))
    
    def test_case_4(self):        
        self.assertFalse(valid(']['))
    
    def test_case_5(self):        
        self.assertFalse(valid('[]]['))
    
    def test_case_6(self):        
        self.assertFalse(valid('][]['))


class SquareBracketsParenthesisCases(unittest.TestCase):                
                
    def test_case_1(self):        
        self.assertTrue(valid('[]()'))
    
    def test_case_2(self):        
        self.assertTrue(valid('([])'))

    def test_case_3(self):        
        self.assertTrue(valid('([])'))
    
    def test_case_4(self):        
        self.assertTrue(valid('[([]())]'))
        
    def test_case_5(self):        
        self.assertFalse(valid('[([]())]]'))
    
    def test_case_6(self):
        self.assertFalse(valid('[([]()))]'))
    
    def test_case_7(self):
        self.assertFalse(valid('[(])'))
    
    def test_case_8(self):
        self.assertFalse(valid('[()]['))


class KeysCases(unittest.TestCase):
                
    def test_case_1(self):        
        self.assertTrue(valid('{}'))
    
    def test_case_2(self):
        self.assertTrue(valid('{}{}'))
    
    def test_case_3(self):
        self.assertTrue(valid('{{}}'))
    
    def test_case_4(self):
        self.assertTrue(valid('{{}}{}{{}}'))
    
    def test_case_5(self):
        self.assertFalse(valid('{{}}{}{{}}}'))
    
    def test_case_6(self):
        self.assertFalse(valid('{{}}{}}{}}}{{{{{}}}'))
    
    def test_case_7(self):
        self.assertFalse(valid('{{}}{'))
    
    def test_case_8(self):
        self.assertFalse(valid('{{}}}'))



class KeysSquareBracketsCases(unittest.TestCase):
                
    def test_case_1(self):        
        self.assertTrue(valid('{[]}'))
    
    def test_case_2(self):        
        self.assertTrue(valid('{}[]'))
    
    def test_case_3(self):        
        self.assertTrue(valid('{[{}]}'))
    
    def test_case_3(self):        
        self.assertFalse(valid('{[}]'))
    
    def test_case_3(self):        
        self.assertFalse(valid('{[{}]}]'))
    
    def test_case_3(self):        
        self.assertFalse(valid(']{[{}]}['))


class AllCases(unittest.TestCase):
                
    def test_case_1(self):        
        self.assertTrue(valid('{[()]}'))
    
    def test_case_2(self):        
        self.assertTrue(valid('{[()(){}{}[]]}'))
    
    def test_case_3(self):        
        self.assertTrue(valid('{[()]}[()]{}[]'))
    
    def test_case_4(self):        
        self.assertTrue(valid('{}[][][]({}{{{{{{[]}}}}}})'))
    
    def test_case_5(self):        
        self.assertTrue(valid('{[()]}({[]})([{}])[{()}][({})]'))
        
    def test_case_6(self):        
        self.assertFalse(valid('[][]{]}}}(())()()[]}{{}{}['))

    def test_case_7(self):        
        self.assertFalse(valid('()['))
    
    def test_case_8(self):        
        self.assertFalse(valid('{}['))
    
    def test_case_9(self):        
        self.assertFalse(valid('[]{'))
    
    def test_case_10(self):        
        self.assertFalse(valid('(){'))
    
    def test_case_11(self):        
        self.assertFalse(valid('[]('))
    
    def test_case_12(self):        
        self.assertFalse(valid('{}('))

    def test_case_13(self):        
        self.assertFalse(valid('][]]]{[]]}}}}{{}{}['))

    def test_case_14(self):        
        self.assertFalse(valid('[][]{]}}}}{{}{}['))

    def test_case_15(self):        
        self.assertFalse(valid('[][]{]}[]}}}{{}{}['))

    def test_case_16(self):        
        self.assertFalse(valid('[][]{]}}}}{{}{}['))

    def test_case_17(self):        
        self.assertFalse(valid('[][]{]]][[[]]]}[]}[]}}{{}{}['))


if __name__ == "__main__":
    unittest.main()