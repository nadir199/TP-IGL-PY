"""

Ceci est un programme de manipulation de vecteurs

"""

class VectorHelper:
    
    """
        Cette classe est une classe utilitaire de manipulation des vecteurs d'entiers.
        
    """
    
    def __init__(self):
        pass

     @staticmethod
    def appFormule(vecteur):
        """
        
        Cette fonction permet d'appliquer la multiplication fois 2 à tous les éléments du vecteur en argument
        
        :args: 
        
            :param vecteur: Un tableau d'entier sur lequel on applique la formule 
            :return: Un tableau d'entier avec les valeurs * 2 
            :rtype: list 

        :example: >>> appFormule([1,2])
                     [2,4]
             

        """
        vec = []
        for i in range(0, len(vecteur)):
            vec[i] = vecteur[i] * 2

        return vec

    @staticmethod
    def minMax(vecteur):

        """
        
        Cette fonction permet de calculer simultanement le max et le min d'un vecteur d'entier :vecteur .
        
        args: 
        
            :param vecteur: Un tableau d'entier 
            :return: Un tableau d'entier [2] un pour le min et le deuxieme pour le max 
            :rtype: list 

        :example:  >>> minMax([1,2,3,4])
                       [1,4]

        """

        max = 0
        min = 10000 

        liste = []
        for i in range(0,len(vecteur)):
            if vecteur[i] > max : 
                max = vecteur[i]

            if vecteur[i] < min : 
                min = vecteur[i]


        liste[0] = min 
        liste[1] = max 

        return liste

    
                  
      @staticmethod 
      def inverserVecteur(vecteur):
        """
        
        Cette fonction permet de retourner l'inverse du vecteur en entrée. 

        args: 
        
            :param vecteur: Un tableau d'entier 
            :return: Un tableau d'entier
            :rtype: int[]

       :example: >>> inverserVecteur([1,2,3,4])
                     [4,3,2,1]
             

        """
        vec = []
        k = 0
        for i in vecteur[::-1]: 
            vec[k] = i
            k = k + 1 

        return vec
             
