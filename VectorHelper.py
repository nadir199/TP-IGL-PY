class VectorHelper:
    def __init__(self):
        pass

    @staticmethod
    def appFormule(vecteur):
        for i in range(0, len(vecteur)):
            vecteur[i] = vecteur[i] * 2

        return vecteur 
