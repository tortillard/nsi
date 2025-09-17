# Représentation des nombres réels  

## Représentation à virgule fixe  
Un nombre à virgule fixe est composé de deux parties.  
La partie entère qui se situe avant la virgule et la partie fractionnaire qui se situe après la virgule.    
Par exemple le nombre `11,011` à pour partie entière `11` et pour partie fractionnaire `011`.  

### Lire un nombre à virgule fixe  
La représentation à virgule fixe est une méthode pour représenter les nombres à virgule en binaire. 

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
1. La première consiste à écrire la partie entière du nombre. Pour se faire on utilise la méthode des divisions successives.   
2. La deuxième consite à effectuer des multiplications successives sur la partie fractionnaire.    
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





## Représentation IEEE - 754  

### écrire un nombre en représentation IEEE - 754  

Pour représenter un nombre en utilisant la norme IEEE-754, il faut suivre plusieurs étapes. Nous utiliserons le format simple précision (32 bits) pour représenter nos nombres.      

Le but est de représenter notre nombre sur 32 bits dont :  
    - s : le signe est sur 1 bit   
    - e : l'exposant biaisé est sur 8 bits  
    - M : la mantisse sur 23 bits  

Voici les étapes pour trouver s,e et M.  


### Étapes pour représenter un nombre en IEEE-754

#### Déterminer le signe (s)

- **Signe (1 bit)** :   
  - Si le nombre est positif, le bit de signe est `0`.  
  - Si le nombre est négatif, le bit de signe est `1`.  

#### converion en binaire du nombre en méthode de virgule fixe   
Convertir le nombre en binaire  

- **Partie entière** : Convertissez la partie entière du nombre en binaire avec la méthode des divisions successives.  
- **Partie fractionnaire** : Convertissez la partie fractionnaire en binaire avec la méthode des multiplications successives.  

**Exemple** : Pour le nombre 6,25  
- Partie entière : 6 en binaire est `110`.  
- Partie fractionnaire : 0.25 en binaire est `0,01` (0,25 * 2 = 0,5 → 0, puis 0,5 * 2 = 1,0 → 1).  

Donc, 6,25 en binaire est `110,01`.  

La mantisse et l'exposant s'obtiennent en normalisant notre nombre écrit en binaire.    
Normaliser un nombre signifi l'écrire sous la forme `1, ....`.    
Dans notre exemple 6,25 se note `110,01`.   

Lorsque l'on normalise ce nombre cela nous donne `1,1001`.   
On peut dire que 6,25 = 1,__1001__ * 2^__2__.    

###  Déterminer la mantisse (m)

La mantisse correspond aux nombres après la virgule auquel il faut ajouter des 0 superflux pour correspondre aux nombres de bit de la représentation.     
On doit avoir une représentation sur 23 bits au total.  
Comme on à que 4 bits après la virgule il faut rajouter 19 fois le bit `0`.    
Ainsi m vaut `10010000000000000000000`.  
  


###  Déterminer l'exposant biaisé (e)
L'exposant biaisé correspond au nombre de décalage de la virgule qu'il à fallut pour normaliser notre nombre auquel il faut ajouter le biais de 127.      

Dans notre cas on à eu un exposant de `2` auquel il faut ajouter le biais de `127` ce qui donne `129`.    
Convertissons 129 en binaire : 129 en binaire est `10000001`.
Ainsi e vaut `10000001`


### Assembler le tout  

Maintenant, nous avons tous les composants pour assembler le nombre en format IEEE-754 :

- **Signe(s)** : `0`    
- **Exposant(e)** : `10000001`    
- **Mantisse(M)** : `10010000000000000000000`    

En combinant ces trois parties, nous obtenons : `0 10000001 10010000000000000000000`  



