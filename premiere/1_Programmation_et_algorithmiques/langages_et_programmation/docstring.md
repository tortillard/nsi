# Docstring

__Qu'est-ce qu'une docstring ?__

> [!TIP]
> Une docstring (ou "documentation string") est une chaîne de caractères utilisée pour documenter une fonction, une classe ou un module en Python.
> Elle est généralement placée immédiatement après la définition de la fonction, de la classe ou du module, et est délimitée par des triples guillemets (simples ou doubles).


## La docstring a plusieurs objectifs :

__Documentation__ : Elle fournit des __informations__ sur ce que fait la fonction, les paramètres qu'elle prend, ce qu'elle retourne, et éventuellement les exceptions qu'elle peut lever. Cela aide les autres développeurs (ou même soi-même) à comprendre rapidement le fonctionnement du code.

__Accessibilité__ : Les docstrings peuvent être consultées à l'aide de la fonction __`help()`__ en Python, ce qui permet d'accéder à la documentation directement dans l'interpréteur Python.

__Meilleures pratiques__ : L'utilisation de docstrings est considérée comme une bonne pratique de programmation, car elle améliore __la lisibilité__ et la maintenabilité du code.  


## Comment écrire une docstring ?
Il existe plusieurs formats pour écrire une docstring. Parmi eux on compte, `Javadoc`, `reST`(pour reStructuredText), `NumPy/SciPy` mais le format le plus utilisé est celui de `Google`. C'est ce format que nous allons utiliser. 

Voici comment se présente le __format Google pour écrire une docstring__ dans une fonction Python. 

```python

def ma_fonction(param1, param2):
    """
    Brève description de ce que fait la fonction.

    Args:
        param1 (type): Description du premier paramètre.
        param2 (type): Description du deuxième paramètre.

    Returns:
        type: Description de la valeur de retour.

    """
    pass  
```  


## Exemple de docstring  


```python

def additionner(a, b):
    """
    Additionne deux nombres.

    Args:
        a (int ou float): Le premier nombre à additionner.
        b (int ou float): Le deuxième nombre à additionner.

    Returns:
        int ou float: La somme de a et b.
    """
    return a + b
```

> [!NOTE]
> On peut préciser le type des paramètres et de la valeur de retour d'une fonction dans la signature de la fonction.
> Comme ceci `def additionner(a : int, b: int) -> int`
> Dans ce cas, préciser le type dans la docstring n'est pas obligatoire.