# Exercices sur les listes  

## Exercice 1 - Prise en main  
1. Créez une liste contenant les cinq premiers nombres entiers (0 à 4) et affichez-la.
2. À partir de la liste créée à l'exercice 1, affichez le premier et le dernier élément.
3. Modifiez le troisième élément de la liste pour qu'il soit égal à 10, puis affichez la liste mise à jour.
4. Ajoutez le nombre 5 à la fin de la liste et affichez la liste.
5. Affichez la longueur de la liste après toutes les modifications.
6. Utilisez une boucle for pour afficher chaque élément de la liste sur une nouvelle ligne(avec `print()`).




## Exercice 2  
Écrivez une fonction qui prend une liste et un élément en paramètres et retourne `True` si l'élément est dans la liste, sinon `False`.  


## Exercice 3  
Ecrivez une fonction qui prend en paramètre une liste de nombres, et qui renvoi une nouvelle liste contenant uniquement les nombres supérieurs à 5.  

## Exercice 4  
Créez deux listes et concaténez-les pour en former une nouvelle liste, puis affichez la liste résultante.

> [!TIP] Il est possible de concaténer 2 listes à  l'aide du symbole `+`
> Par exemple `[1,2,3] + [4,5,6] = [1,2,3,4,5,6]`  


## Exercice 5  
Ecrivez une fonction qui prend en paramètre une liste de nombres, et qui renvoi une nouvelle liste contenant uniquement les nombres pairs.

## Exercice 6  
Ecrivez une fonction qui prend en paramètre une liste de notes(jusqu'à 20), et qui renvoi la moyenne des notes.

## Exercice 7 
Ecrivez une fonction qui prend en paramètre une liste de bits, représentant un nombreécrit en binaire et donnez sa représentation en décimale.  

# Exercices sur les listes de listes  

## Exercice 1  - Prise en main 

1. Créez une liste qui contient le nom de 3 fruits, une deuxième liste qui contient le nom de trois légumes.  
2. Créez une liste `magasin` qui contient les deux listes précédentes.  
3. À partir de la liste `magasin` affichez le deuxième fruit et le premier légume.  
4. Modifiez le nom du troisième légume dans `magasin` pour qu'il soit "carotte", puis affichez la liste mise à jour.  
5. Ajoutez un nouveau fruit à la liste des fruits et affichez `magasin`.  
6. Affichez la longueur de la liste des fruits et celle de la liste des légumes.  
7. Utilisez une boucle `for` pour afficher chaque fruit et chaque légume.

## Exercice 2

Créez 3 listes représentant les notes de 3 élèves.    
Chaque liste doit contenir 4 notes.  
Créez une liste `classe` qui contient les 3 listes précédentes.  
Votre programme doit afficher toutes les notes en dessous de 10(exclus) de la liste `classe`.  

## Exercice 3    

Reprenez la liste `classe` de l'exercice précédent.    
Créez un programme qui renvoi la liste contenant la moyenne des notes pour chaque élève.  


## Exercice 4 - Activité Morpion  

On souhaite représenter le jeux du [Morpion](https://fr.wikipedia.org/wiki/Morpion_(jeu)).    
On considère que la grille est de taille $3 \times 3$.   
On représente la grille de notre jeu par une liste de liste.   
Chaque ligne de la grille du morpion correspond à une liste dans notre liste de listes.     
On utilise le symbole `O` pour représenter un coup joué par le `joueur1` et le symbole `X` pour celui du `joueur2`.     
La partie est terminé si :    
    - 3 symboles sont alignés(verticalement, horizonralement ou diagonalement)    
    - Toutes les cases contiennent un `O` ou un `X`      

1. Créez une fonction `est_termine` qui prend en entrée une grille de morpion et qui renvoi `True` si la partie est terminée et `False` sinon.    
2. Créez une fonction `morpion` qui lance un jeu du morpion entre 2 joueurs et qui affiche le vainqueur. (indice : la partie continue _tant qu'_elle n'est pas finit)  
