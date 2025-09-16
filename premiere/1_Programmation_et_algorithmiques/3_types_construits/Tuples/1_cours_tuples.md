# Les tuples

## Générales  
Les tuples sont des __structures de données__ linéaires.  

Un tuple est __une structure de données linéaire__ qui permet de stocker une collection d'éléments. 

> [!WARNING]
> Contrairement aux listes, les tuples sont __immuables__(qui ne peut pas être modifié),

## Définition en Python 

En Python on définit un tuple avec des parenthèses `()`, puis on y met u nou des éléments séparés par une virgule.  
Exemple : 

```Python

t1 = () # un tuple vide
t2 = (4,9,7) # un tuple de 3 éléments  
t3 = "bonjour", False # une variante sans parenthèses qui correspond au tuple ("bonjour", False)

```

## Opérations possible 

Beaucoup de similitude existe entre les listes et les tuples

### Longueur (ou taille)
On peut utiliser la fonction `len()` sur un tuple. Par exemple `len(t2)` renvoi 3.

### Accès à un élément  
Les éléments d'un tuple sont __indicés__, on peut accéder __aux éléments__ à partir de leur indice.  
En tapant le nom du tuple suivi de crochets et de l'indice de l'élément voulus.  
Par exemple `t3[0]` donne `"bonjour"`.  

### Concaténation  
On peut concaténer des tuples à l'aide du symbole `+`. 
Par exemple `t3 + t2` donne `("bonjour", False, 4, 9, 7)`.

### Répétition  
Il est également possible d'utiliser le symbole `*` pour effectuer une répétition sur les tuples.  
Par exemple `t2 * 3` donne `(4, 9, 7, 4, 9, 7, 4, 9, 7)`


## Opérations impossible  

Comme énoncé précédemment les tuples __sont immuables__. Il n'est pas possible de les modifier. 
Certaines opérations sont donc impossibles avec les tuples.  

Les instructions suivantes déclenche une erreur.  
Dans les exemples suivants on considère le tuple `t4 = (9,3,6)`

- Modification d'un élément : `t4[0] = 1`
- Ajout ou suppression d'un élément : il n'existe pas de méthode pour ajouter un élément à un tuple comme `append()` ou supprimer comme `remove()` pour les listes.  




