# TP1 Boucles - Info sur un nombre

Le but de ce TP est d'écrire une fonction `info_nombre` prenant aucun paramètre mais demande à l'utilisateur de saisir un nombre `n` et qui affiche toutes les informations sur `n` à savoir :  
- la somme des entiers allant jusqu'à `n`  
- la table de multiplication de `n`  
- la factorielle de `n`  
- un triangle sous forme d'étoile de hauteur `n`  

Voici un exemple du résultat attendu pour `n = 5` 

```
Saisissez un nombre : 5

La somme des entiers de 5 est 15

Voici la table de multiplication de 5
0*5=0
1*5=5
2*5=10
3*5=15
4*5=20
5*5=25
6*5=30
7*5=35
8*5=40
9*5=45
10*5=50


La factorielle de 5 est 120


voici le triangle
*
**
***
****
*****
```


## La somme des entiers 
Écrire une fonction `somme_des_entiers` qui prend un entier `n` en paramètre.  
Cette fonction renvoi la somme des entiers allant de `1` à `n` inclus.  


## La table de multiplication  
Écrire une fonction `table_multiplications` qui prend un entier `n` en paramètre.  
Cette fonction affiche ligne par ligne les multiplications allant de `0*n` jusqu'à `10*n`.  

## La factorielle  
La factorielle d'un nombre `x` est le produit des entiers allant de `1` à `x`.
Autrement dit, la __factorielle de 4__ est `24` puisque `1 * 2 * 3 * 4 = 24`.  
Ecrire une fonction `factorielle` qui prend un entier `n` en paramètre et qui renvoie la factorielle de `n`

## Triangle  
Nous allons ici renvoyer un triangle dessiné sous forme de chaine de caractère.  
Ce triangle est dessiné à l'aide du caractère `*`. 
Il se construit en plusieurs _étages_ :
- à l'étage 1 il y a `*` 
- en dessous, à l'étage 2 il y a `**` 
- en dessous, à l'étage 3 il y a `***` 
- ...
- en dessous, à l'étage `n` il y a `*` repété `n` fois.  
 
Ecrire une fonction `triangle_hauteur` qui prend un entier `n` en paramètre et qui renvoie le triangle comme expliqué ci-dessus.  


## Aide pour le TP

> [!TIP] 
> La fonction `input` permet à l'utilisateur de saisir une valeur. Il est possible de récupérer cette valeur dans une variable pour l'utiliser plus tard.  
> Exemple 
> ```Python
> info_saisie = input()
> # On peut également ajouter un message en paramètre de la fonction input 
> age = input("Quel est votre age ?")
> ```
> ⚠️ ATTENTION ⚠️ peu importe le résultat saisi par l'utilisateur, `input` renverra TOUJOURS une chaine de caractères ! 


> [!TIP]  
> La fonction `str` permet de convertir un type en chaine de caractère. Cela est utile notamment pour concaténer des caractères avec des nombres.  
> Par exemple : 
> ```Python
> age = 16  
> # L'exemple ci dessous ne fonctionne pas 
> print("J'ai " + age + "ans et l'année prochaine j'aurais " + age + 1 + " ans")
>
> # L'exemple ci dessous fonctionne
> print("J'ai " + str(age) + "ans et l'année prochaine j'aurais " + str(age + 1) + " ans")
> ```

> [!TIP]  
> De la même manière que la fonction `str` il existe la fonction `int` qui permet de convertit un objet sous forme d'entier.  
> Par exemple : 
> ```Python
> mot = "16"
> nombre = int(mot)
> ```

