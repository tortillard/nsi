# TP Python — Création d'un labyrinte

## Contexte 

On cherche à représenter un labyrinthe en Python. 
Le labyrinthe est une grille de nombres tel que :
- `0` représente une case vide(une case où il est donc possible de se rendre) ;
- `1` représente un mur ;
- `2` représente le départ ;
- `3` représente la sortie ;
- (`4` pourra représenter le chemin trouvé par le programme dans une partie plus lointain du tp).

Voici un exemple de représentation d'une grille :
```Python
1 1 1 1 1 1 1
1 2 0 1 0 0 1
1 0 0 1 0 1 1
1 1 0 0 0 0 1
1 1 1 1 1 3 1
```



## Partie 1 — Créer le labyrinthe

   
> ![IMPORTANT] Q1
> Compléter la fonction suivante qui créer une grille de dimension `hauteur` * `largeur`. De plus, le départ se du labyrinthe se trouve en haut à gauche, et la sortie en bas à droite.  

```Python
def creer_grille(hauteur, largeur):
    """Renvoie une grille"""
    pass
```

> ![IMPORTANT] Q2
> Compléter la fonction suivante qui prend en paramètre une grille renvoyé par la fonction précédente et qui renvoie la même grille mais avec `nb_murs` placé aléatoirement sur celle-ci

```Python
def generer_labyrinthe(grille, nb_murs):
    """Ouvre des passages et renvoie le labyrinthe généré."""
    pass
```

> ![IMPORTANT] Q3
> Compléter la fonction suivante, qui affiche une grille en remplaçant chaque nombre par des caractères bien choisie. Par exemple, `█` pour un mur, un ` ` pour un passage, `D` pour le départ et `A` pour l’arrivée.
```Python
def afficher_labyrinthe(grille):
    """Affiche le labyrinthe dans la console."""
    pass
```
