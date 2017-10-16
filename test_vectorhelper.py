import unittest
from VectorHelper import VectorHelper
class VectorHelperTest(unittest.TestCase):
    def test_trierVecteur(self):
        test_case=[10,9,30,2,2,11,20,30,-5,0]
        VectorHelper.trierVecteur(test_case)
        trie=True
        for i in range(1,len(test_case)-1):
            if(test_case[i]>test_case[i+1]):
                trie=False
                break
        self.assertTrue(trie)

