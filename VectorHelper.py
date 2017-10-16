class VectorHelper:
    def __init__(self):
        pass

    @staticmethod
    def trierVecteur(vecteur):
        for j in range(1,len(vecteur)):
            for i in range(j,len(vecteur)-1):
                if vecteur[j]>vecteur[j+1]:
                    tmp=vecteur[j]
                    vecteur[j]=vecteur[j+1]
                    vecteur[j+1]=tmp
        return vecteur


