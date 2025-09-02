# Simon 
L'objectif de ce projet est de programmer le jeu de société [__Simon__](https://fr.wikipedia.org/wiki/Simon_(jeu)).

L'utilisateur joue contre le programme qui choisit de manière aléatoire une suite de couleurs.   
__Au lancement du jeu__, le programme propose une couleur que le joueur doit reproduire.
Ensuite, à chaque itération, une couleur supplémentaire est ajouté.


## Cahier des charges - Version 1  
Le jeu est entièrement textuelle.    
Les couleurs peuvent être représentés par des chaines de caractères.   
On demande le pseudo du joueur au début du jeu.
Le joueur gagne s'il à correctement saisie 10 caractères et on note le score de chaque joueur dans un fichier nommé `score_simon.txt`.  
Il est intéressant d'effacer le contenu de la console python pour que l'utilisateur n'ai pas de visibilité sur la séquence de couleur à reproduire. Ce [site](https://www.delftstack.com/fr/howto/python/python-clear-console/) explique comment procéder. 

## Cahier des charges - Version 3  
Une version graphique de votre choix du jeu en mettant en évidence la séquence de couleurs à recopier pour l'utilisateur.

## Cahier des charges - Version 2  
Au lieu de taper la chaine de caractère correspondante l'utilisateur tape sur les flèches directionnel de son clavier pour représenter les couleurs verte, jaune, rouge, bleu.  
Pour cela il faut utiliser une __capture d'évènement__. 
Il est possible de capturer l'évènement de pression de touches sur un clavier à l'aide de la bibliothèque `keyboard`,`tkinter`, ...  


