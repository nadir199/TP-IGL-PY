class VectorHelper:
    def __init__(self):
        pass

     @staticmethod
    def appFormule(vecteur):
        """
        Cette fonction permet d'appliquer la multiplication fois 2 à tous les éléments du vecteur en argument
            :param vecteur: Un tableau d'entier sur lequel on applique la formule 
            :return: Un tableau d'entier avec les valeurs * 2 
            :rtype: list 

            :example: 

            >>> appFormule([1,2])
            [2,4]
             

        """
        vec = []
        for i in range(0, len(vecteur)):
            vec[i] = vecteur[i] * 2

        return vec
