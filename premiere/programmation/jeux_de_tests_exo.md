# Exercice sur les tests en Python  

## Exercice 1  
1. Ouvrez votre éditeur de code et importer le module doctest avec `import doctest`
2. Copier puis coller le code suivant. 

```Python  

def somme(n):
    """
    Renvoi la somme des nombres allant de 0 à n inclus si n est positif. 
    0 sinon.

    Args : 
        n (int) : Un nombre strictement supérieur à 0  
    
    Returns : 
        (int) : La somme des n premiers nombres

    >>> somme(4)
    10
    >>> somme(0)
    0 
    >>> somme(-5)
    0
    >>> somme(11)
    66
    """
    ...

```

2. Effacer `...` et compléter le code de la fonction `affiche_carre` 
3. Vérifiez que tout les tests de la doctest ne fournissent pas d'erreur en ajoutant en dehors de votre fonction la ligne `print(doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE))`




## Exercice 2  

Vous travaillez dans une entreprise informatique.   
Votre chef de projet  
Un client de l'entreprise à besoin d'une fonction qui permet de ....
Le client établi un cahier des charges pour la fonction.
Elle doit déterminer si une phrase est un palindrome..., ..., ...  

Votre collègue Adam écrit le code de la fonction ... 

```Python
def est_palindrome(chaine):
    """
    détermine si chaine est un palindrome en ignorant les espaces, la ponctuation les voyelles accentuées et la casse

    Args :
        chaine (str) : Une chaine de caractères 

    Returns :
        (bool) : True si chaine est un palindrome. False sinon. 

    
    """
    phrase_nettoye = ""

    for caractere in chaine :  
        if caractere != " ":

            caractere_min = caractere.lower()

            if caractere_min in "áàâ" : 
                phrase_nettoye += "a"

            elif caractere_min in "éèê" : 
                phrase_nettoye += "e"

            elif caractere_min in "íìî" : 
                phrase_nettoye += "i"

            elif caractere_min in "óòô" : 
                phrase_nettoye += "o"

            elif caractere_min in "úùû" : 
                phrase_nettoye += "u"
                        
            elif caractere_min in "ýŷ" : 
                phrase_nettoye += "y"
            
            else:
                phrase_nettoye += caractere_min
                           
    
    return phrase_nettoye == phrase_nettoye[::-1]
```

Ecrivez la doctest qui permet de vérifier le cahier des charges fournis par le client.

## Exercice 3  

## Exercice 4  

Pour réaliser cet exercice vous avez besoin d'un binôme.  

__Contexte__

Vous travaillez sur un projet de programmation 
Le binome A écrit le code de la fonction 1 et les tests de la fonction 2 
Le binome B écrit le code de la fonction 2 et les tests de la fonction 1

Puis chacun