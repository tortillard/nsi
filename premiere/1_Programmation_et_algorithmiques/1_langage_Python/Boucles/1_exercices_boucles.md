# Partie - 1 : Exercices sur les boucles non bornée 
Chaque exercice dans cette partie est à réalisé avec une boucle non bornée(une boucle `while`).  


## Exercice 1 
Écrire une fonction `compte` qui prend en paramètre un entier `borne` et qui affiche ligne par ligne tout les nombres entiers compris entre 0 et `borne` inclus.   

Par exemple, `compte(4)` affiche 
```
0
1
2
3
4
```

## Exercice 2  
Écrire une fonction `epele` qui prend en paramètre une chaine de caractères `chaine` et qui affiche ligne par ligne tout les caractères compris dans `chaine`.   

Par exemple, `epele("salut")` affiche 
```
s
a
l
u
t
```

> [!TIP]
> Pour rappel, il est possible d'accéder à un caractère d'une chaine en utilisant des crochets et l'indice du caractère souhaité.  
> Par exemple 
> ```Python 
> phrase = "Bonjour tout le monde"  
> troisieme_lettre = phrase[2]  
> ```

## Exercice 3  
Écrire une fonction `possede_espace` qui prend en paramètre une chaine de caractères `chaine` et qui renvoi `False` si aucun espace `" "` est présent dans `chaine`, `True` sinon.  

Exemples : 
- `possede_espace("C'est une belle journée")` renvoi `True`.   
- `possede_espace("Parfum")` renvoi `False`.   


## Exercice 4   

Écrire une fonction `pair_impair` qui prend en paramètre une chaine de caractère composé uniquement de chiffres nomée `str_chiffres`.  
Cette fonction parcours la chaine de caractère un par un et :  
- affiche `pair !` quand le caractère parcouru est un chiffre pair   
- affiche `impair !` quand le caractère parcouru est un chiffre impair   

Par exemple, `pair_impair("25741")` affiche
`̀``
0
1
1
0
1
`̀``

## Exercice 5  
Écrire une fonction `verif_1243` qui ne prend pas de paramètre et demande à un utilisateur d'entrer un nombre jusqu'à ce qu'il soit égal à `1243` si le nombre entré ne correspond pas on affiche `"Mauvais nombre !"`.  


# Partie - 2 : Exercices sur les boucles bornée  
Chaque exercice dans cette partie est à réalisé avec une boucle bornée(une boucle `for`).    

## Exercice 1  
Refaire les exercices 1, 2, 3 et 4 de la __Partie 1__.    

## Exercice 2  
Refaire l'exercice 5 de la __Partie 1__.  
Que remarquez vous ?   


