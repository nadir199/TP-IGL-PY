import unittest

class VectorHelperTest(unittest.TestCase):
    def test_trierVecteur(self):
        test_case=[10,9,30,2,2,11,20,30,-5,0]
        trierVecteur(test_case)
        trie=true
        for i in range(1,test_case.length-1):
            if(test_case[i]>test_case[i+1]):
                trie=false
                break
        self.assertTrue(trie)
        
