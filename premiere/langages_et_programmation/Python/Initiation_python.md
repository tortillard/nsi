# Introduction à Python

## Généralités  

> C'est quoi programmer ?  

Si vous lisez ce texte sur une machine (ordinateur, téléphone, ...), sachez que celle-ci est munie d'un __processeur__.
Le __processeur__ est un composant électronique capable d'effectuer des opérations assez simple mais surtout __TRÈS__ rapidement. 

Ce que nous aimerions faire, en tant qu'humains, c'est de tirer profit de la vitesse d'exécution du processeur pour lui demander de résoudre des problèmes, récupérer des données météo, simuler un jeu de course automobile, etc...

Pour se faire il nous faudrait un moyen de communiquer avec le processeur de notre ordinateur... 

Vous l'avez ?

Oui ! C'est à ça que servent __les langages de programmation__.   
On utilise un langage de programmation pour écrire un programme "compréhensible" par le processeur.   
C'est ainsi qu'on demande au processeur d'éffectuer tel ou tel calcul.   

Parmi ces langages de programmation (il en existe beaucoup), le langage Python est simple à apprendre et à utiliser.   
Sa facilité d'appropriation ne signifie pas que nous ne pouvons programmer que des choses "simples".  
Des applications comme YouTube ou Spotify sont en partie écrites en Python.  



## Origine  

Python est un langage de programmation inventé par Guido van Rossum. Sa première version date de 1991.
<img src="img/Guido.jpg" alt="drawing" width="400"/>

Le nom `Python` vient d'une émission télévisée nommée Monty Python's Flying Circus, dont Guido était passionné.

<img src="img/Python-logo.png" alt="drawing" width="300"/>


## De quoi a-t-on besoin pour programmer ?   

La manière la plus simple d'avoir le nécessaire pour prorammer en Python est de télécharger un __environnement de développement intégré ou IDE__ qui intègre déja ce langage de programmation.    

Parmis les IDE qui intègre déjà Python il y à :
    - Thonny (https://thonny.org/)
    - Pyzo (https://pyzo.org/)

Il existe bien d'autres IDE (PyCharm, VsCodium, ...) certains ont leur particularité mais globalement chacun possède 
- un éditeur de texte, qui permet d'écrire sont programme dans un fichier Python 
- une console(ou Shell) Python qui permet d'évaluer du code Python   
- un débogueur qui permet d'aider à la correction des bugs de notre programme

> Note : N'importe quel éditeur de texte peut faire l'affaire pour programmer en Python. 
> Vous pouvez très bien ouvrir l'application _Bloc-notes_, écrire un programme en Python, et suivre les étapes nécessaires pour que l'interpréteur évalue votre programme, mais ce n'est pas la méthode la plus simple ni la plus utilisée.









## Les variables  

En programmation, on a souvent besoin de déclarer des variables.
En Python, une variable est liée à une valeur et porte un nom. On déclare une variable en lui attribuant un nom puis en utilisant le symbole `=` pour l'affecter à une valeur.    

```Python
# Liste de noms de variables valides  
nom_de_variable = 7
a = 3
_score_du_joueur_11 = 23

# Liste de noms de variables non valides
7nom_de_variable = 7
-a = 3
)score_du_joueur_11 = 23
```

- __Testez les différents noms de variable__


## Les types de bases 

La programmation a pour objectif de représenter des problèmes informatiquement. Afin de représenter un quelconque problème, les langages de programmation mettent à disposition des types de base.

|              Nom en français               |    Nom en Python    |          Exemple           |
| :----------------------------------------: | :-----------------: | :------------------------: |
|            Les nombres entiers             |  int (de integer)   |             4              |
| Les nombres à virgule(ou nombre flottants) | float (de floating) |            4.3             |
|         Les chaînes de caractères          |   str (de string)   | "Bonjour !" ou 'Bonjour !' |
|                Les booléens                |  bool (de boolean)  |       True ou False        |

Il existe d'autres types appelés types construits (vus en SNT mais surtout en 1re NSI). Enfin, il est même possible de créer ses propres types (vus en Terminale NSI).


### Les nombres entiers  
Dans la section des opérateurs arithmétiques, vous avez manipulé des nombres entiers.
En Python, le type __int__ est associé aux nombres entiers. On représente un nombre entier tout simplement en notant le nombre souhaité.  

Exemples : 

```Python
age = 16
nombre_d_objet = 4
annee_revolution = 1789
temperature_chez_les_gaulois = -8000
```  
  


### Les nombres à virgule(ou flottants)
En Python, le type float est associé aux nombres à virgule. On représente un nombre flottant avec un point __( . )__ à la place de la virgule. 

Exemples : 

```Python
taille = 157.6
poids_valise = 20.3
prix_baguette = 1.0
```

### Les opérateurs arithmétiques  

Les opérateurs arithmétiques élémentaires sont intégrés dans le langage Python. On peut s'en servir pour effectuer les mêmes calculs que sur une calculatrice.
On peut les utiliser aussi bien avec des int que des float (tant que les opérations respectent les règles mathématiques).
Comme en mathématiques, il est également possible d'écrire des expressions parenthésées.  

> Note :
    > - En Python, le symbole `#` déclare le début d'un __commentaire__. Un commentaire est un morceau de texte que l'on peut retrouver dans les programmes, généralement pour donner des précisions sur le code. Le commentaire n'est pas lu par Python, il est là à titre informatif.
    > - Les 3 chevrons `>>>` ne sont pas compréhensibles en Python. Cette notation est utilisée pour représenter l'instruction entrée dans une console Python ; la ligne qui suit est le résultat renvoyé.



```Python
>>> 4 + 2  # Addition  
6


>>> 7 - 3  # Soustraction  
4 

>>> -7 - 3.4 # Le symbole - peut aussi être utilisé pour représenter un nombre négatif 
-10.4


>>> 3 * 7.8 # Multiplication  
23.4  


>>> 4 ** 3 # Puissance d'exposant ici 4 puissance 3  
64

>>> 7 / 2 # Division décimale(avec nombres à virgule)  
3.5

# Il est également possible d'effectuer une division euclidienne en utilisant les symboles suivant.

>>> 7 // 2 # partie entière de la division euclidienne 
3

>>> 7 % 2 # reste de la division euclidienne 
1
```

- __Testez tout les opérateurs arithmétiques__


### Les chaines de caractères  
Les chaînes de caractères permettent de représenter des phrases, des mots, etc.
En Python, le type __str__ est associé aux chaînes de caractères. Les chaînes de caractères peuvent contenir n'importe quel caractère ou ne pas en contenir du tout (chaîne de caractères vide).
En Python, on représente une chaîne de caractères par une suite de caractères entourés par des __guillemets simples ( ' )__ ou des __guillemets doubles ( " )__.  

Exemples : 

```Python
nom = "Tortillard"  
mot_de_passe_complique = '78Rtvs_@)./*ko'
premiere_phrase = "Bonjour tout le monde !"
phrase_avec_apostrophe = "Il n'est pas parti toute suite"
```
- __Expliquez ce qui se passe lorsque l'on décide de représenter la dernière chaîne de caractères entourée de guillemets simples.__


Il est possible de concaténer ("coller") deux chaînes de caractères à l'aide du symbole `+`.

Exemples : 

```Python
debut_prenom = "Tim"
fin_prenom = "oléon"
prenom_entier = debut_prenom + fin_prenom # prenom_entier à pour valeur "Timoléon"
```


### Les booléens 
En Python, le type __bool__ est associé aux booléens. Il n'existe que deux valeurs possibles : `True` (vrai) ou `False` (faux).
Le type booléen est très utilisé en programmation (vous en verrez l'utilité par la suite).

Exemples : 
```Python
lumiere_eteinte = True
interrupteur_ferme = False
```

### Opérateurs booléens

George Boole est le créateur de l'algèbre de Boole, une branche des mathématiques qui s'intéresse à la logique. L'algèbre de Boole définit les opérateurs booléens suivants.


#### L'opérateur __NOT (NON)__
L'opérateur __NOT__ est un opérateur _unaire_ (qui agit sur _une seule_ variable). Il a pour effet d'inverser la valeur logique de la variable sur laquelle il agit. Voici sa table de vérité :

|      a      | NOT a |
| :---------: | :---: |
| 0 (ou Faux) |   1   |
| 1 (ou Vrai) |   0   |

En Python, l'opérateur logique __NOT__ s'écrit __not__.

Exemple :

```Python
a = True

>>> not a
False

>>> not not a
True
```

L'opérateur __AND(ET)__ est un opérateur binaire (qui agit sur deux variables). Il a la valeur logique __Vrai__ si et seulement si les deux variables sont __Vrai__. Voici sa table de vérité : 

|   a   |   b   | a AND b |
| :---: | :---: | :-----: |
|   0   |   0   |    0    |
|   0   |   1   |    0    |
|   1   |   0   |    0    |
| __1__ | __1__ |  __1__  |


En Python l'opérateur logique __AND__ s'écrit __and__.
```Python
a = True 
b = False 

>>> print(a and b)
False

>>> print((not a) and b)
False

>>> print(a and (not b))
True
```

L'opérateur __OR(OU)__ est un opérateur _binaire_(qui agit sur deux variables). Il a la valeur logique __Vrai__ si au moins une des deux variables a pour valeur __Vrai__. 
Voici sa table de vérité 

|   a   |   b   |   S   |
| :---: | :---: | :---: |
|   0   |   0   |   0   |
| __0__ | __1__ | __1__ |
| __1__ | __0__ | __1__ |
| __1__ | __1__ | __1__ |

En Python l'opérateur logique __OR__ s'écrit __or__.

```Python
a = True 
b = False 

>>> print(a or b)
True

>>> print(a or (not b))
True

>>> print((not a) or b)
False
```  

L'opérateur __XOR(OU Exclusif)__ est un opérateur _binaire_(qui agit sur deux variables). Il a la valeur logique __Vrai__ si __strictement__ une des deux variables a pour valeur __Vrai__. 
Voici sa table de vérité 

|   a   |   b   |   S   |
| :---: | :---: | :---: |
|   0   |   0   |   0   |
| __0__ | __1__ | __1__ |
| __1__ | __0__ | __1__ |
|   1   |   1   |   0   |

En Python l'opérateur logique __OR__ s'écrit __or__.

```Python
a = True 
b = False 

>>> print(a or b)
True

>>> print(a or (not b))
True

>>> print((not a) or b)
False
```


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
