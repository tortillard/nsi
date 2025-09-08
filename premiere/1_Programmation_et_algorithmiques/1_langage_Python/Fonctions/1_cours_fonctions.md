# Les fonctions  

## Définition   
Une fonction est une séquence d'instructions __réutilisable__ à laquelle est associée __un nom__.  

En Python, on distingue une fonction d'une variable car une fonction possède __des parenthèses__.  

Vous avez déjà utilisé des fonctions déjà contenues dans Python. 
Par exemple la fonction `int()` permet de convertir en `int` une valeur.


## Définir une fonction  

On peut évidemment définir nos propres fonctions. 
Pour cela il faut :  
1. utiliser le mot clé `def`  
2. mettre un espace puis le nom que l'on souhaite attribuer à notre fonction  
3. on ouvre une parenthèse  
4. on ajoute éventuellement un paramètre, s'ils y'en à plusieurs on les sépare par des `,`    
5. on ferme la parenthèse   
6. __/!\ on ajoute `:` au bout de la ligne /!\\__  
7. on passe une ligne et on appuie sur la touche tabulation <img src="img/touche_tabulation.png" alt="drawing" width="30"/> pour commencer à écrire le code de notre fonction.    
8. Enfin, une fonction renvoi __TOUJOURS__ un résultat. On peut préciser ce résultat à l'aide du mot clé `return` suivi du résultat à renvoyer. Si on ne précise pas le renvoi alors la fonction renverra automatiquement `None`.  

Exemples : 
```Python
def une_fonction_sans_parametre():
    a = 2
    return a 

def mon_addition(a, b):
    return a + b

def une_fonction_qui_renvoie_none(phrase):
    nouvelle_phrase = phrase + " ? "
    print(phrase)
```  

## Notation de type  

Pour plus de précision sur les informations de notre fonction il est courant d'utiliser une notation de type.  
La notation de type permet d'indiquer au développeur qui utilise une fonction, quels sont les __types des paramètres__ et le __type de retour__ du résultat.   
On note :    
- Le type des paramètres est précisés en ajoutant `:` suivi du type (exemple `int`,`str`,`bool`, ...  )   
- Le type de la valeur de retour est précisé en ajoutant `->` juste après avoir fermé la parenthèse, suivi du type  

Exemple :  
```Python
# Une fonction sans notation de type 
def mon_addition(a, b):
    return a + b

# La même fonction avec notation de type 
def mon_addition(a : int, b : int) -> int :
    return a + b

```

## Signature d'une fonction  

La signature d'une fonction est le condensé des _informations importantes_ de celle-ci. La signature d'une fonction est composée     
- du __nom de la fonction__   
- le __nom et le type des paramètres__   
- le __type du résultat renvoyé__     

Par exemple la signature de la fonction `mon_addition` est `mon_addition(a : int, b : int) -> int `.  


## Paramètres  

Un __paramètre__ est une __variable__ qui peut être réutilisée à l'intérieur de la fonction.  
__L'argument__ est la valeur associée au paramètre.  
On sépare chaque paramètre par une virgule `,`.  


Exemple :
```Python

# Ecriture d'une fonction avec 4 paramètres  

def une_fonction_avec_4_parametres(nom, prenom, age, ville):
    age_en_str = str(age)
    return "Je m'appelle " + prenom + " " + nom + " , j'ai "+ age_en_str + " ans et j'habite à " + ville  

# Appel de cette fonction  
# Le paramètre 'nom' à pour argument 'Jin'
# Le paramètre 'prenom' à pour argument 'Mya'
# etc...
resultat = une_fonction_avec_4_parametres("Jin", "Mya", 35, "Arras")

```



## Renvoi 

Le mot clé `return` est très important. Il permet de spécifier le renvoi d'une fonction. 
Il est possible de réutiliser le résultat renvoyé d'une fonction dans notre code.    

Par exemple, la fonction `str` prend en paramètre une donnée et convertit son type en `str`.  
On peut donc récupérer le résultat renvoyé, en le stockant dans une variable par exemple.  

Exemple 1: 
```Python
nombre_de_points = 5
nombre_de_points_en_str = str(nombre_de_points)
 
# on stock le résultat de la fonction str(nombre_de_points) dans la variable nombre_de_points_en_str

```

Exemple 2: 
```Python
def calcul_math(x):
    return (x+2)*(x/4)

resultat = calcul_math(7)

# on stock le résultat de la fonction calcul_math(7) dans la variable resultat

```


## Appel de fonction  
Lorsqu'on utilise une fonction on dit que l'on __appelle la fonction__. 
Pour appeler une fonction il suffit :  
- d'écrire son nom      
- ouvrir la parenthèse       
- __donner une valeur aux paramètres(si la fonction possède des paramètres)__       
- fermer la parenthèse      


Exemple :
```Python
# appel de la fonction écrite dans la section "Paramètre"
infos_perso = une_fonction_avec_4_parametres("Turing", "Alan", 41, "Londres")

# il est également possible de donner des variables en paramètre qui contiennent des valeurs  
prenom_entre = "Turing"
nom_entre = "Alan"
age_entre = 41 
ville_entre = "Londres"  
infos_perso = une_fonction_avec_4_parametres(prenom_entre, nom_entre, age_entre, ville_entre)  
```
