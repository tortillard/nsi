# TP2 : Python représentation des textes en machine  


## Généralités sur les chaines de caractères en Python  

> [!TIP]  
> Les chaines de caractères sont définies par le type `str` en Python.  
> On créer une chaine de caractères avec des guillemets simple `' '` ou double `" "`.  

> [!TIP]  
> La longueur d'une chaine de caractères s'obtient avec la fonction `len`.  
> Par exemple :  
> - `len("")` renvoi `0`  
> - `len("a")` renvoi `1`   
> - `len("m1@ou")` renvoi `5`    

> [!TIP]  
> La fonction `str` permet de caster(ou transtyper) en chaine de caractères.
> Par exemple :
> - `str(1234)` renvoi `"1234"`  

## Q1  
Déclarez une variable `c1` dans laquelle vous stockerez la chaine de caractère de votre choix.  
Renvoyez la longueur de cette chaine.  

## Q2  
Déclarez une variable `n1` dans laquelle vous stockerez le nombre de votre choix.   
Changer le type de `n1` afin qu'il passe de `int` à `str`, stocker ce résultat dans `c2`.   


> [!TIP] 
> Les chaines de caractères sont des séquences, il est donc possible d'accéder à 1 caractère par son indice. 
> On accède, au caractère d'indice `i` en notant `chaine[i]`.  
> Par exemple :  
> On considère la chaine `mot = 'Kaizoku'`, `mot[3]` renvoi `"z"`. 

> [!TIP] 
> Il est également possible d'accéder à des morceaux d'une chaine de caractères.  
> On accède, au morceau commencant à l'indice `i` jusqu'à l'indice `j` en notant `chaine[i:j+1]`.  
> Par exemple :  
> On considère la chaine `mot = 'Kaizoku'` et on souhaite avoir le morceau de la chaine `"zok"`.  
> `"z"` est à l'indice 3  
> `"k"` à l'indce 5  
> Il faut donc noter `mot[3:6]` pour renvoyer  `"zok"`.  

> [!TIP] 
> Pour rappel,
> - il est possible de concaténer 2 chaines de caractères avec l'opérateur `+`
> - il est possible de répéter 2 chaines de caractères avec l'opérateur `*`


## Q3  
Reprenez la variable `c1` de la __Q1__ et renvoyez le 4ème caractère de cette chaine.   
Si nécessaire, modifiez `c1` afin que la question soit réalisable.  

## Q4    
Reprenez la variable `c1` et renvoyez le morceau de votre choix de cette chaine de caractère. 

## Q5 
Concaténer `c1` et `c2`.  
Répéter la chaine `c2` autant de fois que `n1`.  


> [!TIP] 
> Il est possible de récupérer le point de code Unicode d'un caractère avec la fonction `ord` en Python.
> Réciproquement la fonction `chr` donne le caractère Unicode correspondant au point de code entré.  
> Par exemple :   
> `ord('T')` renvoi `84`    
> `chr(84)` renvoi `'T'`  

> [!TIP] 
> La comparaison entre 2 chaines de caractères se fait en comparant le point de code des premiers caractères, s'ils sont égaux on compare les deuxième et ainsi de suite...  
> Par exemple :  
> `"alice" < "bob"` renvoi `True`  
> `"alice" < "Alice"` renvoi `False`  
> `"@" <= "{"` renvoi `True`  
> `"3" <= "121"` renvoi `False`    


## Q6  
Créer une fonction `est_ascii` qui prend comme paramètre `caractere`. 
Cette fonction renvoi `True` si `caractere` est un caractère de la table `ASCII` et `False` sinon. 

Exemples :
- `est_ascii("A")` renvoi `True`  
- `est_ascii("@")` renvoi `True`  
- `est_ascii("~")` renvoi `True`  
- `est_ascii("é")` renvoi `False`  


> [!TIP]
> Il existe une méthode `encode` qui permet d'encoder une chaine de caractères en octets en Python. 
> Par défaut lorsqu'on ne précise pas l'encodage elle le fait en utf-8. Mais il est possible de préciser l'encodage `'ascii'` ou `'latin1'`.  
> Note : les chaines d'octets se distingue par le 'b' situé au début de la chaine de caractères.  
> Par exemple :
> - `"accentuâmes".encode()` renvoi `b'accentu\xc3\xa2mes'`
> - `"accentuâmes".encode("latin1")` renvoi `b'accentu\xe2mes'`

## Q7  
Créer une fonction `transformation` qui prend en paramètre `chaine` qui correspond à une chaine de caractères et `codage` un caractère.  
Et qui affiche l'encodage de `chaine` selon `codage`.  
Si `codage` vaut `"L"` cela signifie qu'on souhaite utiliser le système d'encodage `"latin1"`.  
Si `codage` vaut `"A"` c'est la même chose mais pour l'`"ascii"`  
Dans tout les autres cas ce sera l'`"utf-8"`.  

Par exemple : 
-`transformation("été", "L")` renvoi `"b'\xe9t\xe9'"`  
-`transformation("été", "A")` renvoi Une erreur   
-`transformation("été", "bidule")` renvoi `b'\xc3\xa9t\xc3\xa9'`  


> [!TIP]
> Pour décoder une chaine d'octets(comme celle renvoyé par la méthode `encode`) il existe la méthode réciproque `decode` qui a partir d'une chaine d'octets renvoi la chaine de caractères. 
> Par exemple :  
> - `"b'\xc3\xa9t\xc3\xa9'".decode()` renvoi `"été"`  

## Q8 
Créer une fonction `retransformation` qui prend en paramètre `chaine_octet` qui correspond à une chaine d'octet et `codage` un caractère. 
Cette fonction est la réciproque de `transformation`.  

Voici des exemples de ce qu'elle doit renvoyer.  
- `retransformation(b'o\xf9', "L")` renvoi `"où"`  
- `retransformation(b'\xc3\xa9t\xc3\xa9', "truc")` renvoi `"été"`  





