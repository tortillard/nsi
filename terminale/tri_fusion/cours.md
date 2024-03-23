# Les tris  

## Généralités  
Trier une collection d'objet signifie, les rangées dans un certain ordre selon une fonction de comparaison. 

Exemple :
    - Les mots du dictionnaire sont rangés dans l'ordre croissant selon la fonction de comparaison qui associe lexicographique(alphabétique)
    - Les résultats obtenue d'une compétition de lancer de poids sont obtenue dans l'ordre décroissant selon la fonction de comparaison qui associe l'ordre numérique 

Dans la suite du cours on décide de choisir comme collection, une liste python d'entiers et que le terme _trier_ désigne le tri dans l'ordre croissant selon l'ordre numérique. 

__Rappel des tris de Première__


## Tri sélection  
Principe :  
A chaque étape on à une partie de la liste qui est triée(gauche) et une autre non triée(droite).

- On sélectionne dans la partie non triée l'entier le plus petit. 
- Puis on place cet entier à la fin de la partie triée


```Pseudo
TRI SELECTION 
ENTREE : L, Une liste d'entiers
SORTIE : La liste d'entiers L triée 


POUR i allant de 0 à longueur(L-1)
    
    indice_minimum = selectionne_indice_minimum(L, i)
    echange_valeur(L[i], L[indice_minimum])

RENVOIE L 

```

## Tri insertion  



## Complexité 


## Tri fusion  
