# Les listes  

## Avant-propos  
Le programme de 1re NSI parle de manipulation de __tableaux__ en Python et non de __listes__. Cependant, les __tableaux__ ne sont pas implémentés (nativement) dans Python. Autrement dit, nous allons manipuler des objets de type `list` pour parler de __tableaux__. De manière générale, nous dirons qu'en 1re NSI, les terminologies __tableau__ et __liste__ sont les mêmes.  

## Générales  
> [!TIP]
> Les listes sont des __structure de données__ __linéaires__.    

> [!IMPORTANT]
> Une __structure de donnée__ est un objet informatique permettant d'organiser et stocker plusieurs donnée.    

### Définition en Python  
En Python on définit une __liste__ avec des crochets `[]`, puis on y met un ou des éléments séparés par une virgule.    
Exemple : 
```Python 
l1 = [] # une liste vide
l2 = ["Alice", "Bob", "Charlie"]  # une liste de 3 éléments
```

### Longueur (ou taille)  
La longueur d'une liste est associée au nombre d'éléments qu'elle contient. Par exemple, la liste `l2` est de longueur 3 alors que `l1` a pour longueur 0. Il est possible de récupérer la longueur d'une liste avec la fonction `len()`.  
Exemple : 
```Python
l2 = ["Alice", "Bob", "Charlie"]  # une liste de 3 éléments
longueur_l2 = len(l2) # longueur_l2 vaut 3
```

### Indice
Les éléments d'une liste sont __indicés__, autrement dit chacun possède une __position__ dans la liste.  
> [!WARNING]  
> Le premier élément d'une liste est à __l'indice 0__.  



## Opération possible  

### Accès à un élément  
__L'indice__ des éléments d'une liste nous permet de les __identifier__ et donc d'y accéder.  
Pour cela il suffit d'écrire le nom de la liste suivie de l'indice de l'élément en question entre crochet.  
Exemple : 
```Python
l3 = [34, 95, -60, 49] 
element_indice_1 = l3[1]  #element_indice_1 vaut 95  
```

### Modification d'un élement  
Il est également possible de modifier un élément à l'aide de son indice. Pour cela on utilise la même notation que l'accès à un élément suivi du symbole `=` et la valeur qu'on souhaite attribuer.  
Exemple : 
```Python
l3 = [34, 95, -60, 49] 
l3[2] = 47  # nouvelle valeur pour l3 -> [34, 95, 47, 49]
```

### Ajout d'un élément 
On peut ajouter un élément à la fin de notre liste. La _méthode_ (programme de terminale) `.append()` permet cela.  
Pour faire appel à une méthode il suffit de mettre le nom de notre liste suivie d'un point ainsi que le nom de la méthode.  
Exemple : 
```Python
l3 = [34, 95, -60, 49] 
l3.append(18) # nouvelle valeur pour l3 -> [34, 95, -60, 49, 18]
```


## Parcours de liste  
Une des utilités des structures de données c'est que celles-ci peuvent être parcourues.  
En Python, on peut parcourir les `list` de deux manières différentes.  


### Par élément
On peut parcourir directement les éléments d'une `liste` avec une boucle `for`
Exemple :

```Python
l3 = [34, 95, -60, 49] 
for element in l3:
    print(element)
```


### Par indice  
Chaque élément possède un indice on peut donc parcourir les indices des éléments d'une liste et accéder aux éléments un par un.  
Exemple avec une boucle `for`:
```Python
l3 = [34, 95, -60, 49] 
for indice in range(len(l3)): 
    print(l3[indice])
```

Exemple avec une boucle `while`:
```Python
l3 = [34, 95, -60, 49] 
indice = 0
while indice != len(l3):
    print(l3[indice])
    indice = indice + 1
```


## Liste en compréhension   

Il existe une syntaxe en Python qui permet de créer des listes sur une ligne de code. C'est ce qu'on appelle une liste écrite __en compréhension__. 
Pour écrire une __liste en compréhension__ :
    - on commence par __mettre des crochets__ pour définir notre liste  
    - à l'intérieur des crochets on y mets le code correspondant à la liste souhaité    
    - on commence par y mettre __le nom__ de la variable qui représente chaque élément de notre liste  
    - suivi de la __boucle for__   
    - puis éventuellement __une condition__ sur notre variable  

Exemple :
```Python 
l4 = [i for i in range(4)] # [0, 1, 2, 3]
l5 = [nombre for nombre in range(10, 40) if nombre%2 == 0] # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
```


# Liste de listes  
Nous avons vu qu'une liste pouvait contenir différentes valeurs. 
Il se trouve qu'il est possible que les valeurs contenues dans une liste soient des __listes__.
On parle de __liste de listes__ (ou __tableau de tableaux__).

Voici des exemples de __listes de listes__ : 
```Python  
ll_prenoms = [["Alice", "Bob", "Charlie"],  ["Daphné", "Eva", "Frédéric"]]

score_positif = [4,11,37]
score_negatif = [-65,-34,- 7]
scores = [score_positif, score_negatif]
```

Il faut donc être vigilant au résultat attendu lors de l'utilisation des opérations sur une liste de listes.  

Exemple :
```Python  
ll_prenoms = [["Alice", "Bob", "Charlie"],  ["Daphné", "Eva", "Frédéric"]]

len(ll_prenoms) # 2
ll_prenoms[1] # ["Daphné", "Eva", "Frédéric"]
ll_prenoms[1][2] # "Frédéric"

```

## Parcours de liste de listes  

Le parcours de liste de listes se fait avec 2 boucles `for`.    

Initialement le parcours des éléments d'une liste s'effectue avec une boucle `for`. Dans notre situation nos éléments sont également des listes, il faut donc aussi les parcourir avec une deuxième boucle `for`.    

Exemple d'un parcours de liste de liste pour afficher le contenu :   

```Python  
ll_prenoms = [["Alice", "Bob", "Charlie"],  ["Daphné", "Eva", "Frédéric"]]

for liste in ll_prenoms:
    for prenom in liste:
        print(prenom)
```

