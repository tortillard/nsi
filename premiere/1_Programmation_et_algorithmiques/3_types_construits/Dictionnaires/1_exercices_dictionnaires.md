# Exercices sur les dictionnaires  

## Exercice 1 - Prise en main   
1. __Créez un dictionnaire__ nommé `dico_fruits` qui contient les noms de trois fruits comme clés et leurs prix respectifs comme valeurs. Par exemple : `{"pomme": 1.5, "banane": 0.5, "poire": 0.8}`.  
2. À partir du dictionnaire `dico_fruits` que vous avez créé, récupérez le prix de la banane et affichez-le.    
3. Ajoutez un nouveau fruit, par exemple `"cerise"` avec un prix de `2.3` au dictionnaire `dico_fruits`.
4. Ensuite, modifiez le prix de la pomme à `1.2`. Affichez le dictionnaire après ces modifications.
5. Utilisez la fonction `len()` pour afficher le nombre d'items dans le dictionnaire `dico_fruits`.
6. Parcourez le dictionnaire `dico_fruits` et affichez chaque nom de fruit.
7. Parcourez le dictionnaire `dico_fruits` et affichez chaque prix des fruits.
8. Avec un parcours, affichez `Le prix de la (fruit) est de (prix)` pour chaque fruit de `dico_fruits`.    
   

 
## Exercice 2 
Créez un dictionnaire nommé `dico_notes` qui contient les noms de trois étudiants comme clés et leurs notes respectives comme valeurs. Par exemple : `{"Alice": 15, "Bob": 12, "Charlie": 18}`.   
Ensuite, calculez et affichez la moyenne des notes.  

## Exercice 3  
Écrivez une fonction `verifier_cle(dico, cle)` qui prend un dictionnaire et une clé en argument et retourne `True` si la clé existe dans le dictionnaire, sinon `False`. Testez cette fonction avec le dictionnaire `dico_fruits`.

## Exercice 4  
Écrivez une fonction `inverser_dictionnaire(dico)` qui prend un dictionnaire en argument et retourne un nouveau dictionnaire où les clés et les valeurs sont inversées.   
Par exemple, si le dictionnaire d'entrée est `{"a": 1, "b": 2}`, le dictionnaire de sortie devrait être `{1: "a", 2: "b"}`.

## Exercice 5   
Créez deux dictionnaires, `dico1` et `dico2`, et écrivez une fonction `fusionner_dictionnaires(dico1, dico2)` qui fusionne les deux dictionnaires. C'est à dire qui renvoi un nouveau dictionnaire contenant les clés associées aux valeurs de `dico1` et `dico2`. Si une clé existe dans les deux dictionnaires, la valeur du premier dictionnaire doit être conservée.  

## Exercice 6   
Écrivez une fonction `compter_occurrences(chaine)` qui prend une chaine de caractères `chaine` et retourne un dictionnaire avec les caractères comme clés et le nombre d'occurrences de chaque élément comme valeurs.  
Par exemple, pour `chaine` qui vaut `"Bonjour à tous"`, le dictionnaire retourné devrait être `{'B': 1, 'o': 3, 'n': 1, 'j': 1, 'u': 2, 'r': 1, ' ': 2, 'à': 1, 't': 1, 's': 1}`.  

