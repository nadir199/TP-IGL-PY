
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
            :param vecteur: an array of numbers

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