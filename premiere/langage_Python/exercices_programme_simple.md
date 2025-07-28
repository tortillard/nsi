# Programme simple    
 
## Fonctions utiles 

Certaines de ces fonctions sont utiles pour les exercices suivants. Utilisez les quand cela est __nécessaire__.

> __Lorsqu'il est écrit 'afficher' dans une consigne on utilise la fonction `print(contenu_a_afficher)`__  

> __Fonctions `int(donnee)` et `str(donnee)`__. 
> Ces fonctions permettent de convertir __le type__ de la donnée prise en entrée. 
> Ainsi `int(donnee)` convertit `donnee` en `int` de même `str(donnee)` convertit `donnee` en `str`. 

> __Fonction `resultat = input(texte)`__ 
> Cette fonction permet de récupérer un `resultat` entrée par un utilisateur. Il est possible d'ajouter du `texte` pour préciser ce que l'on souhaite attendre de l'utilisateur. 
> Exemple : `age_sous_forme_de_chaine_de_caractere = input("Quel est votre âge ?")` 
> __Attention__ : le résultat obtenu par la fonction `input` est de type `str`



## Opérateurs arithmétique 

### 1.  
Écris un programme qui stocke la valeur `4` dans une variable `a`, la valeur `-7` dans une variable `b` et qui additionne le contenu de `a` et `b` dans une variable `c`. Enfin, affiche le résultat.  


### 2. 
Écris un programme qui stocke la valeur `4` dans une variable `a` ajoute à cette variable la valeur `-7`, multiplie `a` par `-3`, puis retire `1` enfin, divise par `2` le résultat et affichez le. 

### 3.  
Écris un programme qui stocke la valeur `2` dans une variable `a` et la valeur è `7` dans la variable `b`. Puis écrivez les instructions nécessaire pour permuter les valeurs de `a` et `b`. 

### 4.
Écris un programme qui stocke dans une variable `nom` votre nom, dans une variable `prenom` votre prénom et affiche la phrase suivante `Bonjour je m'appelle (prenom) (nom)` 


### 5.  
Écris un programme qui stocke votre age dans une variable `age` et qui affiche la phrase suivante.
`Vous avez (age) ans`. En remplaçant `(age)` par la valeur de la variable `age`.  

### 6
Écris un programme qui stocke la valeur `10` dans une variable `numerateur`, la valeur `3` dans une variable `denominateur`.  
Stocke dans la variable `quotient` le quotient de la division euclidienne de `numerateur` par `denominateur`et dans la variable `reste` le reste.  
Enfin, affiche la phrase suivante `La division de (numerateur) par (denominateur) à pour quotient (quotient) et pour reste (reste)`.  
En remplaçant les mots entre parenthèses par les variable associées.  


### 7. 
Réecrivez en Python les expressions arithmétiques suivantes en attribuant au préalable les valeurs `-3`, `-9` et `11` aux variables `a`, `b`, `c` et `d` puis affichez le résultat:  
  1. $(a - b)^2$
  2. $(a^2 + 2ab + b^2)$
  3. $\frac{a+c}{c+d}$
  4. $\frac{3}{c+4}$


### 8.  
Après avoir cherchez sur internet comment passer d'une température en degré Celsius en degré Farenheit, écris un programme qui demande à l'utilisateur d'entrer une température en degrés Celsius, faites le calcul nécessaire pour la convertir en Farenheit et affichez la phrase suivante `(temperature_en_celsius) degré Celsius équivaut à (temperature_en_farenheit) degré Farenheit`.  

nb : voir dans la section __Fonctions utiles__  pour l'utilisation de la fonction `input()` qui permet de demander à un utilisateur de saisir un résultat.  




## Comparaisons et booléens  

### 9.
Écris un programme qui demande à l'utilisateur d'entrer un nombre. Si le nombre est positif strictement, le programme doit afficher `False`, sinon il doit afficher `True`. 


### 10.
Écris un programme qui demande à l'utilisateur d'entrer deux nombres. Le programme doit afficher `True` si le premier nombre est strictement positif et le deuxième nombre inférieur ou égal à 0, sinon il doit afficher `False`



### 11.
Écris un programme qui demande à l’utilisateur de saisir un nombre et utilisez l’opérateur modulo (%) pour vérifier sa parité(c'est à dire si un nombre est pair ou non) on affichera `True` si le nombre est pair et `False` sinon.


### 12.
Créez deux variables booléennes, `a` et `b`, qui prennent respectivement les valeurs `True` et `False`.  
Affichez le résultat :  
  - L'opérateur `not` sur la variable `a`  
  - Les opérateur `and` et `or` sur les variables `a` et `b`  



### 13.
Écris un programme qui demande à l'utilisateur d'entrer trois nombres. Le programme doit afficher `True` si :
  - Le premier nombre est positif __ou__
  - Le deuxième nombre est négatif __et__ le troisième nombre est nul 
Sinon, le programme doit afficher `False`.

### 14.  
Écris un programme qui demande à l'utilisateur d'entrer trois nombres. Le programme doit afficher `True` si :  
  - La condition suivante est fausse "le premier nombre est supérieur à 5 et le deuxième nombre est inférieur à 7" __ou__  
  - Le  troisième nombre est égal à 3  



## Conditions 


### 15.
__Écrivez une fonction__ qui demande à un utilisateur de rentrer son age et qui __renvoie__ `Vous êtes majeur` si l'âge entrée est supérieur ou égal à 18 ans ou `Vous êtes mineur` sinon. 

### 16.  
__Écrivez une fonction__ qui demande à l'utilisateur de saisir un nombre, et qui __renvoie__ `Positif`, `Négatif` ou `Nul` selon le nombre entré.  


## 17.    
Demandez à l'utilisateur de saisir deux nombres, puis comparez-les et __renvoyer__ `plus grand`, `plus petit` ou `égal` si le premier est plus grand, plus petit ou égal au second.


### 18.  
__Écrivez une fonction__ dans laquelle se cache un nombre secret (par exemple 7), puis demandez à l'utilisateur de saisir un nombre. Indiquez si le nombre saisi est plus petit, plus grand ou égal au nombre secret.  

## 19.  Jeu du Molky   
__Écrivez une fonction__ qui demande d'abord à l'utilisateur le score précédent et le nombre de points marqués à ce tour, calcule la somme de ces deux valeurs, puis choisit une alternative parmi trois en fonction de la valeur de cette somme.  
Si le score de 51 est atteint la victoire est annoncée, sinon, si ce score n'est pas dépassé alors le nouveau score est la somme calculée, et sinon enfin, c'est-à-dire si le score de 51 est dépassé, alors le nouveau score est de 25.  

## 20.  Bowling V1  
Au Bowling on a deux chances pour faire tomber un total de dix quilles.   
Écrivez une fonction qui demande le nombre de quilles renversées avec chacune des deux boules et renvoie `X` si toutes les quilles sont tombées à la première boule, `/` si toutes les quilles sont tombées(à la deuxième boule) et sinon le nombre de quilles renversées.   

## 21.  Bowling V2  
Reprendre l'exercice précédent en ne demandant les informations de la deuxième boule que si elle a besoin d'être lancée.  

## 22.  Bowling V3  
Reprendre l'exercice précédent en renvoyant `!` si les scores saisis sont impossibles.  

## 23. Polynôme du second degré  
Écrivez une fonction qui prend 3 paramètres en entrée. `a`, `b` et `c` et qui résouds l'équation $ax²+bx+c = 0$

## 24. Billard  
On considère un billard dont les dimensions sont données par les variables `longueur` et `largeur`, avec une seule bille de coordonnées $(x, y)$ en supposant que le coin inférieur gauche a les coordonnées $(0,0)$ et le coin supérieur droit les coordonnées $(longueur, largeur)$.  
Après application d'un vecteur de déplacement $(d_x, d_y)$ les nouvelles coordonnées de la bille sont $(x + d_x, y + d_y)$, si ce déplacement n'implique pas de transpercer une paroi de billard.  
Sinon, la bille effectue un rebond parfait sur chacune des parois rencontrées : la nouvelle direction est symétrique de l'ancienne par rapport à la paroi sur laquelle la bille rebondit, et la distance restant à parcourir est inchangée.   

Écrivez une fonction qui demande les coordonnées de labille et un vecteur de déplacement $(d_x, d_y)$, pour lequel on supposera $-longueur \leq d_x \leq longueur$ et $-largeur \leq d_y \leq largeur$, et qui renvoie les coordonnées de la bille à la fin du mouvement.  

  



