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
    
    indice_minimum = selectionne_indice_minimum(L, i)    # Récupère l'indice de l'élement minimum à partir de l'indice i  
    echange_valeur(L, L[i], L[indice_minimum])   # Permutte les éléments situés aux indices i et indice_minimum de L

RENVOIE L 

```

### Activité 
Programmer le tri sélection en python. 


## Tri insertion  

Principe :  

A chaque étape on à une partie de la liste qui est triée(gauche) et une autre non triée(droite).

- On prends le premier entier de la partie non triée. 
- Puis on le place au bon endroit dans la partie triée.


```Pseudo
TRI INSERTION 
ENTREE : L, Une liste d'entiers
SORTIE : La liste d'entiers L triée 


POUR i allant de 0 à longueur(L-1)
    
    insert(L, i)     # insert l'élément d'indice i dans la partie triée de L

RENVOIE L 

```
### Activité 
Programmer le tri insertion en python. 




## Complexité 

La complexité(ou coût) d'un algorithme est une mesure permettant d'indiquer la quantité de ressource nécessaire d'un algorithme.  
Par ressource on entends principalement soit le _temps_ d'éxécution d'un algorithme ou la place _mémoire_ qu'il occupe. 

- La complexité en __espace__ va compter l'espace mémoire utilisé par un algorithme
- La complexité en __temps__ va compter le temps d'exécution d'un algorithme, relativement aux opérations élémentaires. 

On se contentera uniquement de calculer la complexité en temps.   

Afin d'exprimer la complexité en temps, on compte le nombre d'opérations élémentaire d'un algorithme.    
Les __opérations de comparaison__ (`==`,`!=`,`<`,`<=`,`>`,`>=`) sont les plus significative c'est donc celles ci qui nous intéresserons pour déterminer le coût d'un algorithme.   

### Notations   
La complexité d'un algorithme s'exprime en fonction __de la taille des données d'éntrées__.   
Dans notre cas la donnée d'entrée est la liste. Généralement on utilise `n` pour désigner la taille d'un objet.  

Lorsque l'on compte le nombre d'opération, on simplifie la notation en admettant comme complexité __le plus gros exposant__ compté.  

Par exemple :  
- Si on effectue une comparaison pour chaque donnée de la liste, on compte `n`comparaisons on notera : `O(n)`   
- Si on effectue deux comparaison pour chaque donnée de la liste, on compte `2n`comparaisons on notera : `O(n)`   
- Si on effectue 2n comparaison pour chaque donnée de la liste, on compte `2n²`comparaisons on notera : `O(n²)`   


### Activité   
1. Calculer la complexité du tri sélection  
2. Calculer la complexité du tri insertion  



## Tri fusion  

