# Exercices POO

## Exercice 1 - classe Personnage  

Une sociéte souhaite créer un jeu vidéo, pour cela il lui faut créer des personnages.  

### 1.   
Écrire une classe `Personnage`, chaque personnage possède un nom, un niveau, un inventaire pour ranger des objets, un nombre de points d'attaque et un nombre de points de défense.  
Le constructeur prend en paramètres le nom du personnage, ses points d'attaque et de defense. 

### 2.   


```Python
class Personnage:
    def __init__(self, nom_personnage, attaque, defense):
        self.nom = nom_personnage
        self.niveau = 0 
        self.inventaire = []
        self.points_attaque = attaque
        self.points_defense = defense
```