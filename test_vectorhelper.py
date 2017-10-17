import unittest
from VectorHelper import VectorHelper

class VectorHelperTest(unittest.TestCase):

    def test_appFormule(self):

        test_case=[10,9,30,2,2,11,20,30,-5,0]
        vec = VectorHelper.appFormule(test_case)
        
        error = false
        for i in range(0,len(test_case)): 
        	if vec[i] != test_case[i] * 2:
        		error = true


        self.assertTrue(error)
