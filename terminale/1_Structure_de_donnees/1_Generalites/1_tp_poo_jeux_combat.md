# TP - Jeux de combat

On souhaite créer un jeu de combat en tour par tour faisant affronter des personnages.

## Partie 1 - classe Personnage  

En premier lieu, il faut faut créer les __personnages__ qui s'affronteront dans notre jeu.   
Pour cela, créer un fichier `Personnage.py` dans lequel nous allons écrire la classe __`Personnage`__.  

Chaque __`Personnage`__ possède pour attribut :
- un __nom__.    
- un __niveau__.    
- un __inventaire__ pour ranger des objets.   
- une __capacité maximale initialisé à 5__ représentant le nombre d'objets qu'il est possible de ranger dans son inventaire.  
- un nombre de __points d'attaque__, de __points de défense__ et de __points de vie__.
- une __vitesse initialisé à 10__   

Lors de la création d'un personnage on choisit __le nom du personnage, ses points d'attaque, de defense et de vie__.     

### 1.   
Écrire le début de la classe `Personnage` en initialisant chaque attribut __judicieusement__.  

### 2.   
Ajouter les méthodes `get_attaque(self)`, `get_defense(self)`, `get_vie(self)` et `get_vitesse(self)` qui permettent de récupérer respectivement, les points d'attaque, de défense, de vie et de vitesse du personnage.  

### 3. 
Ajouter la méthode `get_incventaire(self)` qui permet de récupérer l'inventaire du du personnage.    

### 3.   
Ajouter les méthodes `set_attaque(self, a)`, `set_defense(self, d)`, `set_vie(self, v)` et `set_vitesse(self, vit)` qui permettent de modifier respectivement, les points d'attaque de défense, de vie et de vitesse du personnage.  

### 4. 
Ajouter une méthode nommé `augmente_capacite` qui permet __d'augmenter__ de __2__ la capacité maximale du personnage. 
 
### 5.  
Un personnage augmente la __capacité maximale__ de son inventaire tout les 10 niveaux (au niveau 10, puis 20, 30, etc...).
Ajouter une méthode `augmente_niveau(self, n)` qui permet __d'ajouter__ `n` niveau à votre personnage et augmente la capacité maximale du Personnage quand c'est nécessaire. 

### 6.   
Ajouter une méthode nommé `nombre_objets` qui renvoi le nombre d'objets présent dans l'inventaire.  

### 7.   
Ajouter une méthode `ajoute_inventaire(self, o)` qui permet __d'ajouter__ un objet `o` à l'inventaire si la capacité maximale n'est pas dépassé. Sinon qui affiche `"Votre inventaire est plein !"` 

### 8.   
Ajouter une méthode `utilise_objet(self, o)` qui retire l'objet `o` de l'inventaire et affiche `"Vous utilisez l'objet o"`.   


## Partie 2 - classe Objet 
Lors d'un tour de jeu le Personnage peut décider soit d'attaquer soit d'utiliser un objet.  
Nous allons donc écrire une nouvelle classe `Objet` dans un autre fichier nommé `Objet.py`.  

### 9.
Écrire la classe `Objet` avec son constructeur ainsi que son seul attribut `nom` qui désigne le nom de l'`Objet`.
Le nom de l'objet sera choisi à la création d'un `Objet`. 

### 10.
Ajouter une méthode qui permet de récupérer le nom de l'`Objet`

### 11.
Ajouter une méthode avec pour signature `utilisation(self, personnage_utilisateur, personnage_adversaire)` qui applique l'effet de l'objet de `personnage_utilisateur`.  

Voici la liste des objets et leurs effet :  
- Si l'objet est une __Potion de vie__ alors : Ajoute 50 points de vie à l'utilisateur  
- __Bracelet de force__ : Ajoute 50 points d'attaque à l'utilisateur    
- __Bouclier__ : Ajoute 50 points de défense à l'utilisateur    
- __Potion de faiblesse__ : Diminue de 50 points l'attaque de l'adversaire    
- __Pierre lumineuse__ : Ajoute 50 points d'attaque à l'utilisateur et diminue de 50 points la défense de l'adversaire  

Pour informer que l'effet d'un objet est bien appliqué, on affichera une phrase explicative.    
Par exemple lors de l'utilisation d'une `Potion de vie` on affichera : `"Votre vie passe de 10 à 60"`  

## Partie 3 - classe Jeu 
Le but de cette partie est de créer une classe `Jeu` en mettant en scène nos `Personnages` et nos `Objets`. 
Créer un nouveau fichier `Jeu.py` placé dans le même dossier que le fichier `Personnage.py` et `Objet.py`. 


### 12.  
Importer les fichiers `Personnage.py` et `Objet.py` dans le fichier `Jeu.py`.  
Pour cela il suffit d'écrire au début du fichier

```Python
from Personnage import Personnage
from Objet import Objet
```

### 13.  

Un `Jeu` (ou une partie) se fait à 2 joueurs.
La classe `Jeu` possède donc 2 attributs qui représente les 2 joueurs.
Ces attributs sont initialisé lors de la création de la classe. 

Écrire le constructeur de la classe `Jeu`, ses attributs ainsi que 2 méthodes permettant de récupérer respectivement les attributs.  

### 14.  

Dans notre jeu, lorsque les 2 joueurs ont fini leur tour recoivent un objet aléatoire qui viendra s'ajouter à leur inventaire.  
Pour cela nous allons utiliser la bibliothèque `random` qui contient une fonction nommé `choice`. (Quelques exemples d'utilisation de cette fonction [ici](https://www.w3schools.com/python/ref_random_choice.asp))

Écrire une méthode `distribution_aleatoire_objet` qui distribue un objet aléatoire de la liste à la __question 11__.  

### 15.  

Écrire une méthode ayant pour signature `frappe(self, perso_attaquant, perso_defendant)` simulant le fait que `perso_attaquant` donne un coup à `perso_defendant`.  

Cette méthode diminue la vie du `perso_defendant` en lui infligeant un nombre de __dégats__. 
Les dégats d'une attaque sont le __maximum__ entre : 
  - `attaque_perso_attaquant - defense_perso_defendant`
  - `10`

Ce calcul signifie : _"Même si un personnage a une très faible attaque et/ou son adversaire a une très grosse défense, un coup infligera 10 points au minimum"_



### 16.

Écrire une méthode ayant pour signature `combat_fini(self)` et qui renvoi un nombre entier.  
Cette méthode permet de tester si un combat est fini. 
Un combat est fini si la vie d'un des 2 joueurs est inférieur ou égal à 0.  
Afin de connaitre le vainqueur du combat on renvoi `1` si le premier joueur n'as plus de vie, `2` si le second joueur n'as plus de vie.  
Si les 2 joueurs possèdent encore de la vie, le combat n'est pas fini et on renvoi `0`. 


### 17.  
Il reste une dernière méthode à écire que nous nommerons `combat`. 
Cette méthode est la plus importante puisqu'elle met en harmonie toutes celle précédemment écrite pour lancer le combat entre 2 joueurs.  

Voilà comment s'organise un combat entre 2 personnages.    
- Le premier joueur fait un choix entre attaquer ou utiliser un de ces objets.   
- Le second joueur fait pareil   
- On distribue aléatoirement un objet aux deux joueurs   
- On affiche un détails des points(attaque, defense, vie) de chaque personnage  
- Lorsque le combat est terminé on affiche le nom du vainqueur !

