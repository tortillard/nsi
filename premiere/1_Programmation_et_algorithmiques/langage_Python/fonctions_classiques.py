#1. Ecrire une fonction est_present(element, li)
# qui renvoie False si element n'est pas dans li, et qui
# renvoie True si le element est dans li.  

def est_present(element, li):
    """
    Renvoi si element est présent ou non.

    Args : 
        element (any): un élément à chercher dans li
        liste (list): la liste dans laquelle on cherche un élément
    
    Returns:
        bool :  True si element est présent dans liste. False sinon.
    """
    for e in li: 
        if e == element :
            return True
    return False

# 2. Ecrire une fonction recherche_indice_fin(element, li)
# qui renvoie -1 si nombre n'est pas dans li, et qui renvoie
# l'indice de element dans la li, la dernière fois
# où on le rencontre

def recherche_indice_fin(element, li):
    """Renvoi le dernier indice de element dans li

    Args:
        element (any): l'élément dont on cherche le dernier indice
        li (list): la liste dans laquelle on cherche element

    Returns:
        int : -1 si element n'est pas présent, le dernier indice de element dans li sinon.
    """
    ind_fin = -1 
    for i in range(len(li)):
        if li[i] == element:
            ind_fin = i
    return ind_fin



#3. Ecrire une fonction recherche_indice_debut(element, li)
# qui renvoie -1 si nombre n'est pas dans li, et qui renvoie
# l'indice de nombre dans li, la première fois
# où on le rencontre

def recherche_indice_debut(element, li):
    """Renvoi le premier indice de element dans li

    Args:
        element (any): l'élément dont on cherche le premier indice
        li (list): la liste dans laquelle on cherche element

    Returns:
        int : -1 si element n'est pas présent, le premier indice de element dans li sinon.
    """
    for i in range(len(li)):
        if li[i] == element:
            return i
    return -1

#4. Ecrire une fonction occurence(element, li)
# qui renvoie 0 si element n'est pas dans li, et qui sinon
# renvoie l'occurence de element dans li.
# (le nombre de fois ou nombre est dans table)

def occurence(element, li):  
    """Compte le nombre d'occurence de element dans li

    Args:
        element (any ): l'élément dont on cherche le nombre d'occurence
        li (list): la liste dans laquelle on cherche le nombre d'occurence

    Returns:
        int : le nombre d'occurence de element dans li 
    """
    occ = 0
    for e in li:
        if e == element:
            occ = occ + 1
    return occ 


#5.Ecrire une fonction somme(li) qui calcule la somme
# des nombres de li.
def somme(li):
    """Renvoi la somme des nombres dans li

    Args:
        li (list): une liste de nombres

    Returns : 
        int : La somme des nombres dans li  
    """
    som = 0
    for nb in li:
        som = som + nb
    return som


#6.Ecrire une fonction moyenne(li) qui calcule la moyenne
# des éléments de li.  
def moyenne(li):    
    """Renvoi la moyenne des nombres dans li

    Args:
        li (list): une liste de nombres

    Returns : 
        int : La moyenne des nombres dans li  
    """
    som = 0
    for e in li:
        som = som + e
    moy = som / len(li)

    return moy

#7. Ecrire une fonction minimum(li) qui renvoie
# la liste composé du nombre minimum de li et l'indice de ce minimum 

def minimum(li):
    """Renvoi le minimum de li ainsi que son indice

    Args:
        li (list): la liste dans laquelle on cherche le minimum
    
    Returns : 
        list : Le minimum ainsi que son indice
    """
    mini = table[0]
    for i in range(len(table)) :
        if  table[i] <  mini :
# Avec < on repère la première apparition du minimum
# Avec <= on repère la dernière apparition du minimum
            mini = table[i]
            ind_mini = i
    return [mini, ind_mini]


#8. Ecrire une fonction maximum(li) qui renvoie 
# la liste composée du nombre maximum de li et l'indice de ce maximum
  
def maximum(li):
    """Renvoi le maximum de li ainsi que son indice

    Args:
        li (list): la liste dans laquelle on cherche le maximum
    
    Returns : 
        list : Le maximum ainsi que son indice
    """
    maxi = li[0]
    for i in range(len(li)) :
        if li[i] > maxi :
# Avec > on repère la première apparition du maximum
# Avec >= on repère la dernière apparition du maximum
            
            maxi = li[i]
            ind_maxi = i
    return [maxi , ind_maxi]


#9. Ecrire une fonction tout_est_pair(li) qui renvoie 
# True si tout les nombres contenu dans li sont pairs et False sinon. 
# On renvoi True si aucun nombre est présent dans la liste 

def tout_est_pair(li):
    """Renvoi True si tout les nombres de li sont pairs

    Args:
        li (_type_): Une liste de nombre

    Returns:
        bool : True si li est vide ou si tout les nombres de li sont pairs. False sinon
    """
    for nb in li :
        if nb%2 != 0: 
            return False
    return True



# 10. Fonction factorielle : 
#   n! = n*(n-1)*(n-2) *.....*3*2*1
#   5! = 5*4*3*2*1 = 120
#   Par convention 0! = 1
# Ecrire une fonction factorielle(n) qui renvoie la factorielle de n

def factorielle(n):
    """Renvoi la factorielle d'un nombre

    Args:
        n (int): le nombre dont on souhaite avoir la factorielle

    Returns:
        int : la factorielle de n 
    """
    res = 1
    for i in range(1,n+1):
        res =  res * i
    return res  

