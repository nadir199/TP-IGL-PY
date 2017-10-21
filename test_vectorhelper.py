import unittest
from VectorHelper import VectorHelper
from VectorHelper import DifferentSizeVectorsException

class VectorHelperTest(unittest.TestCase):
    """
        Cette classe teste les méthodes de la classe 'VectorHelper'    
    """
    #General case test
    def test_trierVecteur(self):
        """
        Teste le fonctionnement de la fonction *trierVecteur* qui trie le vecteur donne en parametre
        """
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
        """
        Teste le cas du tri d'un tableau vide
        """
        res=VectorHelper.trierVecteur([])
        self.assertTrue([]==res)

    def test_sommerVecteurs(self):
        """
        Teste le fonctionnement de la fonction *sommerVecteurs* qui somme deux vecteurs
        """
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
        """
        Teste qu'une exception est generee si les tailles des vecteurs sont differentes
        """
        vecteur1=[11,3,10]
        vecteur2=[11,3]
        with self.assertRaises(DifferentSizeVectorsException):
            VectorHelper.sommerVecteurs(vecteur1,vecteur2)
            
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
          
if __name__ == '__main__':
    unittest.main(verbosity=2)