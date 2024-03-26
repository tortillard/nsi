# Exercices  

## Exercice 1  
1. Dessiner tous les graphes non orientés ayant exactement 3 sommets. 
2. Combien y a-t-il de graphe orientés ayant exactement trois sommets ?

## Exercice 2  
![](img/exo_2_graphe_non_oriente.png)
Donner pour ce graphe:  
1. Le nombre de sommets  
2. Le degré du sommet A  
3. 3 chemins différents allant de A à F   
4. Un cycle commençant  par le sommet F  
5. Représenter ce graphe sous forme de matrice d'adjacence  

## Exercice 3  
![](img/exo_3_graphe_oriente.jpg)
Donner pour ce graphe:
1. Le nombre de sommets  
2. Le degré sortant du sommet 8  
3. Le degré entrant du sommet 5
4. Les chemins allant de 1 à 5   
5. Un cycle commencant par le sommet 3  
6. Représenter ce graphe sous forme de listes d'adjacences  

## Exercice 4  
On décide de représenter un réseau routier sous forme de graphe afin d'avoir une visualisation des routes entre les villes.  
On considères que chaque route ne peut être empruntée que dans 1 sens.   
Il existe une route entre Arras et Beaurains et une route allant de Duisans à Beaurains.
Depuis Beaurains, 3 autres routes sont disponibles, une pour aller à Croisilles, une autre à Duisans et enfin une à Eterpigny.  
On peut aller de Fampoux à Duisans et d'Eterpigny à Fampoux.  
Enfin, il existe une route de Gavrelle à Arras et de Croisilles à Gavrelle.  

1. Dessiner le graphe correspondant à cette description  
2. Donner le nom de 2 villes adjacentes dans ce graphe  
3. Est-il possible d'aller d'Arras à Eterpigny ? De Duisans à Croisilles ? De Croisilles à Gavrelle ? Pour chaque réponse donnée la liste des villes empruntées si c'est possible


## Exercice 5
Programmer la fonction `nb_sommets(g)` prenant en paramètre un graphe sous forme de listes d'adjacences et qui renvoie le nombre de sommet de g. 


## Exercice 6
Programmer la fonction `nb_aretes(g)` prenant en paramètre un graphe(orienté) sous forme de listes d'adjacences et qui renvoie le nombre d'arêtes de g. 


## Exercice 7
Programmer la fonction `degre(g, s)` prenant en paramètre un graphe sous forme de listes d'adjacences et qui renvoie le degré du sommet `s`


## Exercice 8
Programmer la fonction `adjacences_to_matrice(g)` prenant en paramètre un graphe sous forme de listes d'adjacences et qui renvoie le graphe représenté sous forme de matrice d'adjacence constituée de 0 et de 1.



## Exercice 9 
Programmer la fonction `parcours_profondeur(g, s)` prenant en paramètre un graphe sous forme de listes d'adjacences et qui renvoie un parcours en profondeur des sommets de `g` à partir de `s`

## Exercice 10 
Programmer la fonction `parcours_largeur(g, s)` prenant en paramètre un graphe sous forme de listes d'adjacences et qui renvoie un parcours en largeur des sommets de `g` à partir de `s`
