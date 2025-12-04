# Files  

## Types de donées abstraits  
Les __Files__ sont une structure de données linéaire.  
Elles permettent de stocker différents types de données.  

L'utilisation et la manipulation d'une __File__ en informatique et sensiblement la même _qu'une file de fichier à imprimer_ ou _une file de personnes à la caisse au supermarché_

<!-- img d'une file  -->

> [!TIP]   
> - Il est possible d'accéder __uniquement__ au premier élément de la __File__  
> - Les éléments d'une __File__ ne possèdent pas d'indice   
> - Pour accéder à un autre élément de la __File__ il faut que les éléments devant lui soit sortie de la File(défiler)  
> - Lorsqu'un élément vient s'ajouter il se met à la fin de la __File__  

> [!TIP] FIFO  
> On dit que les __Files__ sont des structures de données de type __FIFO__  
> __First In First Out__ (le premier entrant est le premier sortant)  

## Python 

Le type __File__ n'existe pas _nativement_ en Python, plusieurs manières de le représenter existe.    
- En utilisant les bibliothèques `collections.deque`, `queue.Queue`, ...    
- En écrivant une classe __File__    

Nous nous interessons principalement à cette seconde manière en terminale.   

> [!NOTE] Remarque  
> A travers les TPs, interrogations ou sujets de bacs différents que vous allez voir, le choix utilisé pour représenter les __Files__ peut être différent.   
> Parfois avec une classe écrite différemment de celle du cours, parfois sans définir de classe, ...  

<!-- écriture de la lcasse Pile ???? -->
```Python

```
