# Tri par insertion  


## Principe   

<!-- image animation -->

## Algorithme 

### Pseudo code 

### Python  

## Remarques  

Il est possible d'améliorer la complexité du __tri insertion__ en utilisant le principe de la __dichotomie__.      

Dans l'algorithme du __tri insertion__ on doit _inserer_ le nombre à l'indice `i` entre les indices `0` et `i-1` à la bonne place.      

- _Prenons par exemple la liste \[__2,3,5,7,11__,4,6\] nous somme à l'étape où 4 doit être inséré._    

Les nombres compris entre l'indice `0` et `i-1` sont tous triés !     

- _Dans notre exemple, ce sont les nombres __2,3,5,7,11__ qui sont déjà triés._    

On peut donc tirer profit de cette information afin de trouver plus rapidement la place où le nombre à l'indice `i` doit être inseré en utilisant la __dichotomie__.    

- _On cherche à placer 4 en utilisant la dichotomie dans la partie triée._   
- _On cherche dans la partie de notre liste triée le milieu, ici c'est __5__. On le compare avec le 4._    
- _Comme 4 < __5__  on réitère l'opération sur la partie __2,3__. Ici le milieu est __3__._     
- _Le nombre __3__ se trouve à l'indice 1 il faut donc insérer le nombre 4 entre l'indice 1 et 2_.    