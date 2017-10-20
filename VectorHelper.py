
"""
Ceci est un programme de manipulation de vecteurs
"""
class VectorHelper:
    """
        Cette classe est une classe utilitaire de manipulation des chaines de caractere
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
    def inverserVecteur(vect):
        """
        Inverse le vecteur :vect

        Args:
            :type vect: int[]
            :param vect: un tableau de nombres

        """
        tai=len(vect)
        for i in range(0,int(tai/2)):
            tmp=vect[i]
            vect[i]=vect[tai-1-i]
            vect[tai-1-i]=tmp

        return vect

class DifferentSizeVectorsException(Exception):
    def __init__(self):
        Exception.__init__(self,"Les vecteurs doivent avoir la meme taille")