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
        
        
    def test_inverserVecteur(self):
        """
            Test de la méthode 'inverserVecteur' qui inverse les elements du vecteur argument.
        """

        test_case=[10,9,30,2,2,11,20,30,-5,0]
        test_result = [0,-5,30,20,11,2,2,30,9,10]
        vec = VectorHelper.inverserVecteur(test_case)

        error = false
        for i in range(len(test_case)):
            if vec[i] != test_result[i]:
                error = true
                break

        self.assertTrue(error)