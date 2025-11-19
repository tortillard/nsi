# Exercices - Récursivité  

## Exercice 1  
Ecrire une fonction récursive `somme_n(n)` qui renvoi la somme des entiers allant de `1` à `n`. Le code assurera que n est supérieur ou égal à 0.     
Par exemple, `somme_n(3)` renvoi `6`

## Exercice 2  
Ecrire une fonction récursive `punition(nb, texte)` qui prend en paramètre un entier positif `nb` et une chaine de caractère `texte` et renvoi une chaine de caractère constitué de `texte`, `nb` fois.    
On rappel que l'affichage du caractère `\n` permet de sauter une ligne.  

Le code `print(punition(5, "je dois écouter en cours"))` doit renvoyer :
```
je dois écouter en cours
je dois écouter en cours
je dois écouter en cours
je dois écouter en cours
je dois écouter en cours
```

## Exercice 3  
Ecrire une fonction récursive `somme_liste(l)` qui prend en paramètre une liste d'entier `l` et renvoi la somme de ces nombres.  
On rappel qu'il est possible de récupérer des 'tranches'(slices) d'une liste avec les instructions suivantes :
- `l[x:y]` : renvoi la liste `l` constitué des éléments allant de l'indice `x` à `y-1`.    
- `l[x:]` : renvoi la liste `l` constitué des éléments allant de l'indice `x` jusqu'à la fin de la liste.      
- `l[:y]` : renvoi la liste `l` constitué des éléments allant de l'indice `0` jusqu'à `y-1`  

`somme_liste([3,9,2,11])` doit renvoyer `25`.

## Exercice 4  
On cherche à écrire une fonction récursive `fibo(n)`, qui renvoi le résultat de la suite de fibonacci au rang `n`.  

Voici comment est définie la suite de Fibonacci : 
- Si n = 0 ou 1 on renvoie n 
- Sinon F(n) = F(n-1) + F(n-2)

Voici les premiers termes de la suite de Fibonacci :
|   n   | fibo(n) |
| :---: | :-----: |
|   0   |    0    |
|   1   |    1    |
|   2   |    1    |
|   3   |    2    |
|   4   |    3    |
|   5   |    5    |
|   6   |    8    |

 
## Exercice 5  
Écrire une fonction récursive `retourne(chaine)` qui renvoie le retournement d'une chaine de caractères.  
Par exemple, `retourne("Salut")` renvoi `"tulaS"`

## Exercice 6  
Compléter la fonction récursive ci-dessous. 

```Python
def est_pair(n):
    """
    Renvoie True si n est pair, False sinon
    CU: n >= 0
    Exemple :
    >>> est_pair(1)
    False
    >>> est_pair(6)
    True

    """
    assert n >= 0 ,'n doit être positif ou nul'
    ...

```

