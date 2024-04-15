import Plateau as Pl
from random import randint

class IA:
    def __init__(self):
        """Constructeur d'objet IA
        L'objet IA possède un attribut boites.
        Lors de la création de l'objet cet attribut correspond à un dictionnaire vide
        """
        self.boites = dict() # {config : [ [(0,1,"G"),3], [(1,1,"A"),5], ...]}

    def ajoute_boites(self, pla : Pl, couleur_pion_qui_doit_apprendre = "n") :
        """
        ajoute la boite {c : liste_liste_mouvement_poids} au dictionnaire self.boites
        tel que :
            - c est la configuration associée au plateau(autrement dit sa représentation sous forme de chaine de caractère)
            - liste_liste_mouvement_poids est de la forme [ [(pos_x_1, pos_y_1, mouvement_1), 1], [(pos_x_2, pos_y_2, mouvement_2), 1], ... ]
        
        Exemples:
        >>> ia = IA()
        >>> len(ia.get_boites()) == 0
        True

        >>> plateau1 = Pl.Plateau()
        >>> ia.ajoute_boites(plateau1)
        >>> len(ia.get_boites()) == 1
        True

        >>> plateau2 = Pl.Plateau()
        >>> ia.ajoute_boites(plateau2)
        >>> len(ia.get_boites()) == 1
        True
        
        >>> (list(ia.get_boites().keys())[0] == str(plateau1)) == str(plateau2)
        True  
        >>> (list(ia.get_boites().values())[0] == [ [(0,0,'A'),1], [(1,0,'A'),1], [(2,0,'A'),1] ]
        True
        """
        pass
            

        # dans une config les elements [(0,1,"G"),3] signifie on prends le pion à l'emplacement (0,1) et on le deplace à "G"
                        
    
    def pondere_hausse(self, couple_config_mouvement_choisis_par_IA ): # [(config_ss_forme_de_chaine, (0,1,"G"), (config_ss_forme_de_chaine_2, (1,1,"A"), ...]
        """
        couple_config_mouvement_choisis_par_IA est une liste de couple (c, m) 
        la fonction pondere à la hausse la probabilité pour l'IA d'effectuer les mouvements m lorsqu'elle est confrontée à la config c
        """
        #b = self.get_boites()
        pass  
                    

    
    def choisi_une_boite_pour_une_config(self, config : str)-> tuple:
        """Choisis une boite pour une configuration donné et renvoi un mouvement à effectuer selon les pondérations associés.

        Args:
            config: Une configuration sous forme de chaine de caractères

        Returns:
            Un mouvement choisi de la forme (X, Y, M)
        """
        b = self.get_boites()
        aux = choisis_au_hasard(b[config]) # (0,1,"G")
        res = str(aux[0]) +","+ str(aux[1]) +","+ aux[2]
        return res

    def get_boites(self) -> dict:
        """renvoi la valeur de l'attribut boites

        Returns:
            la valeur de l'attribut boites
        """
        return self.boites
    


    

def choisis_au_hasard(liste_indices_mouvement_poids): 
    """
    liste_indices_mouvement_poids est une liste de couple (mouvement, poids)
    la fonction renvoi un mouvement au hasard de cette liste en tenant compte de la pondération de chaque poids

    param liste_indices_mouvement_poids :  [ [(0,1,"G"), 3], [(1,1,"A"), 5], ...]

    """
    pass



    
    
    
