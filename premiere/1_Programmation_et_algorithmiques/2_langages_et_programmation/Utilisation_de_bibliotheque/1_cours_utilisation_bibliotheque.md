# Utilisation de bibliothèque  

## Généralités  
Les bibliothèques (ou module, paquets) sont des programmes écrits par des programmeurs. 
Par définition il est totalement possible d'écrire ses propres bibliothèques.  

Ces programmes n'ont rien de plus que ceux qu'on à pu écrire ou voir depuis le début de l'année.   
Alors pourquoi les appelles t-on bibliothèque ? 

__Cet adjectif est donné à un programme utilisé dans un autre programme__  

Prenons un fichier `tournoi_de_football.py`, par exemple. Dans ce fichier est écrit un programme en Python qui permet de faire la gestion d'un tournoi de football.  
Le fichier `tournoi_de_football.py` à besoin du fichier `equipes.py` pour avoir accès aux données de chaque équipe.  
Il faut donc __importer__ le fichier `equipes.py` dans le fichier `tournoi_de_football.py`, dans ce contexte on dira que `equipes.py` est __bibliothèque__.  

## Emplacement des bibliothèques  

- Dans le cas évoqué ci-dessus on peut imaginer que le programmeur est l'auteur des 2 programmes. Il __faut placer dans le même dossier les 2 programmes__ afin que l'un puisse importer l'autre
- De manière générale les bibliothèques que nous allons utiliser ne sont pas écrites par nos soins, elles sont soit disponible sur internet. Des sites comme [PyPI](https://pypi.org/) permettent d'explorer les bibliothèques Python mise en ligne par la communauté qu'il est possible de récupérer.  
- Enfin, certaines bibliothèques sont déjà présentes sur nos machines puisqu'elles ont été installés lors de l'installation de votre IDE(Pycharm, Thonny, ...) Python.  

## Le mot clé `import` en Python

Pour importer une bibliothèque dans un programme en Python, on utilise le mot clé `import`.  
Ce mot peut être utilisé de 2 manières différentes.  
- `from nom_bibliotheque import nom_fonction` : Une fois cette ligne écrite il est possible de faire appel à `nom_fonction`. Il est possible de remplacer `nom_fonction` par `*` afin de pouvoir faire appel à toutes les fonctions de `nom_bibliotheque`
- `import nom_bibliotheque` : Une fois cette ligne écrite il est également possible de faire appel à toutes les fonctions mais chaque appel devra être précédée du nom de la bibliothèque. Voici un exemple d'utilisation `nom_bibliotheque.nom_fonction`

## Exemples d'utilisation  

3 exemples sur la fonction `sqrt` qui permet de calculer la racine carré d'un nombre, provenant de la  bibliotheque `math`. Ce module est habituellement déjà installé sur votre machine.  

```Python
from math import sqrt
resultat = sqrt(25)

from math import *
resultat = sqrt(25)

import math 
resultat = math.sqrt(25)
```