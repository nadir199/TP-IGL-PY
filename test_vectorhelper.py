import unittest
from VectorHelper import VectorHelper

class VectorHelperTest(unittest.TestCase):

    def test_appFormule(self):

        test_case=[10,9,30,2,2,11,20,30,-5,0]
        vec = VectorHelper.appFormule(test_case)
        
        error = true
        for i in range(0,len(test_case)): 
        	if vec[i] != test_case[i] * 2:
        		error = false


        self.assertTrue(error)
        
    def test_minMax(self):

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
