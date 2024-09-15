# Les conditions  

## Explication  
Dans beaucoup de langages de programmation, il existe des __instructions conditionnelles__.    


Les conditions permettent d'exécuter différents blocs de code selon si une condition est satisfaite ou non(si elle vaut `True` ou `False`).

Cela permet entre autres de résoudre des problèmes qui nécessitent de traiter différents cas.   

Par exemple, si on souhaite écrire le programme d'une caisse automatique d'un supermarché qui associe le code barre d'un article à son nom en français.  
On a bien plusieurs articles à distinguer, il nous faut donc utiliser __des conditions__ pour résoudre ce problème.  


Voici un programme en pseudo-code qui peut répondre à ce problème.
```Pseudo  
code_barre = scanner.bip()

SI code_barre = "019381" :
    afficher "Pommes"

SINON SI code_barre = "28984" :
    afficher "Limonade"

SINON SI code_barre = "753989" :
    afficher "Brioche"

SINON SI code_barre = "142356" :
    afficher "Thé"

SINON 
    afficher "Nom d'article inconnu" 
```

## Utilisation des conditions en Python  

En Python, on définit une condition de la manière suivante :
    - On utilise le mot-clé `if` (traduit par le "si" conditionnel)   
    - Suivi d'une instruction qui renvoie un booléen, souvent une condition    
    - On termine en notant `:` à la fin de la ligne   
    - Puis on passe une ligne et on appuie sur la touche tabulation pour indenter  
    - Enfin on écrit le code qu'on souhaite exécuter si l'instruction booléenne vaut `True`  

Voici un exemple d'utilisation 
```Python  
age = 12
if age <= 15 :
    print("Collège")
```

Le programme suivant affiche `Collège` puisque la condition est satisfaite, c'est-à-dire qu'elle renvoie `True`.    


Il est également possible de multiplier les conditions dans un programme.    

Par exemple :   

```Python  
age = 12
if age <= 15 :
    print("Collège")

if age == 15 :
    print("Troisieme")

if age == 14 :
    print("Quatrième")

if age == 13 :
    print("Cinquième")

if age == 12 :
    print("Sixième")
```


Ce programme affiche les lignes suivantes :
```
Collège  
Sixième  
```
Il regarde chaque condition et exécute les blocs de code associés.  

Cette structure de programme n'est pas la plus utilisée.    


## Utilisation d'elif  
Une autre structure est plus utilisée après l'utilisation de `if` il s'agit de l'utilisation du mot clé `elif` (qui peut se traduire par "sinon si ..").  
Le mot clé `elif` a pour but de distinguer les cas et d'exécuter uniquement un bloc de code parmi toutes les conditions.  
Autrement dit, si on écrit le même code que précédemment en utilisant des `elif` à la place de tous les `if` (excepté le premier).  

```Python  
age = 12
if age <= 15 :
    print("Collège")

elif age == 15 :
    print("Troisieme")

elif age == 14 :
    print("Quatrième")

elif age == 13 :
    print("Cinquième")

elif age == 12 :
    print("Sixième")
```
Ce programme affichera uniquement `Collège`. Pourquoi ?   
La première condition est satisfaite, on exécute donc le bloc de code qui lui est associé.  
Comme les conditions qui suivent sont des `elif`, aucun autre bloc de code sera exécuté même si la condition `age == 12` est satisfaite par exemple.    




## Utilisation de else  

On peut se poser la question de savoir ce qu'il se passe si eon reprend le même programme en changeant la valeur de la variable `age = 17`.  
Si c'est le cas, aucune condition n'est satisfaite.   
Le programme affiche uniquement un message si `age` vaut au moins `15`, le programmeur n'a pas pensé à afficher un message pour __tous les autres cas__.  

C'est le mot clé `else` (qui peut se traduire par sinon ..) qui permet d'exécuter un bloc de code dans le cas où toutes les conditions précédentes du code n'ont pas été satisfaites.     

Voici un exemple d'utilisation de `else` en reprenant le programme précédent.    
```Python  
age = 20
if age <= 15 :
    print("Collège")

elif age == 15 :
    print("Troisieme")

elif age == 14 :
    print("Quatrième")

elif age == 13 :
    print("Cinquième")

elif age == 12 :
    print("Sixième")

else: 
    print("Pas collège")
```

Ce programme affiche `Pas collège`.   
Aucune condition n'est satisfaite, c'est donc le bloc de code de `else` qui est exécuté.  

On peut évidemment utiliser l'instruction `else` sans qu'il y ait d'instruction `elif`.  
Par exemple :
```Python
age = 13
if age <= 15:
    print("Collège")
else:
    print("Pas au collège")
```  

> - [!WARNING] Il n'est pas possible d'utiliser `elif` ou `else` avant d'avoir utilisé au moins une condition avec un `if` auparavant