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
    4. on ajoute éventuellement des paramètres séparés par des `,`
    5. on ferme la parenthèse   
    6. __/!\ on ajoute `:` au bout de la ligne /!\\__  
    7. on passe une ligne et on appuie sur la touche tabulation <img src="img/touche_tabulation.png" alt="drawing" width="30"/> pour commencer à écrire le code de notre fonction
    8. Enfin, comme une fonction renvoie un résultat dans la __majorité__ des cas, la dernière ligne de notre programme doit commencer par le mot clé `return` suivi du résultat à renvoyer.          

Exemples : 
```Python
def une_fonction_sans_parametre():
    a = 2
    return a 

def mon_addition(a, b):
    return a + b

def une_fonction_qui_ne_renvoie_rien(phrase):
    print(phrase)

# La fonction print() affiche un message dans la console mais ne renvoie rien 
# C'est en utilisant le mot clé return que l'on renvoie un résultat

```  
## Notation de type  

Pour plus de précision sur les informations de notre fonction il est courant d'utiliser une notation de type.  
La notation de type permet d'indiquer au développeur qui utilise une fonction, quels sont les types des paramètres et le type de retour du résultat.   
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
    - du nom de la fonction 
    - le nom et le type des paramètres 
    - le type du résultat renvoyé   

Par exemple la signature de la fonction `mon_addition` est `mon_addition(a : int, b : int) -> int `.  


## Paramètre  

Un __paramètre__ est une variable qui peut être utilisée à l'intérieur de la fonction.   
__L'argument__ est la valeur associée au paramètre.  
On sépare chaque paramètre par une virgule `,`.  


Exemple :
```Python
def une_fonction_avec_4_parametres(nom, prenom, age, ville):
    age_en_str = str(age)
    return "Je m'appelle " + prenom + " " + nom + " , j'ai "+ age_en_str + " ans et j'habite à " + ville  
```



## Renvoi 

Le mot clé `return` est très important. Il permet de renvoyer le résultat d'une fonction. 
Quand une fonction renvoie un résultat il est possible de réutiliser le résultat renvoyé.  

Par exemple la fonction `str(donnee)` renvoi `donnee` en convertissant son type en `str`.  
On peut donc récupérer le résultat renvoyé, en le stockant dans une variable par exemple.  

Exemple : 
```Python
nombre_de_points = 5
nombre_de_points_en_str = str(nombre_de_points)
 
# on stocke le résultat de la fonction str dans la variable nombre_de_points_sous_en_str

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
