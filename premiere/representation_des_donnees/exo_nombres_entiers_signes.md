## Exercice 1    
 
1. En complément à deux, quel intervalle d’entiers relatifs peut-on représenter avec des mots de 8 bits ?   Combien de valeurs sont représentées ?    
 
2. Même question avec des mots de 32 bits et 64 bits.     


## Exercice 2    
Dans cet exercice, on utilise un codage en complément à 2 sur 4 bits.  

1. Quels sont les nombres minimum et maximum que l’on peut représenter ?  

2. Compléter le tableau :    
   
| Décimale | Complément à 2 |
| :------: | :------------: |
|    -8    |                |
|    -5    |                |
|    -1    |                |
|    0     |                |
|    3     |                |
|          |      0111      |
|          |      1001      |
|          |      1100      |

## Exercice 3  

1. Donnez la représentation en complément à 2 sur 1 octet de 0 et -128
2. Donnez la représentation en décimale des nombres `0000 1000` et `1000 1000` écrit en complément à 2.  
3. Donnez la représentation en décimale des nombres 96 et 48 sur 1 octet. Faites l'addition entre ces deux nombres. Vous obtenez un résultat écrit en complément à 2.  
4. Donnez la représentation en décimale du résultat obtenu à la question 3. Que remarquez-vous ? 



## Exercice 4  
Posez et verifiez chaque calculs en représentant les nombres négatifs en complément à 2.  

1. 34+(-27)
2. 75+(-43)
3. 60+(-100)
4. 127+(-128)


# Programmation Python  

## Remarques sur les chaines de caractères    
1. Prenons une chaine de caractères `mot="Bonjour"` il est possible de récupérer 1 caractère de cette chaine à partir de son indice en utilisant des crochets. `mot[2]` va renvoyer `"n"` puisque c'est le caractère qui se trouve à l'indice 2(les indices commencent à partir de 0).    

2. On peut également récupérer _des morceaux_ d'une chaine de caractères en mettant entre crochets les indices de début et de fin(-1) du morceau souhaité. Par exemple `mot[2:4]` va renvoyer `"nj"` car on à récupérer le morceau de la chaine de caractère commencant à l'indice 2 et se terminant à l'indice 4-1 c'est à dire 3.  

## Exercice 5  
écrivez une fonction qui prend un nombre écrit en binaire et qui renvoi sa valeur en décimale.
Voici la signature de la fonction `convertit_en_decimale(n_binaire : str) -> int`.  

`convertit_en_decimale("1011")` doit donner `11`


## Exercice 6  
écrivez une fonction qui prend un nombre écrit en binaire avec une représentation en bit de signe et qui renvoi sa valeur en décimale.
Voici la signature de la fonction `convertit_en_decimale_bit_de_signe(n_binaire : str) -> int`.  

`convertit_en_decimale_bit_de_signe("1011")` doit donner `-3`



## Exercice 7  
Il existe une technique qui permet de représenter les nombres négatifs en complément à 2 plus rapidement.  
Premièrement, on écrit le nombre en binaire sans s'occuper du signe.  
Deuxièmement, on regarde dans l'écriture binaire où se situe le dernier 1 (le 1 le plus à droite).  
Enfin on réecrit le nombre en inversant tout les bits avant le dernier 1.  

Exemple : 
Si on utilise la méthode habituel pour calculer `-52`. 
On représente `52` en binaire ce qui donne `110100`.  
On inverse chaque bit ce qui donne `001011`. 
Enfin on ajoute 1 ce qui donne `001100`.  

Vérifions si notre technique donne le même résultat.
Premièrement, on écrit le nombre en binaire sans s'occuper du signe `110100`
Deuxièmement, on regarde où se situe le dernier 1. Ici il se situe à l'indice 3 (on commence à compter à partir de 0). Afin de distinguer on réecrit le nombre avec un espace marquant la position du dernier 1. Ce qui nous donne `110 100`
Enfin on réecrit le nombre en inversant tout les bits avant le 1 qui se situe à l'indice 3.  On obtient donc `001 100`.  
C'est bien le résultat obtenu auparavant.  

1. écrivez une fonction qui prend en paramètre un bit sous forme de chaine de caractère et qui renvoie l'inverse de ce bit sous forme de chaine de caractère. La signature de la fonction est la suivante `inverse(b : str) -> str`.

`inverse("1")` doit donner `"0"`


2. écrivez une fonctione qui prend en paramètre un nombre écrit en binaire sous forme de chaine de caractères et qui renvoie l'indice du dernier 1 de ce nombre. La signature de la fonction est la suivante `position_premier_un_a_droite(n_binaire : str) -> int`

`position_premier_un_a_droite("110100")` doit donner `3`


3. écrivez une fonction qui prend en paramètre un nombre négatif écrit en complément à 2 et qui renvoie sa valeur en décimale.  
La signature de la fonction est la suivante `convertit_en_decimale_ca2(n_binaire : str) -> str`.  

`convertit_en_decimale_ca2("11001011")` doit donner `-53`.