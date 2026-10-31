# TP - Le musée  

Nous allons écrire le programme qui permet de gérer l'organisation d'un musée.
Pour cela, nous serons amené à nous occuper des tarifs des visiteurs, les réductions éventuelles etc...  

## Tarifs  

Le musée applique les tarifs suivants.  
- 6 ans ou moins : __gratuit__ 
- de 6 à 17 ans inclus : __5€__ 
- de 18 à 64 ans inclus : __10€__ 
- 65 ans ou plus : __7€__

> [!IMPORTANT]  
> __Q1__ : écrire une fonction `tarif_musee` qui prend en paramètre `age` de type `int` et qui renvoie le __tarif__ correspondant de type `int`. 


## Réduction édutiante  

Un tarif étudiant peut s'appliquer afin de modifier le tarif.  
Une réduction de 2€ s'applique aux personnes étudiantes.    
__Attention__ le prix ne doit pas être inférieur à 0.  

> [!IMPORTANT]  
> __Q2__ : écrire une fonction `tarif_musee_reduc_etu` qui prend en paramètre  
> - `age` de type `int`  
> - `etu` de type `bool`  
> Cette fonction fait exactement le même travail que la fonction `tarif_musee` à l'exception qu'elle renvoie le tarif diminué de 2€ si `etu` vaut `True`.  
> Si `etu` vaut `False` le tarif ne s'applique pas.   


## Vérification du billet  

Avant d'entrer voir les oeuvres du musée, le visiteur doit se rendre au point de vérification.  
Au point de vérification, une personne demande au visiteur si
- il possède un billet   
- quel est l'âge noté sur le billet du visiteur  

> [!IMPORTANT]  
> __Q3__ : écrire une fonction `verif_billet` qui prend en paramètre    
> - `possede_billet` de type `bool`    
> - `age` de type `int`    
> Cette fonction doit renvoyer une chaine de caractères. 
> Si `possede_billet` vaut `True` et `age` est compris entre `0` et `140` alors on renvoi `"Billet valide"`.       
> Si `age` est inférieur à `0` ou supérieur à `140` on renvoi `"Age invalide sur le billet"`.  
> Sinon dans les autres cas on renvoi `"Billet invalide"`.  


## Activités dans le musée  

Des activités supplémentaire sont disponible dans le musée.  
Voici le menu des activités proposées.  

| Code  |  Activité  | Prix  |
| :---: | :--------: | :---: |
|   1   | Exposition |  2€   |
|   2   |  Atelier   |  4€   |
|   3   |   Guide    |  9€   |

> [!IMPORTANT]  
> __Q4__ : écrire une fonction `activite_sup` qui prend en paramètre `code` de type `int`. Cette fonction doit 
> - __afficher__ le nom de l'activité
> - __renvoyer__ le prix de l'activité de type `int`  


## Scénario  

Sans utiliser la fonction de la __Q1__ utiliser toutes les autres fonctions écrites pour répondre aux questions suivantes.  

> [!IMPORTANT]  
> __Q5__ : écrire une fonction `scenario_1` qui ne prend aucun paramètre et traduis le scénario suivant.
> - Un personne étudiante de 23 ans achète un billet.   
> - Son billet est vérifié.   
> - Elle décide en supplément de faire appel à un guide  

> [!IMPORTANT]  
> __Q6__ : écrire une fonction `scenario_1` qui ne prend aucun paramètre et traduis le scénario suivant.
> - Une personne de 16 ans achète un billet.   
> - Son billet est vérifié.   
> - Elle décide en supplément de faire une exposition 