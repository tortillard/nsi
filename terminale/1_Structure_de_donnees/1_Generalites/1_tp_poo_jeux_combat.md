# TP - Jeux de combat

On souhaite créer un jeu de combat en tour par tour faisant affronter des personnages.

## Partie 1 - classe Personnage  

En premier lieu, il faut faut créer les __personnages__ qui s'affronteront dans notre jeu.    
On décide de créer une classe __`Personnage`__.  

Chaque __`Personnage`__ possède :
- un __nom__.    
- un __niveau__.    
- un __inventaire__ pour ranger des objets.   
- une __capacité maximale initialisé à 5__ représentant le nombre d'objets qu'il est possible de ranger dans son inventaire.  
- un nombre de __points d'attaque__, de __points de défense__ et de __points de vie__.   

Lors de la création d'un personnage on choisit __le nom du personnage, ses points d'attaque, de defense et de vie__.     

### 1.   
Écrire le début de la classe `Personnage` en initialisant chaque attribut __judicieusement__.  

### 2.   
Ajouter les méthodes `get_attaque()`, `get_defense()` et `get_vie()` qui permettent de récupérer respectivement, les points d'attaque et de défense du personnage.  

### 2.   
Ajouter les méthodes `set_attaque(x)`, `set_defense(y)` et `set_vie(z)` qui permettent de modifier respectivement, les points d'attaque de défense et de vie du personnage.  

### 3. 
Ajouter une méthode `augmente_capacite()` qui permet __d'augmenter__ de __2__ la capacité maximale du personnage. 
 
### 4.  
Un personnage augmente la capacité maximale de son inventaire tout les 10 niveaux (au niveau 10, puis 20, 30, etc...).
Ajouter une méthode `augmente_niveau(n)` qui permet __d'ajouter__ `n` niveau à votre personnage. 

### 5.   
Ajouter une méthode `taille_inventaire` qui renvoi le nombre d'objets présent dans l'inventaire.  

### 6.   
Ajouter une méthode `ajoute_inventaire(o)` qui permet __d'ajouter__ un objet `o` à l'inventaire si la capacité maximale n'est pas dépassé. 

### 7.   
Ajouter une méthode `utilise_objet(o)` qui retire l'objet `o` de l'inventaire.   


## Partie 2 - classe Jeux 

