
class Pion:
    def __init__(self, couleur):
        """Constructeur d'objet Pion

        Args:
            couleur: le caractère 'b' ou 'n' selon si le pion est blanc ou noir 
        """
        self.col = couleur
     
    def get_color(self):
        """renvoi la valeur de l'attribut 'color'

        """
        return self.col

    def __str__(self):
        """renvoi une représentation sous forme de chaine de caractère
        en utilisant les caractères unicode des pions blancs et noirs

        """
        c = self.get_color()
        if c == 'b':
            res = '♙' #pion blanc
        else:
            res = '♟' #pion noir
        return res
    


if __name__ == "__main__":
    p = Pion((0,0), 'n')
   