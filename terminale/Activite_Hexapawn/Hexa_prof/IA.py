#import Boite as Bo
import Plateau as Pl
from random import randint

class IA:
    def __init__(self):
        """Constructeur d'objet IA
        L'objet IA possède un attribut boites.
        Lors de la création de l'objet cet attribut correspond à un dictionnaire vide
        """
        self.boites = dict() # {config : [ [(0,1,"G"),3], [(1,1,"A"),5], ...]}

    def ajoute_boites(self, pla, couleur_pion_qui_doit_apprendre = "n") :
        """
        ajoute la boite {c : liste_couple_mouvement_poids}
        tel que :
            - c est la configuration associée au plateau(autrement dit sa représentation sous forme de chaine de caractère)
            - liste_couple_mouvement_poids est de la forme [ [(pos_x_1, pos_y_1, mouvement_1), 1], [(pos_x_2, pos_y_2, mouvement_2), 1], ... ]
        """
        p = pla.get_plateau()
        config = str(pla)
        if not config in self.boites:
            self.boites[config] = []
            for ind_ligne in range(len(p)):
                for ind_case in range(len(p[0])):
                    case_a_tester = p[ind_ligne][ind_case]
                    if case_a_tester != None and p[ind_ligne][ind_case].get_color() == couleur_pion_qui_doit_apprendre:
                        li_mouvement_disponible = pla.mouvement_possible((ind_case, ind_ligne))
                        for mouvement in li_mouvement_disponible:
                            self.boites[config].append(list(((ind_case, ind_ligne, mouvement), 1))) # dans une config les elements [(0,1,"G"), 3] signifie on prends le pion à l'emplacement (0,1) et on le deplace à "G"
                        
    
    def pondere_hausse(self, couple_config_mouvement_choisis_par_IA): # [(config_ss_forme_de_chaine, (0,1,"G"), (config_ss_forme_de_chaine_2, (1,1,"A"), ...]
        """
        couple_config_mouvement_choisis_par_IA est une liste de couple (c, m) 
        la fonction pondere à la hausse la probabilité pour l'IA d'effectuer les mouvements m lorsqu'elle est confronté à la config c
        """
        b = self.get_boites()
        for config, mouvement in couple_config_mouvement_choisis_par_IA:
            liste_mouvement = b[config]
            
            for mouv in liste_mouvement:
                print(str(mouv[0]), str(mouvement))
                if mouv[0] == mouvement:
                    mouv[1] += 3            
                    

        
    def choisi_une_boite_pour_une_config(self, config):
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

    def get_boites(self):
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
    sommes_tout_les_poids = sum([ind_mouvement_poids[1] for ind_mouvement_poids in liste_indices_mouvement_poids])
    tirage_aleatoire = randint(0, sommes_tout_les_poids)

    listes_proba_cumules = [liste_indices_mouvement_poids[0][1]]
    for i_ind_mouv_poids in range(1, len(liste_indices_mouvement_poids)):
        listes_proba_cumules.append(listes_proba_cumules[i_ind_mouv_poids-1] + liste_indices_mouvement_poids[i_ind_mouv_poids][1])

    i = 0  
    while listes_proba_cumules[i] < tirage_aleatoire:
        i+=1
    return liste_indices_mouvement_poids[i][0] # (0,1,"G")
        
if __name__ == "__main__":
    ia = IA()
    plateau1 = Pl.Plateau()
    ia.ajoute_boites(plateau1)
    print(list(ia.get_boites().values())[0])