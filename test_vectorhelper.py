import unittest
from VectorHelper import VectorHelper

class VectorHelperTest(unittest.TestCase):
    """
    
        Cette classe teste les méthodes de la classe 'VectorHelper'
        
    """
    
    def test_appFormule(self):
        """
            Test de la méthode 'appFormule' qui multiplie par 2 les elements du vecteur argument.
        """

        test_case=[10,9,30,2,2,11,20,30,-5,0]
        vec = VectorHelper.appFormule(test_case)
        
        error = true
        for i in range(0,len(test_case)): 
        	if vec[i] != test_case[i] * 2:
        		error = false
                break


        self.assertTrue(error)
        
    def test_minMax(self):
        """ 
            Test de la méthode 'minMax' qui retourne le minimum et le maximum d'un vecteur d'entier. 
        """

        test_case=[10,9,30,2,2,11,20,30,-5,0]
        min = -5
        max = 30
        vec = VectorHelper.minMax(test_case)
        
        error = true
        if vec[0] != min :
        	error = false

        if vec[1] != max :
        	error = false


        self.assertTrue(error)

    def testPair_inverserVecteur(self):
        vecteur = [1, 2, 3, 4, 5, 6]
        saveVect = [1, 2, 3, 4, 5, 6]
        VectorHelper.inverserVecteur(vecteur)
        inverted = True
        for i in range(0, len(vecteur) - 1):
            if vecteur[i] != saveVect[len(vecteur) - 1 - i]:
                inverted = False
                break
        self.assertTrue(inverted)

    def testImpair_inverserVecteur(self):
        vecteur = [1, 2, 3, 4, 5]
        saveVect = [1, 2, 3, 4, 5]
        VectorHelper.inverserVecteur(vecteur)
        inverted = True
        for i in range(0, len(vecteur) - 1):
            if vecteur[i] != saveVect[len(vecteur) - 1 - i]:
                inverted = False
                break
        self.assertTrue(inverted)

    def testEmptyAndOne_inverserVecteur(self):
        vecteur = []
        VectorHelper.inverserVecteur(vecteur)
        self.assertTrue(vecteur == [])

        vecteurOne = [1]
        VectorHelper.inverserVecteur(vecteurOne)
        self.assertTrue(vecteurOne == [1])