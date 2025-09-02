# Les dictionnaires  

## Générales  

> [!TIP]
> Les dictionnaires sont des __structures de données associatives__.  

> [!IMPORTANT]
> Les dictionnaires fonctionnent avec un système de __clé__ et __valeur__.  
> Chaque __clé__ est associée à une __valeur__ du dictionnaire.  
> On appel un couple __clé__ et __valeur__ un _item_

> [!WARNING] 
> Comme on _identifie_ chaque __valeur__ de notre dictionnaire par une __clé__ il faut que les clés de notre dictionnaire soit __UNIQUE__.  

> [!WARNING] 
> Il est __IMPOSSIBLE__ de mettre en __clé__ d'un dictionnaire une valeur _mutable_(qu'on peut modifier).
> Comme par exemple une liste.   

## Définition en Python   
En Python on définit un __dictionnaire__ avec des accolades `{}`.
Puis on ajoute un couple __clé__, __valeur__ séparé par deux points `cle : valeur`. 
Enfin on sépare chaque couple par une `,`. 


Exemple : 
```Python 
dico_vide = {} # représente le dictionnaire vide
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}
dico_aleatoire = {"Bonjour" : False, 2 : (4, 9), True : 5, ("S", "alu","t") : [3.9, 7.2]}

# pour plus de lisibilité on peut passer des lignes entre chaque item.  Le dictionnaire suivant est équivalent à celui précédent
dico_aleatoire = {"Bonjour" : False, 
                    2 : (4, 9), 
                    True : 5, 
                    ("S", "alu","t") : [3.9, 7.2]
                }

dico_ERREUR = {[4,2] : "erreur !", [3.2, 4.7] : "erreur encore !"} # il n'est pas possible de définir ce dictionnaire car il est composé d'au moins une clé mutable.  
```

### Longueur (ou taille)  
La longueur d'un dictionnaire est associée au nombre de couple _clé_ et _valeur_ qu'il contient.  
Par exemple, le dictionnaire `dico_score` est de longueur 4 alors que `dico_vide` a pour longueur 0.    
Il est possible de récupérer la longueur d'un dictionnaire avec la fonction `len()`.    

Exemple : 
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}  # un dictionnaire de 4 items(couple clé valeur)
longueur_dico_score = len(dico_score) # longueur_dico_score vaut 4  
```

### Accès à une valeur   

Les éléments d'un dictionnaire ne sont pas _indicés_.   
On récupère une valeur à partir de sa __clé__.    
On récupère une valeur en notant `nom_du_dictionnaire[cle]`.

Exemple : 
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}  
valeur = dico_score["Bob"]  # la variable valeur contient 4 
```

### Ajout et Modification de couple clé/valeur  
Il est également possible d'__ajouter__ ou __modifier__ des couples clé/valeur.
Pour cela on utilise la même notation que l'accès à un élément suivi du symbole `=` et la valeur qu'on souhaite attribuer.  

> [!IMPORTANT]
> Si dans notre instruction, la clé _est déjà présente_ dans le dictionnaire alors cela __MODIFIERA__ la __valeur__ associée à la __clé__.
> En revanche, si la clé n'_est pas présente_ dans le dictionnaire alors cela __AJOUTERA__ une nouvelle __clé__ avec la  __valeur__ associée.  

Exemple : 
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}    

dico_score["Daniel"] = 40  # dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 40}    
dico_score["Elia"] = 73 # dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 40, "Elia" : 73}    
```

## Parcours de dictionnaire  

Comme les dictionnaires ne sont pas indicés il n'existe pas de _parcours par indice_.  

### Parcours par clés     
Il est possible d'utiliser le parcours par _élément_ dans ce cas là, les _éléments_ parcouru sont les _clés_ du dictionnaire.  

Exemple : 
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}    
for cle in dico_score :
    print(cle) 

# la variable `cle` va prendre les valeurs : "Alice", "Bob", "Charlie", "Daniel" et "Elia"
```  

Il existe également une autre façon de parcourir les clés, en utilisant la méthode `.keys()` des dictionnaires.    
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}    
for cle in dico_score.keys() :
    print(cle) 

# la variable `cle` va prendre les valeurs : "Alice", "Bob", "Charlie", "Daniel" et "Elia"
```

### Parcours par valeurs 

Pour parcourir les __valeurs__ de notre dictionnaire il est possible dans un premier temps de parcourir les __clés__ puis à partir de celle-ci accéder aux __valeurs__.   

Exemple 1 :   
```Python  
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}    
for cle in dico_score : # ou `for cle in dico_score.keys() :`
    print(dico_score[cle]) 

# `dico_score[cle]` va prendre les valeurs : 10, 4, 7, 2
```


On peut parcourir les valeurs de notre dictionnaire en utilisant la méthode `.values()` des dictionnaires.    

Exemple 2 :  
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}    
for valeur in dico_score.values() :
    print(valeur) 

# la variable `valeur` va prendre les valeurs : 10,4,7 et 2
```


### Parcours des clés et valeurs en même temps  
Un couple clé/valeur est nommée _item_, il est possible de parcourir les __clés__ et les __valeurs__ de notre dictionnaire en utilisant la méthode `.items()` des dictionnaires.    

Exemple 1 : 
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}    
for item in dico_score.items() :
    print(item)

# la variable item va prendre les valeurs suivantes :('Alice', 10), ('Bob', 4), ('Charlie', 7) et ('Daniel', 2)
```

Avec l'exemple 1 on peut récuperer les __clés__ et les __valeurs__ de chaque _item_ dans un __tuple__.  
Il existe une autre manière d'utiliser la méthode `.items()` afin de ne pas avoir à récupérer ces derniers dans un tuple.

Exemple 2 : 
```Python
dico_score = {"Alice" : 10, "Bob" : 4, "Charlie" : 7, "Daniel" : 2}    
for cle, valeur in dico_score.items() :
    print(cle)
    print(valeur)

# les variables cle et valeur vont prendre respectivement les valeurs suivantes :
# |cle         | valeur|
# | "Alice"    | 10    |
# | "Bob"      |  4    |
# | "Charlie"  |  7    |
# | "Daniel"   |  2    |
```

