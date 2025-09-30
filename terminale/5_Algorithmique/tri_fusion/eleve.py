

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
    ...

def tri_selection(l : list[int]):
    """Tri l dans l'ordre croissant numérique selon l'algorithme du tri sélection

    Args:
        l: Une liste d'entiers

    Returns:
        La liste l triée
    """
    ...

#################
# TRI INSERTION #
#################


def insert(l : list[int], i : int):
    """Insert l'élément d'indice i à sa place dans la tranche l[:i]

    Args:
        l: Une liste d'entiers
        i: L'indice de l'élément à insérer
    """
    ...


def tri_insertion(l : list[int]):
    """Tri l dans l'ordre croissant numérique selon l'algorithme du tri insertion

    Args:
        l: Une liste d'entiers

    Returns:
        La liste l triée
    """
    ...



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
    ...

def fusionne(l1 : list[int], l2 : list[int]) -> list[int]:
    """Renvoie la liste l triée, tel que l est la fusion de l1 et l2

    Args:
        l1: Une liste d'entier
        l2: Une liste d'entier

    Returns:
        La fusion de l1 et l2
    """
    ...


def tri_fusion(l : list[int]) -> list[int]:
    """Tri l dans l'ordre croissant numérique selon l'algorithme du tri fusion 

    Args:
        l: Une liste d'entiers

    Returns:
        La liste l triée
    """
    ...





if __name__ == "__main__":
    from random import randint
    l = [randint(-20,20) for i in range(9)]
    print(l)
    # print(tri_selection(l))
    # print(tri_insertion(l))
    # print(tri_fusion(l))
