# Initiation à la programmation avec le langage Python  

## C'est quoi Python ?  

Python est un langage de programmation inventé par Guido van Rossum. Sa première version date de 1991. 
![Guido van Rossum](img/Guido.jpg)  

Le nom `Python` vient d'une émission télévisée nommée _Monty Python's Flying Circus_ pour laquelle Guido était passionnée.   

![Logo Python](img/Python-logo.png)    


## Quels outil faut-il pour programmer en Python ? 

### Interpréteur  

Pas grand chose ! Comme dans la plupart des langages de programmation il vous suffit de télécharger sur le site officiel de Python(https://www.python.org/downloads/) la dernière version pour pouvoir programmer.   

Le téléchargement installe le langage de programmation ainsi qu'un interpréteur __Python__. Le rôle de l'interpréteur __Python__ est de _comprendre_ le code Python.  

Par exemple la ligne `Vive l'informatique` ne sera pas comprise par l'interpréteur Python. C'est une ligne écrit en français et notre intepréteur n'est capable que de _comprendre_ du Python. Par contre la ligne `a = 2` sera comprise par l'interpréteur puisqu'elle est écrite en Python.  


### Editeur de texte  

L'interpréteur ne _comprend_ qu'une ligne à la fois. Il est possible d'écrire un programme en Python sur plusieurs ligne dans un __éditeur de texte__ puis de dire à l'interpréteur d'évaluer chaque ligne du programme.  

N'importe quel éditeur de texte fait l'affaire pour programmer en Python. Vous pouvez très bien ouvrir l'application _Bloc-notes_  écrire un programme en Python et faire les étapes nécesaaires pour que l'interpréteur lise votre programme mais ce n'est pas la méthode la plus simple ni celle la plus utilisée.  

Il existe des IDE(Integrated Development Environment) ou environnement de développement intégré spécialisé pour le langage Python. 
Les IDE contiennent un éditeur de texte, un terminal Python et un débogueur(outil permettant de corriger les bugs de notre programme).

En bref, les IDE facilitent la vie des développeurs voici quelques noms d'IDE avec lesquels il est possible de programmer en Python : 
    - Thonny (https://thonny.org/) 
    - Pycharm (https://www.jetbrains.com/fr-fr/pycharm/) 
    - Pyzo (https://pyzo.org/)  
    - VSCodium (https://vscodium.com/)  


## Le langage Python  

Premièrement à quoi ça sert de programmer ? Si vous lisez ce texte sur une machine(ordinateur, téléphone, ...) il est très probable que ce dernier soit muni d'un __processeur__. Le processeur est un composant électronique capable d'éffectuer des opérations __TRES__ rapidement, on dit souvent que c'est le _cerveau_ de l'ordinateur. 

Ce que nous aimerions faire en tant qu'humain, c'est de tirer parti de la vitesse d'exécution du processeur pour lui demander de résoudre des problèmes, récupérer des données météo, simuler un jeu de cours automobile, etc... 

Il nous faudrait donc un moyen en tant qu'humain de communiquer avec un processeur...

Vous l'avez ? 

Oui ! c'est à ça que servent les langages de programmation. On utilise un langage de programmation pour écrire un programme "compréhensible" par le processeur. Ainsi on peut discuter avec notre machine.    

Parmis ces langages de programmation(il en existe un paquet), le langage Python est simple d'apprentissage et d'utilisation. Sa facilité d'appropriation ne veut pas dire que nous ne pouvons programmer que des choses "simples". Des applications comme Youtube ou Spotify sont écrite en partie en Python.  


## Les variables  

En programmation on à souvent besoin de déclarer des variables. 
En Python une variable est liée à une valeur et porte un nom. On déclare une variable en lui attribuant un nom puis on utilise le symbole `=` pour l'affecter à une valeur.    

```Python
# Liste de nom de variable valide  
nom_de_variable = 7
a = 3
_score_du_joueur_11 = 23

# Liste de nom de variable non valide
7nom_de_variable = 7
-a = 3
)score_du_joueur_11 = 23
```

- __Testez les différents noms de variable__


## Les types de bases 

La programmation à pour objectif de représenter des problèmes informatiquement. Afin de représenter un quelconque problème les langages de programmation mettent à dispositions des types de bases.

|              Nom en français               |    Nom en Python    |          Exemple           |
| :----------------------------------------: | :-----------------: | :------------------------: |
|            Les nombres entiers             |  int (de integer)   |             4              |
| Les nombres à virgule(ou nombre flottants) | float (de floating) |            4.3             |
|         Les chaines de caractères          |   str (de string)   | "Bonjour !" ou 'Bonjour !' |
|                Les booléens                |  bool (de boolean)  |       True ou False        |

 Il existe d'autre type appelé _types construits_ (vu en SNT mais surtout en 1re NSI). Enfin il est même possible de créer ses propres types (vu en Terminale NSI).


### Les nombres entiers  
Dans la section des opérateurs arithmétiques vous avez manipulé des nombres entiers. 
En Python le type __int__ est associée aux nombres entiers. On représente un nombre entier tout simplement en notant le nombre souhaité.  

Exemples : 

```Python
age = 16
nombre_d_objet = 4
annee_revolution = 1789
temperature_chez_les_gaulois = -8000
```  
  


### Les nombres à virgule(ou flottants)
En Python le type __float__ est associée aux nombres à virgule. On représente un nombre flottant avec un __point ( . )__ à la place de la virgule. 

Exemples : 

```Python
taille = 157.6
poids_valise = 20.3
prix_baguette = 1.0
```

### Les opérateurs arithmétiques  

Les opérateurs arithmétique élémentaire sont intégré dans le langage Python. On peut s'en servir pour effectuer les mêmes calculs que sur une calculatrice. 
On peut les utilise aussi bien avec des _int_ que des _float_(tant que les opérations respectent les règles mathématique). 
Comme en mathématique il est également possible d'écrire des expressions parenthésées.  


> _Note_ : 
> - En Python le symbole `#` déclare le début d'un __commentaire__. Un commentaire est un morceau de texte que l'on peut retrouver dans les programmes généralement pour donner des précisions au code. Le commentaire n'est pas _lus_ par Python il est là à titre informatif. 
> - Les 3 chevrons `>>>` ne sont pas compréhensible en Python. Cette notation est utilisé pour représenter l'instruction entré dans une console Python, la ligne qui suit est le résultat renvoyé.



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
Les chaines de caractères permettent de représenter des phrases, des mots, ...  
En Python le type __str__ est associée aux chaines de caractères. Les chaines de caractères peuvent contenir n'importe quel caractère ou ne pas en contenir du tout(chaine de caractères vide).  
En Python on représente une chaine de caractère par une suite de caractères entourés par des __guillemets simple ( ' )__ ou des __guillemets double ( " )__  

Exemples : 

```Python
nom = "Tortillard"  
mot_de_passe_complique = '78Rtvs_@)./*ko'
premiere_phrase = "Bonjour tout le monde !"
phrase_avec_apostrophe = "Il n'est pas parti toute suite"
```
- __Expliquez ce qui se passe lorsque l'on décide de représenter la dernier chaine de caractère entouré de guillemet simple__


Il est possible de concaténer('coller') deux chaines de caractères à l'aide du symbole `+`. 
Exemples : 

```Python
debut_prenom = "Tim"
fin_prenom = "oléon"
prenom_entier = debut_prenom + fin_prenom # prenom_entier à pour valeur "Timoléon"
```


### Les booléens 
En Python le type __bool__ est associée aux booléens. Il n'y a qu deux valeurs possibles pour les booléens, soit la valeur `True` (vrai) ou `False` (faux).  

Les valeurs de vérité booléennes nous permettent notamment de manipuler des conditions (voir suite du chapitre)

Exemples : 
```Python
lumiere_eteinte = True
interrupteur_ferme = False
```

### Opérateur booléens  
George Boole est le créateur de l'algèbre de Boole, c'est une partie des mathématiques qui s'intéresse à la logique. 
L'algèbre de Boole définit des opérateurs booléen suivant.  

On illustre chaque opérateur booléen dans un tableau.  
`a, b, ..` sont des variables et la colonne `S` et le résultat logique de l'opération illustré entre les variables.  


L'opérateur __NOT(NON)__ est un opérateur _unaire_(qui agit sur _une_ seule variable). Il à pour effet d'inverser la valeur logique de la variable sur laquelle il agit. 
Voici sa table de vérité :

|      a      |   S   |
| :---------: | :---: |
| 0 (ou Faux) |   1   |
| 1 (ou Vrai) |   0   |


En Python l'opérateur logique __NOT__ s'écrit __not__. 
Exemple : 

```Python
a = True 

>>> not a
False

>>> not not a
True
```

L'opérateur __AND(ET)__ est un opérateur _binaire_(qui agit sur deux variables). Il à la valeur logique __Vrai__ si et seulement si les deux variables sont __Vrai__. 
Voici sa table de vérité 

|   a   |   b   |   S   |
| :---: | :---: | :---: |
|   0   |   0   |   0   |
|   0   |   1   |   0   |
|   1   |   0   |   0   |
| __1__ | __1__ | __1__ |

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

L'opérateur __OR(OU)__ est un opérateur _binaire_(qui agit sur deux variables). Il à la valeur logique __Vrai__ si au moins une des deux variables à pour valeur __Vrai__. 
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

L'opérateur __XOR(OU Exclusif)__ est un opérateur _binaire_(qui agit sur deux variables). Il à la valeur logique __Vrai__ si __strictement__ une des deux variables à pour valeur __Vrai__. 
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

Exemples : 

On souhaite écrire un programme qui demande le nombre de pommes que possède un utilisateur, pour lui en donner 2 supplémentaire.  
On affiche à la fin un message qui donne le nouveau nombre de pomme que possède notre utilisateur.  

```Python
nb_pomme_en_str = input("Combien de pomme possédez vous ?")
nb_pomme = int(nb_pomme_en_str)
nouveau_nb_pomme = nb_pomme + 2
nouveau_nb_pomme_en_str = str(nouveau_nb_pomme)
print("Maintenant vous avez " + nouveau_nb_pomme_en_str + "!")
```

## Les boucles  

Une boucle est une structure de contrôle utiliser afin d'automatiser le traitement d'une ou plusieurs instruction répètitive. 
Par exemple si un programme informatique doit récupérer le nom et la date de naissance des 1200 élèves d'un établissement scolaire au lieu d'écrire 1200 fois les mêmes instruction dans notre programme on aura plutôt quelque chose comme cela. 

```
pour identifiant_eleve allant de 0 à 1199 faire
    nom_eleve = recupere_nom(identifiant_eleve)
    date_naissance_eleve = recupere_date_naissance(identifiant_eleve)
    identifiant_eleve = identifiant_eleve + 1
```  

En Python il existe deux types de boucle. 
