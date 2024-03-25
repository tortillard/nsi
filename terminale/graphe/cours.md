# Graphes  

## Vocabulaire  

Un __graphe__ est une structure de donnée relationnel comportant :  
- un ensemble __d'arrêtes__, généralement noté $E$ (Edges en anglais)  
- un ensemble __de sommets__, généralement noté $V$ (Vertices en anglais)  


Un graphe __non orienté__ est représenté par des arrêtes. 
L'ensemble des __arrêtes__ est constitué de couple symétrique, c'est à dire que pour chaque couple (sommet_1, sommet_2) il existe également le couple (sommet_2, sommet_1)
> Cette situation peut être représentée par le graphe des relations dans un réseau social à liens "d'amitié". (Exemple : Facebook) 


![](img/exemple_graphe_non_oriente.png)   


Un graphe __orienté__ est représenté par des arrêtes fléchées nommé __arcs__.  
L'ensemble des __arcs__ est constitué de couple (sommet_1, sommet_2)  
> Cette situation peut être représentée par le graphe des relations dans un réseau social à liens "d'abonnement". (Exemple : X(anciennement Twitter), Youtube)

![](img/exemple_graphe_oriente.png)  



Dans un graphe non orienté :  
- on dit que deux sommets sont __adjacents__(ou voisins) si une arrête relie ces deux sommets.    
- Le nombre de sommets adjacents à un sommet est appelé le __degré__.    

Dans un graphe orienté :  
- si une arrête relie (sommet_1, sommet_2) on dit que:  
    - sommet_2 est un __successeur__ de sommet_1   
    - sommet_1 est un __prédecesseur__ de sommet_2   

- le nombre de sommets :  
    - successeur d'un sommet est appelé __degré sortant__  
    - prédécesseur d'un sommet est appelé __degré entrant__  

On appelle __chemin__ la suite de sommets $s_0, s_1, ... s_f$ tels que $\forall i, 0 \leq i \lt f$, $s_i \space \text{et} \space s_{i+1}$ sont adjacents  

On appelle __cycle__ dans un graphe non orienté (__circuit__ dans un graphe orienté) un chemin tels que le premier et le denier sommet sont identique.

Un graphe est dit __connexe__ si pour chaque sommet $s$ du graphe, il existe un chemin entre $s$ et n'importe quel autre sommet du graphe.  







## Représentation d'un graphe en programmation  
On peut représenter les graphes de différentes manières en programmation, il suffit de trouver une structure de donnée adéquat pour représenter l'ensemble des sommets et des arrêtes. 

### Matrice d'adjacence  
Une première méthode est d'utiliser une matrice d'adjacence.   
La matrice est de la taille du nombre de sommet du graphe.  
On rempli cette matrice en mettant des `1`(ou `True`) à la i-ème ligne et j-ième colonne s'il existe une arrête entre les sommets i et j, sinon on mets des `0`(ou `False`) 

Exemple avec le graphe non orienté :
| 0   | 1   | 2   | 3   | 4   |
| --- | --- | --- | --- | --- |
| 0   | 1   | 1   | 1   | 0   |
| 1   | 0   | 0   | 0   | 1   |
| 1   | 0   | 0   | 0   | 1   |
| 1   | 0   | 0   | 0   | 0   |
| 0   | 1   | 1   | 0   | 0   |

<img src="img/exemple_graphe_non_oriente.png" alt="exemple_gno" width="200"/>   



Exemple avec le graphe orienté :

| 0   | 1   | 2   | 3   | 4   |
| --- | --- | --- | --- | --- |
| 0   | 1   | 0   | 1   | 0   |
| 0   | 0   | 0   | 0   | 1   |
| 1   | 0   | 0   | 0   | 1   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |


<img src="img/exemple_graphe_oriente.png" alt="exemple_go" width="200"/>   

### Liste d'adjacence


## Algorithmique sur les graphes    

### Parcours de graphe  
1. En profondeur d'abord  
2. En largeur d'abord   

### Détection de cycle  


### Recherche d'un chemin dans un graphe    
