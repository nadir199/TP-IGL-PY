import unittest
from VectorHelper import VectorHelper
from VectorHelper import DifferentSizeVectorsException

class VectorHelperTest(unittest.TestCase):
    #General case test
    def test_trierVecteur(self):
        test_case=[10,9,30,2,2,11,20,30,-5,0]
        VectorHelper.trierVecteur(test_case)
        trie=True
        for i in range(0,len(test_case)-1):
            if(test_case[i]>test_case[i+1]):
                trie=False
                break
        self.assertTrue(trie)
    #Test for empty array
    def testVide_trierVecteur(self):
        res=VectorHelper.trierVecteur([])
        self.assertTrue([]==res)

    def test_sommerVecteurs(self):
        vecteur1=[10,9,23,2,11,2,1,3,10]
        vecteur2=[10,11,7,8,9,18,19,17,10]
        vecteur3=VectorHelper.sommerVecteurs(vecteur1,vecteur2)
        error=False
        for i in range(0, len(vecteur1)-1):
            if(vecteur1[i]+vecteur2[i] != vecteur3[i]):
                error=True
                break
        self.assertFalse(error)
    def testException_sommerVecteurs(self):
        vecteur1=[11,3,10]
        vecteur2=[11,3]
        with self.assertRaises(DifferentSizeVectorsException):
            VectorHelper.sommerVecteurs(vecteur1,vecteur2)

if __name__ == '__main__':
    unittest.main()


