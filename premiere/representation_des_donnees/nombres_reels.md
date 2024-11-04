# Représentation des nombres réels  

## Représentation à virgule fixe  
Un nombre à virgule fixe est composé de deux parties.  
La partie entère qui se situe avant la virgule et la partie fractionnaire qui se situe après la virgule.    
Par exemple le nombre `11,011` à pour partie entière `11` et pour partie fractionnaire `011`.  

### Lire un nombre à virgule fixe  
Il est possible d'écrire des nombres à virgule en binaire.  
La représentation à virgule fixe est la plus simpliste.  

Voici un nombre écrit en binaire représenté en virgule fixe.    
`1011, 101`.    
Pour lire ce nombre il suffit d'employer la même méthode que pour lire un nombre entier écrit en binaire.    
A noter que les nombres à droite de la virgule représente des puissances de 2 négatives !  

Ainsi pour lire ce nombre nous devons effectuer le calcul suivant :   
$1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 + 1 \times 2^{(-1)} + 0 \times 2^{(-2)} + 1 \times 2^{(-3)}$  
$8 + 2 + 1 + 0.5 + 0.125$    
$11.625$  
 

### écrire un nombre à virgule fixe  

Pour écrire un nombre à virgule fixe il y à 2 étapes.   
1. La première consiste à écrire la partie entière du nombre. Pour se faire on utilise la méthode des  divisions successives.   
2. La deuxième consite à effectuer des multiplications successives sur la partie fractionnaire.    
Pour la partie fractionnaire on effectue des multiplications successives en prenant uniquement la partie fractionnaire.      
Voici les étapes à effectuer.    
On récupère la partie fractionnaire.    
On la multiplie par 2.   
Le nombre obtenu possède :  
    - une partie entière, c'est le bit qui va être utilisé dans notre représentation.    
    - une partie fractionnaire qu'il faut à nouveau multiplier par 2    

On réitère l'opération jusqu'à ce que la partie fractionnaire soit 0 ou que l'on tombe sur une cycle d'opérations.    



Exemple avec `10,375` :
Partie entière : `1010`

Partie fractionnaire : 
`0.375 * 2 = 0.75` la partie entière est 0 donc on rajoute un 0 après la virgule et la partie entière est 0.75 on va maintenant la multiplier par 2.  
`0.75 * 2 = 1.5` la partie entière est 1 donc on rajoute un 1 après la virgule et la partie entière est 0.5 on va maintenant la multiplier par 2.  
`0.5 * 2 = 1.0` la partie entière est 1 donc on rajoute un 1 après la virgule et la partie entière est 0 donc on sarrête !  

On à donc pour la partie fractionaire `011`.  

Ainsi la représentation en virgule fixe de `10,375` est `1010,011`
