# Pseudo-code

## Généralités  
Le __pseudo-code__ est un outil qui permet d'aider l'écriture d'un algorithme.  
Le but est d'écrire un algorithme sans ce soucier du langage de programmation utilisé.  
Pour cela, on écrit de manière naturel en français(simplifiée) notre algorithme.    

Les avantages du pseudo-code sont les suivants: 
- Cela permet de prendre conscience de l'ampleur du code à écrire
- La résolution d'un problème informatique est généralement simplifiée en 2 étapes `Réflexion -> écriture du code`.   
Avec cette manière on admet que 
  1. le programmeur maitrise le langage qu'il utilise 
  2. le problème à résoudre est relativement simple, pour convertir ses pensées en code
En pratique ce n'est pas toujours le cas.   
Le pseudo-code vient rajouter une étape intermédiaire à la résolution du problème afin de simplifier les efforts. On obtient donc :  
`Réflexion -> écriture du pseudo-code -> Traduction dans le langage de programmation utilisé`


## Mot clé en pseudo-code   
Le Pseudo-code n'as pas vocation à être compris par un ordinateur, il ne possède donc pas de règle ou de convention à respecter pour en écrire.   
Toute fois, il existe des pratiques et des mots clés qui font consensus.

|                          Mots clés                           |              Signification              |                                   équivalent en Python                                   |
| :----------------------------------------------------------: | :-------------------------------------: | :--------------------------------------------------------------------------------------: |
|                          `FONCTION`                          |          Définir une fonction           |                                          `def`                                           |
| `SI` (condition) `ALORS` (instruction), `SINON`(instruction) |         Définir des conditions          |                                      `if`,  `else`                                       |
|   `REPETER`(ou `POUR i ALLANT de x A y AVEC UN PAS DE z`)    |              Boucle bornée              |                                          `for`                                           |
|          `TANT QUE`(condition) `FAIRE`(instruction)          |            Boucle non bornée            |                                         `while`                                          |
|                        `DEBUT`, `FIN`                        | Marqueur de début et fin d'instructions | En Python, ce sont les indentations qui définissent le début et la fin d'une instruction |

Cette liste n'est pas complète et peut être modifiée à la guise du programmeur tant que le pseudo-code écrit est cohérent.  
En pratique certains mots-clés associé à des verbes peuvent être utilisé : `LIRE`, `INVERSE`, `MANGE`, `AJOUTER` 

### Exemples  

On prend le cas d'une fonction `additionne_borne` avec le paramètre `a` et le paramètre `b` qui fait la somme des nombres allant de `a` à `b`. 

Voici un exemple de pseudo-code.  

```Pseudo
FONCTION additionne_borne(a, b)
    
    resultat = 0

    POUR i ALLANT de a A b AVEC UN PAS DE 1
        AJOUTER i A resultat
    FIN POUR

    RETOURNER resultat 

FIN FONCTION
```

La même fonction écrite en Python
```Python

def additionne_borne(a, b):
    resultat = 0  

    for i in range(a, b+1):
        resultat = resultat + i
    
    return resultat
```


## Niveau de précision  

Selon l'écriture du pseudo-code le niveau de précision de l'algorithme peut varier.  
- Si le niveau de précision est trop faible il faudra fournir plus d'effort lors de l'étape concernant la traduction dans le langage de programmation choisi.   
- En revanche, si le niveau de précision est important le pseudo-code sera quasiment écrit dans le langage de programmation.  

Voici des niveaux différents de précision pour le même programme.  

__Faible précision__
```Pseudo
FONCTION additionne_borne(a, b)
    
    resultat = 0

    
    AJOUTER i A resultat POUR i ALLANT DE a A b
    

    RETOURNER resultat 

FIN FONCTION
```


__Précision moyenne__
```Pseudo
FONCTION additionne_borne(a, b)
    
    resultat = 0

    POUR i ALLANT de a A b AVEC UN PAS DE 1
        AJOUTER i A resultat
    FIN POUR

    RETOURNER resultat 

FIN FONCTION
```

__Forte précision__
```Pseudo
FONCTION additionne_borne(a, b)
    
    resultat = 0

    POUR i ALLANT de a A b AVEC UN PAS DE 1
        resultat = resultat + i
    FIN POUR

    RETOURNER resultat 

FIN FONCTION
```