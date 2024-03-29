

#################
# TRI SELECTION #
#################


def selection_min(l : list[int], ind : int):
    """Selectionne l'indice de l'élément minimum dans la tranche l[i:]

    Args:
        l: Une liste d'entiers non vide
        ind: Un indice d'élément tel que 0 <= ind < len(l) 

    Returns:
        L'indice du minimum dans la tranche l[i:]
    """
    mini = ind
    for i in range(ind, len(l)):
        if l[i] < l[mini]:
            mini = i
    return mini

def tri_selection(l : list[int]):
    """Tri l dans l'ordre croissant numérique selon l'algorithme du tri sélection

    Args:
        l: Une liste d'entiers

    Returns:
        La liste l triée
    """
    for i in range(len(l)):
        ind_min = selection_min(l, i)
        l[ind_min], l[i] = l[i], l[ind_min]

    return l

#################
# TRI INSERTION #
#################


def insert(l : list[int], i : int):
    """Insert l'élément d'indice i à sa place dans la tranche l[:i]

    Args:
        l: Une liste d'entiers
        i: L'indice de l'élément à insérer
    """
    el = l[i]
    place = i
    while place >= 1 and el < l[place-1]:
        l[place] = l[place-1]
        place = place - 1
    l[place] = el


def tri_insertion(l : list[int]):
    """Tri l dans l'ordre croissant numérique selon l'algorithme du tri insertion

    Args:
        l: Une liste d'entiers

    Returns:
        La liste l triée
    """
    for i in range(len(l)):
        insert(l, i)
    return l



##############
# TRI FUSION #
##############


def separe(l : list[int]) -> tuple[list]:
    """Coupe l en deux sous-listes et renvoie le tuple composé de ces deux sous listes

    Args:
        l: une liste d'entier

    Returns:
        Le tuple composé de l1 et l2 tel que la concaténation de l1 et l2 vaut l
        
    """
    if len(l) == 0:
        return ([], [])
    elif len(l) == 1:
        return ([l[0]], [])
    else:
        m = len(l) // 2       
    
        # return (l[:m], l[m:]) 

        # le slicing(utilisation des tranches) n'est pas exigé dans le programme de terminale 
        # il est possible d'utiliser les lignes de code suivantes qui font le même travail
        
        l_gauche = [l[i] for i in range(m)]
        l_droite = [l[i] for i in range(m, len(l))]
        return (l_gauche, l_droite)

def fusionne(l1 : list[int], l2 : list[int]) -> list[int]:
    """Renvoie la liste l triée, tel que l est la fusion de l1 et l2

    Args:
        l1: Une liste d'entier
        l2: Une liste d'entier

    Returns:
        La fusion de l1 et l2
    """
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    else:
        tete_l1 = l1.pop(0)
        tete_l2 = l2.pop(0)
        if tete_l1 < tete_l2:
            return [tete_l1] + fusionne(l1, [tete_l2] + l2)
        else:
            return [tete_l2] + fusionne([tete_l1] + l1, l2)
        
        # if l1[0] < l2[0]:
        #     return [l1[0]] + fusionne(l1[1:], l2)
        # else:
        #     return [l2[0]] + fusionne(l1, l2[1:])
        

def tri_fusion(l : list[int]) -> list[int]:
    """Tri l dans l'ordre croissant numérique selon l'algorithme du tri fusion 

    Args:
        l: Une liste d'entiers

    Returns:
        La liste l triée
    """
    if len(l) <= 1:
        return l
    else:
        l1,l2 = separe(l)
        t_l1 = tri_fusion(l1)
        t_l2 = tri_fusion(l2)
        res = fusionne(t_l1, t_l2)
        return res 





if __name__ == "__main__":
    from random import randint
    l = [randint(-20,20) for i in range(9)]
    print(l)
    # print(tri_selection(l))
    # print(tri_insertion(l))
    print(tri_fusion(l))