import Pion as Pi

class Plateau:
    def __init__(self):
        """Constructeur d'objet Plateau
        Un objet Plateau possède un attribut plateau permettant de représenter le plateau de jeu.  
        """
        self.plateau = [
            [Pi.Pion("n") for _ in range(3)],
            [None for _ in range(3)],
            [Pi.Pion("b") for _ in range(3)]
        ]
                    

    def est_gagnant(self, position_pion):
        """Renvoi vrai si un pion est considéré comme gagnant
        Un pion est considéré comme gagnant s'il se trouve sur la ligne de opposé à sa ligne de départ

        Returns:
            True si le pion à la position position_pion est gagnant.
            On dit qu'un pion est gagnant s'il est arrivé sur la ligne de départ de son adversaire

        Exemples:
        >>> pla = self.get_plateau()
        >>> pla.est_gagnant((0,0))
        False
        >>> pla.deplace((0,2), "A")
        >>> pla.deplace((2,0), "A")
        >>> pla.deplace((0,1), "D")
        >>> pla.est_gagnant((1,0))
        True
        """
        pass


    def deplace(self, position_pion : tuple, action : str):
        """deplace le pion à la position position_pion
        avec le mouvement action sur le self(le plateau)

        Args:
            position_pion: la position du pion à déplacer
            action: "A", "G" ou "D" 
            

        Returns:
            la liste de liste de case du plateau mis à jour après le mouvement effectué 

        Exemples:
        >>> pla = Plateau()
        >>> str(pla)
        ♟♟♟
        ___
        ♙♙♙
        
        >>> pla.deplace((0,2), "A")
        >>> str(pla)
        ♟♟♟
        ♙__
        _♙♙

        >>> pla.deplace((0,1), "D")
        >>> str(pla)
        ♟♙♟
        ___
        _♙♙
        """
        pass
     
    
        
    def mouvement_possible(self, position_pion : tuple) -> list :
        """Renvoi la liste des déplacements disponible pour un pion  

        Args:
            position_pion: La position du pion dont on souhaite connaitres les déplacements disponible

        Returns:
            Une liste contenant les déplacements possible pour un pion
            Les déplacements possible:
                            "A" : Avancer
                            "G" : Attaque vers la gauche(du point de vue des blancs)
                            "D" : Attaque vers la droite(du point de vue des blancs)
        """
        
        li_li_mes_cases = self.get_plateau()
        x_pos, y_pos = position_pion
        c = li_li_mes_cases[y_pos][x_pos].get_color()
        
        res = []
        
        if not((c == "b" and y_pos == 0) or (c == "n" and y_pos == 2)):
            if c == "b":
                if li_li_mes_cases[y_pos-1][x_pos] is None: # cas avance
                    res.append("A")
                
                if (x_pos != 0):
                    aux_b_g = li_li_mes_cases[y_pos-1][x_pos-1]
                    if aux_b_g is not None and aux_b_g.get_color() == "n": # cas attaque à gauche
                        res.append("G")

                if (x_pos != 2):
                    aux_b_d = li_li_mes_cases[y_pos-1][x_pos+1]
                    if aux_b_d is not None and aux_b_d.get_color() == "n": # cas attaque à droite
                        res.append("D")

            elif c == "n":
                if li_li_mes_cases[y_pos+1][x_pos] is None:
                    res.append("A")
                
                if (x_pos != 0):
                    aux_n_g = li_li_mes_cases[y_pos+1][x_pos-1]
                    if aux_n_g is not None and aux_n_g.get_color() == "b":  # cas attaque à gauche
                        res.append("G")

                if (x_pos != 2):
                    aux_n_d = li_li_mes_cases[y_pos+1][x_pos+1]
                    if aux_n_d is not None and aux_n_d.get_color() == "b":  # cas attaque à droite
                        res.append("D")

        return res


    def partie_est_finie(self) -> bool:
        """Renvoi un booléen associé à l'état de la partie afin de savoir si elle est finit

        Args:
            p: le plateau

        Returns:
            True si la partie est finit, False sinon
        """
        res = True
        li_li_cases = self.get_plateau()
        nb_pion_blanc, nb_pion_noir = 0, 0

        for ind_ligne in range(len(li_li_cases)):
            for ind_case in range(len(li_li_cases[0])):
                case = li_li_cases[ind_ligne][ind_case]
                if not (case is None):
                    if self.est_gagnant((ind_case, ind_ligne)):
                        return True
                    
                    else:
                        if case.get_color() == "b":
                            nb_pion_blanc += 1
                        elif case.get_color() == "n":
                            nb_pion_noir += 1

                        li_mouvement = self.mouvement_possible((ind_case, ind_ligne))
                        res = res and (li_mouvement == [])

        return res or (nb_pion_noir == 0) or (nb_pion_blanc == 0)
    
        
    def set_plateau(self, nouveau_plateau):
        """Méthode permettant de modifier la valeur de l'attribut plateau.  

        Args:
            nouveau_plateau: valeur à attribuer à l'attribut plateau  
        """
        self.plateau = nouveau_plateau
            
    def get_plateau(self) :
        """Méthode permettant de renvoyer la valeur de l'attribut plateau 

        Returns:
            la valeur de l'attribut plateau
        """
        return self.plateau

    def __str__(self):
        """
        Renvoi une représentation du plateau sous forme de chaine de caractère comme dans l'exemple

        Exemples:
        >>> pla = Plateau()
        >>> str(pla)
        ♟♟♟
        ___
        ♙♙♙
        """
        pass
                    
        
        
                    
            
            
    
if __name__ == "__main__":
    p = Plateau()
    print(p)