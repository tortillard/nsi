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

## Exercice 2  
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


## TP - Pokémons  

Le pokédex est un appareil permettant d'obtenir des informations d'un pokémon.  
Nous souhaitons implémenter les fonctionnalitées de __recherche__ d'un pokédex.  
Par exemple, dans notre pokédex il sera possible d'obtenir:
- La liste de tout les pokémons de type feu  
- La liste de tout les pokémons de la première génération  
- La liste de tout les pokémons de la première génération de type feu  
- ...   


Il faut tout d'abord récupérer les informations concernant nos pokémons.  
1. Commencer par télécharger le fichier : ![pokemons.csv](pokemons.csv) <!-- lien vers le fichier pokemons.csv -->  

> [!IMPORTANT]
> L'extension `.csv` signifie `comma separate value` en français `valeur séparé par des virgule`.

> [!IMPORTANT]
> Les fichiers `.csv` sont généralement constituée comme suit :   
> - La première ligne définit les __attributs__ de nos données  
> - Le reste des lignes constituent l'ensemble de nos données   
>   - Une ligne représente une donnée, appelée également un __enregistrement__   
>   - Chaque __enregistrement__ possède des __valeurs__ associées aux __attributs__ et séparés par des virgules(ou point-virgules, ...)

> [!TIP]
> Vous pouvez ouvrir un fichier `.csv` avec un éditeur de texte(bloc-notes par exemple) pour voir à quoi ressemble votre fichier. 
> Faite le test ! 


2. Une fois le fichier téléchargée, créer un fichier python nommée `pokedex.py` qui se situe au __MÊME ENDROIT__ que votre fichier `csv`(par exemple créer un dossier dans lequel vos 2 fichiers seront présents).  

Il faut maintenant récupérer les données de notre fichier `.csv` en Python.  
Pour cela, nous allons utiliser un module en Python nommée `csv`.  

3. Dans la première ligne de votre fichier python écrivez `import csv` pour importer ce module.  

Le module `csv` contient une fonction nommée `DictReader` qui permet de transformer chaque __enregistrement__ de notre fichier en dictionnaire python.  
Chaque dictionnaire à pour clé les __attributs__ et pour __valeurs__ les données de l'enregistrement.  

Le code suivant permet de manipuler les données de notre fichier.  

```Python
with open('pokemons.csv') as mon_fichier: # on ouvre et lit le fichier 'pokemons.csv' 

        lecteur = csv.DictReader(mon_fichier, delimiter=';') # on convertit le fichier lu en objet 'DictReader' en précisant que le caractère qui délimite les données est ';'
    
        for dico_pokemon in lecteur: # pour chaque dictionnaire de pokemon crée dans l'objet 'DictReader'
            print(dico_pokemon) # on l'affiche !              
```

4. Copier-coller le code précédent et assurez vous de son fonctionnement.  
5. A partir du code précédent, créer une fonction nommée `liste_dico_pokemon()` qui ne prend aucun paramètre et renvoi la liste constituée des dictionnaires représentant les pokémons. 
Voici ce que devrait renvoyer `liste_dico_pokemon()` :
```Python
[{'n': '1', 'pokemon': 'Bulbizarre', 'type': 'Plante', 'type2': 'Poison', 'sous_evolution': '', 'evolution': 'Herbizarre', 'mega_evolution': '', 'forme_normale': '', 'region': 'Kanto', 'generation': '1'},
{'n': '2', 'pokemon': 'Herbizarre', 'type': 'Plante', 'type2': 'Poison', 'sous_evolution': 'Bulbizarre', 'evolution': 'Florizarre', 'mega_evolution': '', 'forme_normale': '', 'region': 'Kanto', 'generation': '1'},
 ...]
```  
  
Maintenant que nous avons notre liste de Pokémon(représenté par des ditionnaires) nous pouvons en extraire des parties.

Par exemple au lieu de récupérer tout les attributs de chaque pokémon on peut souhaiter obtenir qu'une partie des attributs.  

6. Écrivez une fonction `extraire_attributs(li_dico_pokemon, liste_attributs)` qui renvoie la liste des pokémons(représenté par un dictionnaire) avec uniquement les attributs présent dans `liste_attributs`.   
Voici ce que devrait renvoyer `extraire_attributs(li_dico_pokemon, liste_attributs)`, si :
- `li_dico_pokemon` vaut la même valeur que précédemment  
- `liste_attributs` vaut `["n", "pokemon", "type"]`
```Python
[{'n': '1', 'pokemon': 'Bulbizarre', 'type': 'Plante'},
{'n': '2', 'pokemon': 'Herbizarre', 'type': 'Plante', },
 ...]
```  

On souhaite maintenant, ajouter une __condition__ sur la valeur des attributs des pokémons à renvoyer.  
Par exemple, on renvoi un pokémon _si son `"type"` est `"Plante"`_.  

7. Écrivez une fonction `selectionne_par_type(li_dico_pokemon, type_recherche)` qui renvoie la liste des pokémons(représenté par un dictionnaire) de `li_dico_pokemon` du type `type_recherche`.  
8. En vous inspirant de la question précédente, écrivez une fonction `selectionne_par_attributs(li_dico_pokemon, dico_attributs)`. Avec `dico_attributs` qui est un dictionnaire où les clés sont des attributs et les valeurs sont les valeurs que les attributs des pokémons doivent satisfaire pour être renvoyé dans la liste.     
Voici ce que devrait renvoyer `selectionne_par_attributs(li_dico_pokemon, dico_attributs)`, si:
- `li_dico_pokemon` vaut la même valeur que précédemment  
- `dico_attributs` vaut `{"n" : 1}`. 
```Python
[{'n': '1', 'pokemon': 'Bulbizarre', 'type': 'Plante', 'type2': 'Poison', 'sous_evolution': '', 'evolution': 'Herbizarre', 'mega_evolution': '', 'forme_normale': '', 'region': 'Kanto', 'generation': '1'}]
```  

On souhaite maintenant trier l'ordre d'apparition des pokémons dans la liste qui est renvoyé.  
Pour trier une liste il existe une fonction nommée `sorted()`. Cette fonction trie la liste passée en paramètre.  
Vous pouvez tester en tapant `sorted([4,0,9,2,7])`.  
Or notre liste ne contient pas des nombres mais des dictionnaires.    
Si on essaie de trier une liste de dictionnaire à la place d'une liste de nombre, une erreur apparait.    
Cela parait évident puisque la fonction ne sait pas comparer 2 dictionnaires.    
Cela parait absurde de dire `le premier dictionnaire est plus petit que le deuxième`.    
Il faut donc indiquer à la fonction `sorted` comment comparer 2 dictionnaires.    

> [!TIP]
> Pour cela, la fonction `sorted` possède un paramètre optionnel nommée `key` qui permet de préciser la _clé_ sur laquelle on souhaite comparer.    
> Sans rentrer dans les détails il faut lui attribuer(entre autre) la valeur d'une `lambda` fonction.    
> Prenons la liste de dictionnaire `magasin = [{"nom" : "Pomme" , "prix" : 4.2 , "place": 70}, {"nom" : "Verre", "prix" : 2.1, "place": 375},{"nom" : "ecran", "prix" : 98.7, "place": 120}]`.      
> Il est évidemment impossible d'écrire `sorted(magasin)`.    
> Par contre si l'on souhaite trier notre liste notre liste dans l'ordre croissant des prix il suffit d'écrire : `sorted(magasin, key = lambda article : article["prix"])`

9. Tester le code précédent  
10. Modifier le code précédent pour que les articles soit trié en fonction de `"place"`
11. Modifier le code précédent pour que les articles soit trié en fonction de `"nom"`, comment sont trié les articles ?  

__Retour aux pokémons !__  
12. En vous inspirant du code des questions précédentes écrivez une fonction `tri_selon_attribut(li_dico_pokemon, attribut)` qui renvoie `li_dico_pokemon` trié selon le paramètre `attribut`.  

On souhaite maintenant fusionnez 2 listes de pokémon(toujours représenté par des dictionnaires).    
On considère la première liste de dictionnaire étant `l_d1` et la seconde `l_d2`.     
La fusion de ces deux dictionnaires doit être la liste des pokémons compris dans `l_d1` et ceux dans `l_d2`.   
__Attention__ : Il est possible que des pokémons de `l_d1` soit présent dans `l_d2` !

13. Écrivez une fonction `fusion_dico(li_dico_pokemon_1, li_dico_pokemon_2)` qui prend 2 listes de dictionnaires(pokémon) et renvoie la fusion de ces 2 listes.   

14. Des dresseurs pokémons vous ont fait une demande de recherche, voici leurs demandes :  
    - 1. La liste de tout les pokémons de type plante.   
    - 2. La liste de tout les pokémons de la première génération.  
    - 3. La liste de tout les pokémons de la première génération de type plante.     
    - 4. La liste des noms et régions de tout les pokémons de type eau.    
    - 5. La liste des noms, type et deuxième type de tout les pokémons de type feu.    
    - 6. La liste des noms, type et generation de tout les pokémons de type Normal de la génération 4 (attention au type de l'attribut `génération`)    
    - 7. La liste des noms des pokémons et de leur génération trié par l'ordre alphabétique de leurs noms.  
    - 8. La liste des noms et types des pokémons de la génération 1 de type Psy et de la géneration 7 de type Glace.  
    