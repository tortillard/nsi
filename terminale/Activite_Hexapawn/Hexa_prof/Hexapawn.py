import Plateau as Pl
import Pion as Pi
import IA as i

class Hexapawn:

    def __init__(self):
        """Constructeur d'objet Hexapawn.   
        Le jeu Hexapawn possède un attribut plateau. 
        Lors de la création de l'objet, cet attribut correspond à un plateau lors d'un début de partie. 
        """
        self.Plateau = Pl.Plateau()

    def get_plateau(self):
        """Méthode permettant de renvoyer la valeur de l'attribut plateau  
        """
        return self.Plateau
    
    def set_new_plateau(self):
        """Méthode permettant de réinitialiser la valeur de l'attribut plateau.  
        """
        self.Plateau = Pl.Plateau()

    def est_entree_utilisateur_valide(self, entree_utilisateur : str, plateau : Pl, joueur_qui_doit_jouer_est_blanc : bool) -> bool:
        """fonction permettant de vérifier que l'entrée saisie par un utilisateur est correct

        Args:
            entree_utilisateur: chaine sous la forme X,Y,M où X est la position en abcisse Y en ordonnée (l'origine est en haut à gauche) et M un mouvement parmis {A, G, D}
            plateau: Le plateau sur lequel on joue
            joueur_qui_doit_jouer_est_blanc: True si c'est au tour du joueur avec les pions blanc de jouer

        Returns:
            True si l'entree saisie est validée, False sinon
        """
        
        res = False
        
        coordo_entree = tuple(int(m) for m in entree_utilisateur[:3].split(","))
        coordo_x, coordo_y = coordo_entree
        mouvement_souhaite = entree_utilisateur[-1]
        li_li_cases = plateau.get_plateau()
        pion_a_deplacer = li_li_cases[coordo_y][coordo_x]

        if pion_a_deplacer != None : # les coordonnées entrées désigne bien une case où se situe un pion
            if (pion_a_deplacer.get_color() == "b") == joueur_qui_doit_jouer_est_blanc : # les joueurs doivent déplacer des pions de leur couleurs
    
                liste_moove_possible = plateau.mouvement_possible(coordo_entree)
                if liste_moove_possible != []:
                    if mouvement_souhaite in liste_moove_possible:
                        res = True
        return res



    def joue(self, ia : i):
        """Méthode permettant de lancer la partie, il faut utiliser la méthode Plateau.place_pion() au préhalable
        """
    
        self.set_new_plateau()
        p = self.get_plateau()
        ia.ajoute_boites(p)
        couple_config_mouvement_choisis_par_IA = []

        joueur_qui_doit_jouer_est_blanc = True
        entree_utilisateur = "1,1,R" #initialisation absurde pour un premier tour de boucle
        
        ia_bete = i.IA()
        ia_bete.ajoute_boites(p, "b")

        #print(p)

        while not p.partie_est_finie():
            
            while not self.est_entree_utilisateur_valide(entree_utilisateur, p, joueur_qui_doit_jouer_est_blanc):
                if joueur_qui_doit_jouer_est_blanc:
                    #entree_utilisateur = input("mouvement souhaité par les pions blancs ? : ") # entree du type 0,2,A
                    entree_utilisateur = ia_bete.choisi_une_boite_pour_une_config(str(p))
                else:
                    #entree_utilisateur = input("mouvement souhaité par les pions noirs ? : ")
                    entree_utilisateur =  ia.choisi_une_boite_pour_une_config(str(p)) 
                      
            if not joueur_qui_doit_jouer_est_blanc:
                tranforme_entree_utilisateur = tuple((( int(entree_utilisateur[0])), int(entree_utilisateur[2]), str(entree_utilisateur[-1])))
                couple = str(p), tranforme_entree_utilisateur
                couple_config_mouvement_choisis_par_IA.append(couple)
                
            coordo_entree = tuple(int(m) for m in entree_utilisateur[:3].split(","))
            mouvement_souhaite = entree_utilisateur[-1]

            new_li_li_cases = p.deplace(coordo_entree, mouvement_souhaite)      

            

            p.set_plateau(new_li_li_cases) # pour optimiser : l'IA prend des configs final(incoherente) c'est pg ça fontcionne quand même !
            # mais si on veut changer ça il faut faire une modif sur les lignes ici 
            # on ajoute les config des parties gagnantes pour l'IA bete ça pollue la mémoire ! :)
            
            ia.ajoute_boites(p)
            ia_bete.ajoute_boites(p, "b")

            #print(p)

            joueur_qui_doit_jouer_est_blanc = not joueur_qui_doit_jouer_est_blanc


        if joueur_qui_doit_jouer_est_blanc:
            return couple_config_mouvement_choisis_par_IA
        return [None]
            
        
    def joue_et_apprends(self, nb_partie : int) -> i.IA :
        """Méthode permettant de simuler l'apprentissage d'un objet de la classe IA du jeu Hexapawn.

        Args:
            nb_partie: le nombre de partie que l'on souhaite faire jouer à notre IA

        Returns:
            l'objet IA qui à appris
        """
        ia = i.IA()
        nb_victoire_IA = 0
        for _ in range(nb_partie):
            couple_config_mouvement_choisis_par_IA =  self.joue(ia) # renvoi [(config_ss_forme_de_chaine, (0,1,"G"), (config_ss_forme_de_chaine_2, (1,1,"A"), ...]
            if not (None in couple_config_mouvement_choisis_par_IA):
                nb_victoire_IA += 1 
                ia.pondere_hausse(couple_config_mouvement_choisis_par_IA)
            
        print(nb_victoire_IA)
        return ia        


if __name__ == "__main__":
    h = Hexapawn()
    p = h.get_plateau()
    # h.joue()

    ia = h.joue_et_apprends(150)
    jeux_apprentissage = ia.get_boites()
    for cle, valeur in jeux_apprentissage.items():
        print(cle +" : "+ str(valeur))

    
