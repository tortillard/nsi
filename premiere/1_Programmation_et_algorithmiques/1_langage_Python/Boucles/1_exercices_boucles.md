# Partie - 1 : Exercices sur les boucles non bornée 
Chaque exercice dans cette partie est à réalisé avec une boucle non bornée c'est à dire une boucle utilisant le mot clé `while`.  

## Exercice 1 
Écrire une fonction `compte` qui prend en paramètre un entier `borne` et qui affiche ligne par ligne tout les nombres entiers compris entre 0 et `borne` inclus.   

## Exercice 2  
Écrire une fonction `epele` qui prend en paramètre une chaine de caractères `chaine` et qui affiche ligne par ligne tout les caractères compris `chaine` .   

> [!TIP]
> Pour rappel il est possible d'accéder à un caractère d'une chaine en utilisant des crochets et l'indice du caractère souhaité.  
> Par exemple 
> ```Python 
> phrase = "Bonjour tout le monde"  
> troisieme_lettre = phrase[2]  
> ```

## Exercice 3  
Écrire une fonction `possede_espace` qui prend en paramètre une chaine de caractères `chaine` et qui renvoi `False` si aucun espace `" "` est présent dans `chaine`, `True` sinon.  

Exemple : 
- `possede_espace("C'est une belle journée")` renvoi `True`.   
- `possede_espace("Parfum")` renvoi `False`.   

## Exercice 4  

> Il n'est pas nécessaire d'utiliser une boucle pour cet exercice.  

En utilisant les fonctions des exercices 1, 2 et 3 écrivez une fonction `choix` qui prend en paramètre une chaine de caractères `chaine`.  

Elle _comptera_ le nombre de lettre présentes dans `chaine` si `chaine` ne possèdent pas d'espace. Sinon elle _epelera_ chaque lettre.  

# Partie - 2 : Exercices sur les boucles bornée  
Chaque exercice dans cette partie est à réalisé avec une boucle non bornée c'est à dire une boucle utilisant le mot clé `for`.  

## Exercice 1  
Faites les exercices 1, 2 et 3 de la partie 1.  

## Exercice 2  
Reprenez la fonction `choix` de l'exercice 4 de la partie 1.
Faites le nécessaire pour que `choix` fasse appel aux fonction de l'exercice précédent.  
