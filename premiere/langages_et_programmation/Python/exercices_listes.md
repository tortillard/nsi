# Partie 1 -Exercices sur les listes  

## Exercice 1 - Prise en main  
1. Créez une liste contenant des nombres entiers de votre choix et affichez-la.
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

> [!TIP] 
> Il est possible de concaténer 2 listes à  l'aide du symbole `+`  
> Par exemple `[1,2,3] + [4,5,6] = [1,2,3,4,5,6]`  



## Exercice 5  
Ecrivez une fonction qui prend en paramètre une liste de nombres, et qui renvoi une nouvelle liste contenant uniquement les nombres pairs.

## Exercice 6  
Ecrivez une fonction qui prend en paramètre une liste de notes(jusqu'à 20), et qui renvoi la moyenne des notes.

## Exercice 7 
Ecrivez une fonction qui prend en paramètre une liste de bits, représentant un nombre écrit en binaire et donnez sa représentation en décimale.  

## Exercice 8 
Ecrivez une fonction qui prend en paramètre une liste de nombre et qui renvoie le nombre maximum de cette liste

## Exercice 9  
Ecrivez une fonction qui prend en paramètre une liste de nombre `l` et un nombre `n` et qui renvoi le nombre de fois ou `n` est dans `l`. Si `n` n'est pas présent dans `l` on renverra `-1`.  

## Exercice 10 
Ecrivez une fonction qui prend en paramètre une liste de chaine de caractères et qui renvoie une nouvelle liste contenant les chaines de caractères ayant un nombre de voyelles pairs. 

## Exercice 11 
Écrivez une fonction qui prend en paramètre une liste de chaînes de caractères et qui renvoie une nouvelle liste contenant les chaînes de caractères ayant une consonne à chaque indice impair de cette chaîne.

Exemple :
    - Le mot "aliments" sera dans la liste finale car "l", "m", "n" et "s" sont des consonnes.
    - Le mot "alimentation" ne sera pas dans la liste finale car les lettres aux indices impairs sont "l", "m", "n", "a", "i", "n", __or__ "a" et "i" sont des voyelles."  


# Partie 2 -Exercices sur les listes de listes  

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



## Exercice 4  
Vous avez créez une fonction qui récupère le minimum d'une liste (voir __exercice 8__ de la __Partie 1__).
Créez une nouvelle fonction qui prend en paramètre une liste de liste de nombre, et qui renvoie la liste constitué de 2 éléments. Le premier étant le nombre minimum parmis toutes les sous-listes, le deuxième étant l'indice de la sous liste qui contient ce nombre. 
__Votre fonction devra faire appel à la fonction de l'exercice 8.__



## Activité Morpion  

On souhaite représenter le jeux du [Morpion](https://fr.wikipedia.org/wiki/Morpion_(jeu)).    
On considère que la grille est de taille $3 \times 3$.   
On représente la grille de notre jeu par une liste de liste.   
Chaque ligne de la grille du morpion correspond à une liste dans notre liste de listes.     
On utilise le symbole `O` pour représenter un coup joué par le `joueur1` et le symbole `X` pour celui du `joueur2`.     
La partie est terminé si :    
    - 3 symboles sont alignés(verticalement, horizonralement ou diagonalement)    
    - Toutes les cases contiennent un `O` ou un `X`      

1. Créez une fonction `est_termine` qui prend en paramètre une grille de morpion et qui renvoi `True` si la partie est terminée et `False` sinon.      

2. Créez une fonction `place_symbole` qui prend en paramètre :  
   - une grille de morpion  
   - une abscisse  
   - une ordonnée  
   - et un symbole sous la forme d'un caractère   
Et qui renvoi la grille avec le symbole placé aux bonnes coordonnées.  

3. Créez une fonction `morpion` qui lance un jeu du morpion entre 2 joueurs et qui affiche le vainqueur. (indice : la partie continue __tant qu'__\elle n'est pas finit)  
