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
    def trierVecteur(vecteur):
        """
        Trie un vecteur en ordre croissant

        Args:
            :type vecteur: int[]
            :param vecteur: un tableau de nombres

        Returns:
            Le vecteur trie.

        """
        for j in range(0,len(vecteur)):
            for i in range(0,len(vecteur)-1):
                if vecteur[i]>vecteur[i+1]:
                    tmp=vecteur[i]
                    vecteur[i]=vecteur[i+1]
                    vecteur[i+1]=tmp
        return vecteur

    @staticmethod
    def sommerVecteurs(vect1, vect2):
        """
        Somme les deux vecteurs :vect1 et :vect2 element par element

        Args:
            :type vect1: int[]
            :param vect1: un tableau de nombres

            :type vect2: int[]
            :param vect2: un tableau de nombres

            Les deux vecteurs :vect1 et :vect2 doivent etre de meme taille


        Returns:
            :int[] La somme des elements de :vect1 et :vect2 element par element

        Raises:
            :DifferentSizeVectorsException: si :vect1: et :vect2: sont de tailles differents
        """

        if len(vect1)!=len(vect2):
            raise DifferentSizeVectorsException()
        vect3 = [None]*len(vect1)
        for i in range(0,len(vect1)-1):
            vect3[i]=vect1[i]+vect2[i]
        return vect3

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
            vec.append(vecteur[i] * 2)

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


        liste.append( min)
        liste.append(max)

        return liste



    @staticmethod
    def inverserVecteur(vect):
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
    
        for i in vect[::-1]:
            vec.append( i)
      
        return vec

    

class DifferentSizeVectorsException(Exception):
    def __init__(self):
        Exception.__init__(self,"Les vecteurs doivent avoir la meme taille")
