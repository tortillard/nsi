# Représentation des nombres entiers signes dans une machine  

Pour représenter les nombres entiers signés (càd qui possèdent un signe exemple `-7`) nous allons observer 2 façons de procéder.  

## Représentation avec un bit de signe  

### Explications  

La première façon consiste à dédier un bit dans notre écriture qui est associé au signe de nombre que l'on souhaite représenter.   

- Il nous faut donc premièrement convenir sur combien de bits nous voulons écrire un nombre.   
- Le bit le plus à gauche servira de bit de signe. Si ce bit est à 1 cela correspondra au signe négatif, s'il est à zéro cela correspondra au signe positif.  
- Enfin le reste des bits sert à représenter le nombre entier sans signe(en valeur absolue)  
 
Exemple 1:       
Écrire sur 5 bits la représentation avec un bit de signe du nombre -4   

|      Position des bits      | Bit de signe | 4ème bit de la représentation de 4 | 3ème bit | 2ème bit | 1er bit |
| :-------------------------: | :----------: | :--------------------------------: | :------: | :------: | :-----: |
| Représentation du nombre -4 |      1       |                 0                  |    1     |    0     |    0    |

La représentation sur 5 bits avec un bit de signe du nombre -4 est `10100`  


Exemple 2:       
Écrire sur 8 bits la représentation avec un bit de signe du nombre 11     

|      Position des bits      | Bit de signe | 7ème bit de la représentation de 11 | 6ème bit | 5ème bit | 4ème bit | 3ème bit | 2ème bit | 1er bit |
| :-------------------------: | :----------: | :---------------------------------: | :------: | :------: | :------: | :------: | :------: | :-----: |
| Représentation du nombre 11 |      0       |                  0                  |    0     |    0     |    0     |    1     |    1     |    1    |

La représentation sur 8 bits avec un bit de signe du nombre 11 est `00000111`  


Un octet est l'association de 8 bits, cette unité est beaucoup utilisé en informatique.  
On à tendance à représenter les nombres sous forme de multiple d'octet(multiple de 8 bits).  
C'est pour cela que les tailles de 8, 16, 32 ou 64 bits sont les plus courantes pour représenter les entiers.  

### Inconvénients  
La représentation avec un bit de signe pose plusieurs inconvénients.

- Premièrement nous avons deux représentations du nombre `0` :

|   Position des bits    | Bit de signe | 7ème bit de la représentation de 11 | 6ème bit | 5ème bit | 4ème bit | 3ème bit | 2ème bit | 1er bit |
| :--------------------: | :----------: | :---------------------------------: | :------: | :------: | :------: | :------: | :------: | :-----: |
| Représentation de `-0` |      1       |                  0                  |    0     |    0     |    0     |    0     |    0     |    0    |
| Représentation de `+0` |      0       |                  0                  |    0     |    0     |    0     |    0     |    0     |    0    |


- Deuxièmement l'opération d'addition(pour ne citer qu'elle) ne donne pas de résultat cohérent :
Normalement `4 + (-3) = 1`, or si on prends la représentation avec un bit de signe sur 8 bit de `4` et `-3` on obtient respectivement `00000100` et `10000011`. 
On pose l'addition suivante avec la représentation binaire de ces nombres. 

| Position des bits | Bit de signe | 7ème bit de la représentation de 11 | 6ème bit | 5ème bit | 4ème bit | 3ème bit | 2ème bit | 1er bit |
| :---------------: | :----------: | :---------------------------------: | :------: | :------: | :------: | :------: | :------: | :-----: |
|                   |      0       |                  0                  |    0     |    0     |    0     |    1     |    0     |    0    |
|         +         |      1       |                  0                  |    0     |    0     |    0     |    0     |    1     |    1    |
|         =         |      1       |                  0                  |    0     |    0     |    0     |    1     |    1     |    1    |

L'addition nous donne le résultat `10000111` que nous lisons `-7` ce résultat est évidemment faux, comme dit précédemment nous devrions obtenir `1`.  


Une autre représentation des nombres entiers signés permet de régler ce problème...



## Représentation avec le complément à 2  

Il y a certaines étapes à suivre afin de représenter un nombre en complément à 2.  
Initialement on donne une taille sur laquelle on souhaite représenter nos nombres (8 bits, 16 bits, etc ...).    
Ensuite 2 possibilités s'offrent à nous.  
    - Soit on souhaite représenter un nombre positif :    
      - Dans ce cas la, on le représenter en binaire comme d'habitude    
    - Soit on souhaite représenter un nombre négatif :   
      - Premièrement on prends la représentation positif de ce nombre   
      - On inverse tout les bits, c'est à dire qu'on change les `0` en `1` et les `1` en `0`    
      - Puis on ajoute 1 au résultat précédent  

Exemple :  
On souhaite représenter en binaire le nombre `-11` sur 5 bits en complément à 2.    

- On représente le nombre `11` en binaire sur 5 bits cela nous donne `01011`    
- On inverse chaque bit de cette représentation autrement dit on passe de `01011` à `10100`   
- Enfin on ajoute 1 au résultat on passe donc de `10100` à `10101`  

La représentation de `-11` en binaire sur 5 bits en complément à 2 est `10101`.      
Autrement dit, si on additionne `01011`(c'est à dire 11) et `10101`(c'est à dire -11) nous devrions obtenir 0.    
Vérifions :  



| Position des bits | bit pour réprésenter la retenue | 5ème bit | 4ème bit | 3ème bit | 2ème bit | 1er bit |
| :---------------: | :-----------------------------: | :------: | :------: | :------: | :------: | :-----: |
|                   |                                 |    0     |    1     |    0     |    1     |    1    |
|         +         |                                 |    1     |    0     |    1     |    0     |    1    |
|         =         |                1                |    0     |    0     |    0     |    0     |    0    |

On obtient bien 0 sur 5 bits lorsque l'on additionne la représentation de `11` et `-11`.  
