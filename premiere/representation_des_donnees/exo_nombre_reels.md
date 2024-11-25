## Exercice 1  
Convertissez en décimale les nombres suivants écrits en binaire avec une représentation à virgule fixe : 

- `0011,1100`  
- `1100,0101`  
- `0001,1010`  
- `101, 1011` 


## Exercice 2  

Convertissez les nombres décimaux suivants en binaire en utilisant une représentation à virgule fixe :  

- `6,25`    
- `3,75`   
- `2,5`  
- `1,625`
- `3,40625`  


## Exercice 3

Effectuez les opérations suivantes en utilisant une représentation à virgule fixe :   

- `2.5 + 1.75`  
- `3.25 - 1.5`  


## Exercice 4  

- Donnez la représentation en virgule fixe du nombre `3,11`. Combien de chiffre après la virgule est-il raisonnable de représenter ?
-  Donnez la représentation en virgule fixe du nombre `0,1`, `0,25`, `0,3`.  Même question ?  
- Reprenez le nombre obtenu écrit en virgule fixe à la question précédente et calculez sa valeur, en vous servant de Python comme calculatrice. Quel résultat obtenez vous ?     


# Exercices de programmation 
### Exercice 5 
1. Programmez une fonction qui permet de récuperer la partie entière d'un nombre à virgule. Voici la signature de la fonction `recup_partie_entiere(nombre_a_virgule : float) -> int`.

L'appel de `recup_partie_entiere(3.5)` doit renvoyer `3`

2. Programmez une fonction qui permet de récupérer la partie fractionnaire d'un nombre à virgule à partir de sa partie entière. Voici la signature de la fonction `recup_partie_fractionnaire(nombre_a_virgule : float, partie_entiere : int) -> float`.  

L'appel de `recup_partie_entiere(3.5, 3)` doit renvoyer `0.5`

3. Programmez une fonction qui permet de donner la représentation en virgule fixe avec 10 bits après la virgule d'un nombre flottants entrez en paramètre. Voici la signature de la fonction `virgule_fixe(nombre_a_virgule : float) -> str`

L'appel de `virgule_fixe(3.5)` doit renvoyer `"11,1000000000"`
L'appel de `virgule_fixe(1.625)` doit renvoyer `"1,1010000000"`



### Exercice 6 
1. Reprenez la fonction suivante et ajoutez la dans votre programme. 
```Python
def convertit_en_decimale(n_binaire : str) -> int:
	res = 0
	taille_mot = len(n_binaire)
	for i in range(taille_mot):
		decalage = taille_mot-1
		res = res + int(n_binaire[i])*(2**(decalage-i))
	return res
```

2. Programmez une fonction qui prend en entrée la partie fractionnaire d'un nombre à virgule écrit en binaire. Cette fonction doit renvoyer la valeur de la partie fracionnaire.  Voici la signature de la fonction `convertit_en_decimale_fractionnaire(n_binaire_fractionnaire : str) -> int`.  

L'appel de `convertit_en_decimale_fractionnaire("1000")` doit renvoyer `0.5`.  

Astuce : Vous pouvez grandement vous inspirer du code de `convertit_en_decimale` pour écrire votre programme.  


3. Programmez une fonction qui prend en entrée une représentation à virgule fixe d'un nombre en binaire sous forme de chaine de caractères. Cette fonction doit renvoyer sa valeur en décimale.   
Voici la signature de la fonction `decimale_vers_virgule_fixe(repr_avec_virgule : str) -> float`

L'appel de `decimale_vers_virgule_fixe("11,110000")` doit renvoyer `3.75`.  
L'appel de `decimale_vers_virgule_fixe("11,110000")` doit renvoyer `19.1875`.  

Astuce : La méthode `chaine.find(c)` permet d'obtenir l'indice du caractère `c` dans `chaine`. Par exemple `"Bientot Noël !".find("n")` va renvoyer `3`.  

