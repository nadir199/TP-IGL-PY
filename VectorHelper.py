class VectorHelper:
    def __init__(self):
        pass

    @staticmethod
    def trierVecteur(vecteur):
        for j in range(0,len(vecteur)):
            for i in range(0,len(vecteur)-1):
                if vecteur[i]>vecteur[i+1]:
                    tmp=vecteur[i]
                    vecteur[i]=vecteur[i+1]
                    vecteur[i+1]=tmp
        return vecteur

