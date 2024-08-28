

## Rappel : les types de bases 

|       Français        | Anglais  | Python  |    Exemples de valeurs     |
| :-------------------: | :------: | :-----: | :------------------------: |
|    Nombre entiers     | Integer  |  `int`  |        `4` ou `-7`         |
|    Nombre décimaux    | Floatant | `float` |      `9.3` ou `-11.0`      |
| Chaines de caractères |  String  |  `str`  | `"Hello"` ou `'@kwm78E-$'` |
|        Booléen        | Boolean  | `bool`  |     `True` ou `False`      |

> Il existe d'autres types qui seront vu plus tard en NSI. 

## Opérateurs arithmétique
Ces opérateurs s'utilisent avec des `int` et des `float`  
| En Python |             En Français             |  
| :-------: | :---------------------------------: | 
|    `+`    |              Addition               | 
|    `-`    |            Soustraction             | 
|    `*`    |           Multiplication            | 
|   `**`    |              Puissance              |          
|    `/`    |              Division               |          
|   `//`    | Quotient de la division euclidienne |          
|    `%`    |  Reste de la division euclidienne   |          



<!-- 
// TO DO  
Mettre 0 ou 1 ou mettre des Vrai et des Faux pcqe c'est un chapitre les booléens ? 
Voir pour exo ou application à faire entre ## op arithmé ## op bool , ... 

-->
## Opérateurs booléens  

### Opérateur NOT 

L'opérateur __NOT(NON)__ est un opérateur _unaire_ (qui agit sur _une seule_ variable). Il a pour effet d'inverser la valeur logique de la variable sur laquelle il agit. Voici sa table de vérité :

|      a      | NOT a |
| :---------: | :---: |
| Faux |   1   |
| Vrai |   0   |

En Python, l'opérateur logique __NOT__ s'écrit __not__.


### Opérateur AND
L'opérateur __AND(ET)__ est un opérateur binaire (qui agit sur deux variables). Il a la valeur logique __Vrai__ si et seulement si les deux variables sont __Vrai__. Voici sa table de vérité : 

|   a   |   b   | a AND b |
| :---: | :---: | :-----: |
|   0   |   0   |    0    |
|   0   |   1   |    0    |
|   1   |   0   |    0    |
| __1__ | __1__ |  __1__  |


En Python l'opérateur logique __AND__ s'écrit __and__.



### Opérateur OR  
L'opérateur __OR(OU)__ est un opérateur _binaire_(qui agit sur deux variables). Il a la valeur logique __Vrai__ si au moins une des deux variables a pour valeur __Vrai__. 
Voici sa table de vérité 

|   a   |   b   |   S   |
| :---: | :---: | :---: |
|   0   |   0   |   0   |
| __0__ | __1__ | __1__ |
| __1__ | __0__ | __1__ |
| __1__ | __1__ | __1__ |

En Python l'opérateur logique __OR__ s'écrit __or__.


### BONUS - Opérateur XOR
L'opérateur __XOR(OU Exclusif)__ est un opérateur _binaire_(qui agit sur deux variables). Il a la valeur logique __Vrai__ si __strictement__ une des deux variables a pour valeur __Vrai__. 
Voici sa table de vérité 

|   a   |   b   |   S   |
| :---: | :---: | :---: |
|   0   |   0   |   0   |
| __0__ | __1__ | __1__ |
| __1__ | __0__ | __1__ |
|   1   |   1   |   0   |

En Python il n'existe pas d'opérateur __logique XOR__, il est possible de simuler son fonctionnement à partir des opérateurs `not` et `or` .



## Particularité pour les chaines de caractères
- `+`
- `*`


## Opérateurs de comparaison 
- `<` 
- `>`
- `<=` 
- `>=`
- `==`
- `!=`









### Fonctions pratique 
 
- print(contenu) : permet d'afficher du contenu dans la console   
- input(message_de_saisi) : permet de demander à l'utilisateur de saisir une chaine de caractère  
- int(a) : permet de convertir a en type _int_  
- float(a) : permet de convertir a en type _float_  
- str(a) : permet de convertir a en type _str_   

Exemple : 

_On souhaite écrire un programme qui demande le nombre de pommes que possède un utilisateur, pour lui en donner 2 supplémentaires. On affiche à la fin un message qui donne le nouveau nombre de pommes que possède notre utilisateur._  

```Python
nb_pomme_en_str = input("Combien de pommes possédez-vous ?")
nb_pomme = int(nb_pomme_en_str)
nouveau_nb_pomme = nb_pomme + 2
nouveau_nb_pomme_en_str = str(nouveau_nb_pomme)
print("Maintenant vous avez " + nouveau_nb_pomme_en_str + " pommes !")
```

