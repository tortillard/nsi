def echange(l, i, j):
    """Echange l[i] et l[j] de place

    Args:
        l (list): Une liste de nombres
        i (int): Un indice compris entre 0 et len(l)-1
        j (int): Un indice compris entre 0 et len(l)-1
    
    Rrturns :
        None
    """
    l[i], l[j] = l[j], l[i]



# TRI selection 

def selection_minimum(l, ind):
    """Renvoie l'indice du minimum se situant entre les indices ind et len(l)-1

    Args:
        l (list): Une liste de nombres
        ind (ind): Un indice compris entre 0 et len(l)-1

    Returns:
        int : L'indice du minimum se situant entre les indices ind et len(l)-1
    """
    ind_minimum = ind
    for ind_nombre_parcrouru in range(ind, len(l)):
        
        if l[ind_nombre_parcrouru] < l[ind_minimum]:
            ind_minimum = ind_nombre_parcrouru

    return ind_minimum

def tri_selection(l):
    """Renvoie la liste l triée dans l'ordre croissant en utilisant le tri par sélection du minimum

    Args:
        l (list): Une liste de nombres

    Returns:
        list: La liste l triée dans l'ordre croissant
    """
    for place_du_minimum in range(len(l)):
        indice_minimum = selection_minimum(l, place_du_minimum)
        # l[place_du_minimum], l[indice_minimum] = l[indice_minimum],  l[place_du_minimum]
        echange(l, place_du_minimum, indice_minimum)
    return l

# TRI insertion

def inserer(l,i):
    """Insère le nombre à l'indice i dans l, entre les indices 0 et i pour que cette partie de la liste soit triée.

    Args:
        l (list): Une liste de nombres
        i (int): Un indice compris entre 0 et len(l)-1

    Returns : 
        None
    """
    ind_nb_a_inserer = i
    
    while l[ind_nb_a_inserer-1] > l[ind_nb_a_inserer] and i!= 0 :
        
        echange(l, ind_nb_a_inserer-1, ind_nb_a_inserer)
        ind_nb_a_inserer = ind_nb_a_inserer - 1


def tri_insertion(l):
    """Renvoie la liste l triée dans l'ordre croissant en utilisant le tri par insertion

    Args:
        l (list): Une liste de nombres

    Returns:
        list: La liste l triée dans l'ordre croissant
    """
    for i in range(1, len(l)):
        inserer(l, i)
    return l 




# Tri insertion dichotomique 

def trouve_ind_dicho(l, i):
    """Renvoie l'indice auquel l[i] doit être inséré pour que la partie de l se trouvant entre l'indice 0 et i-1 soit triée.
    Cet indice est trouvé grâce à la recherche dichotomique

    Args:
        l (list): Une liste de nombres
        i (int): Un indice compris entre 0 et len(l)-1

    Returns:
        int : L'indice où doit être placé l[i]

    """
    
    ind_debut = 0
    ind_fin = i
    element = l[i]
    
    while ind_debut < ind_fin:
	
        ind_milieu = (ind_debut + ind_fin) // 2
        milieu = l[ind_milieu]
		
        if milieu < element:
        	ind_debut = ind_milieu + 1
        else:
            ind_fin = ind_milieu 
    
    return ind_debut


def insere_dicho(l, ind_element_a_deplacer):	
    """Insère le nombre à l'indice ind_element_a_deplacer dans l, entre les indices 0 et ind_element_a_deplacer pour que cette partie de la liste soit triée.
    La position est trouvée à l'aide de la recherche dichotomique.  

    Args:
        l (list): Une liste de nombres 
        ind_element_a_deplacer (int): Un indice compris entre 0 et len(l)-1
    """
    ind_dicho = trouve_ind_dicho(l, ind_element_a_deplacer)
    for i in range(ind_element_a_deplacer, ind_dicho, -1 ):
        echange(l, i, i-1)
		 

def tri_insertion_dicho(l):
    """Renvoie la liste l triée dans l'ordre croissant en utilisant le tri par insertion et la recherche dichotomique

    Args:
        l (list): Une liste de nombres

    Returns:
        list: La liste l triée dans l'ordre croissant
    """
    for i in range(len(l)):
        insere_dicho(l, i)
    return l 



if __name__ == "__main__":
    from random import randint
    
    l = [randint(-10,10) for i in range(5)]
    print(tri_selection(l))
    print(tri_insertion(l))
    print(tri_insertion(l))
        

