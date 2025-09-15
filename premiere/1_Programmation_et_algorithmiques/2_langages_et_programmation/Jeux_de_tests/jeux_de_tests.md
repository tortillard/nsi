# Jeux de tests  

## Utilité  
### Définition  
La norme IEEE 829-1998 définiti les tests (informatique) comme suit :

> _"Un test est un ensemble de cas à tester (état de l'objet à tester  avant exécution du test,_ 
> _actions ou données en entrée, valeurs ou observations attendues, et état de l'objet après exécution),_
> _éventuellement accompagné d'une procédure d'exécution (séquence d'actions à exécuter)._ 
> _Il est lié à un objectif."_  

### Objectifs  

- L'objectif principal des _tests_ en informatique est de s'assurer que le programme écrit est __correct__.  
Cela permet d'identifier les problèmes à corriger ou d'améliorer le code déjà écrit.  

- Le __[programmation par pair](https://fr.wikipedia.org/wiki/Programmation_en_bin%C3%B4me)__(pair programming) ou la _revue de code_(code review) sont des pratiques courrantes dans le monde du travail en informatique. Dans ces situations les jeux de tests ont un rôle important pour l'avancer dans le travail.  

- L'apparition des jeux de tests à donné naissance à une nouvelle façon de programmer __[le développement piloté par les tests](https://fr.wikipedia.org/wiki/Test_driven_development)__ (TDD pour Test-Driven Developpement). Le but de cette méthode consiste à écrire les tests avant d'écrire le code. Cela peut paraitre contre intuitif mais cette méthode permet d'éviter un bon nombre d'erreur. 

## L'écriture des tests   

De manière précise, il existe différentes façon d'écrire un test selon le langage de programmation utilisés, la suite du cours montre un exemple en Python.    
Plus généralement, l'écriture d'un test se fait de la manière suivante  :  
  - écriture des entrées à tester   
  - appel des fonctions(ou du code) à tester sur les entrées ET __vérification du résultat attendu__   

### Exemple  

Voici le pseudo code d'un programme qui compte les voyelles

```Pseudo
FONCTION compte_voyelles(chaine_a_tester):
    res = 0
    POUR lettre DANS chaine_a_tester :
        SI lettre est une VOYELLE : 
            res = res + 1  
    RENVOI res
```

Voici l'écriture d'un test pour la fonction compte_voyelles  

```Pseudo
mot_a_tester = "BONJOUR"
res = compte_voyelles(mot_a_tester) == 3
AFFICHE(res)
```

## Qualité et Quantité 

Le but des tests est de limiter les erreurs produite par le programme.  

- __Quantité__ : Il faut donc multiplier(raisonnablement) les tests afin de couvrir un maximum de cas différents.   
- __Qualité__ : Il faut penser à chaque cas sans écrire des tests redondants ou inutile.  


__Remarque__ : Un jeu de test correctement écrit ne suffit pas(toujours) pour affirmer la __correction__ d'un programme

## Le module doctest en Python  

En Python, il existe un module nommé `doctest` permettant d'écrire des tests pour nos fonctions.    

Une fois le module importé, il suffit d'écrire la __doctest__ pour chaque fonction en dessous de la docstring.  

Pour écrire un test il faut respecter la syntaxe suivante. Mettre `>>> la_fonction_a_tester()` puis passer une ligne en écrivant le résultat attendu.  

__Exemple__

```Python
import doctest


def compte_voyelles(chaine_a_tester):
    """
    Compte le nombre de voyelles en majuscule de chaine_a_tester

    Args :
        chaine_a_tester (str) : Une chaine de caractère
    
    Returns : 
        (int) : Le nombre de voyelles en majuscule de chaine_a_tester
    
    >>> compte_voyelles("BONJOUR")
    3
    >>> compte_voyelles("bonjour tout le monde !")
    0  
    >>> compte_voyelles("@lsPE2-*}8F")
    1
    """
    res = 0
    for lettre in chaine_a_tester:
        if (lettre == "A") or (lettre == "E") or (lettre ==  "I") or (lettre == "O") or (lettre == "U") or (lettre ==  "Y"):
            res = res + 1
    return res

print(doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE))
```

Copier puis coller le code précédent et exécuter le pour interpréter le résultat fourni par le module doctest.

