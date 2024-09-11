# Type de base et opérateurs


## Rappel : les types de base  

|       Français        | Anglais  | Python  |    Exemples de valeurs     |
| :-------------------: | :------: | :-----: | :------------------------: |
|    Nombres entiers    | Integer  |  `int`  |        `4` ou `-7`         |
|    Nombre décimaux    | Floating | `float` |      `9.3` ou `-11.0`      |
| Chaines de caractères |  String  |  `str`  | `"Hello"` ou `'@kwm78E-$'` |
|        Booléen        | Boolean  | `bool`  |     `True` ou `False`      |

> Il existe d'autres types qui seront vus plus tard en NSI. 

## Opérateurs arithmétiques
Ces opérateurs s'utilisent avec des `int` et des `float`  
| Python |              Français               |
| :----: | :---------------------------------: |
|  `+`   |              Addition               |
|  `-`   |            Soustraction             |
|  `*`   |           Multiplication            |
|  `**`  |              Puissance              |
|  `/`   |              Division               |
|  `//`  | Quotient de la division euclidienne |
|  `%`   |  Reste de la division euclidienne   |




## Opérateur sur les chaînes de caractères
| Python |   Français    |    Exemple     | Résultat  |
| :----: | :-----------: | :------------: | :-------: |
|  `+`   | Concaténation | "Bon" + "jour" | "Bonjour" |



## Opérateurs booléens  

### Opérateur NOT 

L'opérateur __NOT(NON)__ est un opérateur _unaire_ (qui agit sur _une seule_ variable). Il a pour effet d'inverser la valeur logique de la variable sur laquelle il agit.

|   a   | NOT a |
| :---: | :---: |
| Faux  | Vrai  |
| Vrai  | Faux  |

En Python, l'opérateur logique __NOT__ s'écrit __not__.


### Opérateur AND
L'opérateur __AND(ET)__ est un opérateur binaire (qui agit sur deux variables). Il a la valeur logique __Vrai__ si et seulement si les deux variables sont __Vrai__. 

|    a     |    b     | a AND b  |
| :------: | :------: | :------: |
|   Faux   |   Faux   |   Faux   |
|   Faux   |   Vrai   |   Faux   |
|   Vrai   |   Faux   |   Faux   |
| __Vrai__ | __Vrai__ | __Vrai__ |


En Python, l'opérateur logique __AND__ s'écrit __and__.


### Opérateur OR  
L'opérateur __OR(OU)__ est un opérateur _binaire_(qui agit sur deux variables). Il a la valeur logique __Vrai__ si au moins une des deux variables a pour valeur __Vrai__. 

|    a     |    b     |    S     |
| :------: | :------: | :------: |
|   Faux   |   Faux   |   Faux   |
| __Faux__ | __Vrai__ | __Vrai__ |
| __Vrai__ | __Faux__ | __Vrai__ |
| __Vrai__ | __Vrai__ | __Vrai__ |

En Python, l'opérateur logique __OR__ s'écrit __or__.


### BONUS - Opérateur XOR
L'opérateur __XOR(OU Exclusif)__ est un opérateur _binaire_(qui agit sur deux variables). Il a la valeur logique __Vrai__ si __strictement__ une des deux variables a pour valeur __Vrai__.   

|    a     |    b     |    S     |
| :------: | :------: | :------: |
|   Faux   |   Faux   |   Faux   |
| __Faux__ | __Vrai__ | __Vrai__ |
| __Vrai__ | __Faux__ | __Vrai__ |
|   Vrai   |   Vrai   |   Faux   |

En Python, il n'existe pas d'opérateur __logique XOR__ mais il est possible de simuler son fonctionnement à partir d'opérateur déjà connus.





## Opérateurs de comparaison     

Il existe également des opérateurs de comparaisons en Python.   
Tout les opérateurs de comparaisons renvoient un booléen(`True` ou `False`).  

| Python |     Français      |  Exemple   | Résultat |
| :----: | :---------------: | :--------: | :------: |
|  `<`   | Inférieur(strict) |  `4 < 3`   | `False`  |
|  `>`   | Supérieur(strict) |  `4 > 3`   |  `True`  |
|  `<=`  | Inférieur ou égal |  `7 <= 7`  |  `True`  |
|  `>=`  | Supérieur ou égal | `7 >= 11`  | `False`  |
|  `==`  |       Égaux       | `4 == 2*2` |  `True`  |
|  `!=`  |     Différent     | `3*3 != 9` | `False`  |

> [!TIP]
> On peut traduire en français une instruction avec un opérateur booléen sous forme de question. 
> Par exemple, pour tester l'égalité entre une variable `a` et `b` :
>   - En Python `a == b`
>   - En français `Est-ce que a est égal à b ?` 



### Fonctions pratique 
 
- `print(contenu)` : permet d'afficher du contenu dans la console   
- `input(message_de_saisi)` : permet de demander à l'utilisateur de saisir une chaine de caractère  
- `int(a)` : permet de convertir a en type _int_  
- `float(a)` : permet de convertir a en type _float_  
- `str(a)` : permet de convertir a en type _str_   

