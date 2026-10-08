# Exercices sur les conditions  

## Exercice 1  

On considère les voyelles minuscules dans l'ordre suivant :  
- `'a'` est la voyelle numéro `1`  
- `'e'` est la voyelle numéro `2`  
- ...  
- `'y'` est la voyelle numéro `6`  
  
Écrire une fonction `associe` qui prend un paramètre `lettre` et qui renvoi le numéro de la voyelle associée selon la valeur de `lettre`.  

Par exemple : `associe("e")` renvoi `2`

## Exercice 2  
Modifiez votre fonction pour que cela fonctionne également lorsque `lettre` est une majuscule  

## Exercice 3  
Écrire une fonction `est_pair` qui prend un nombre entier en paramètre et renvoie `"Pair"` si le nombre est pair et `"Impair"` s'il est impair.

## Exercice 4  
Écrire une fonction `remarque` qui prend un paramètre `note`.  
Cette `note` est un nombre.  
Cette fonction renvoi :    
- `"Excellent"` si la note est supérieure ou égale à 90    
- `"Bien"` si la note est comprise entre 75 et 89  
- `"Suffisant"` si la note est comprise entre 50 et 74  
- `"Insuffisant"` si la note est inférieure à 50  

__Testez votre fonction__ 
 
## Exercice 5  
Si cela n'est pas encore fait, modifiez votre fonction pour que lorsque la `note` est négatif ou supérieur à 20, on affiche `"Erreur"`.  

## Exercice 6  
Écrire une fonction `classer_temperature` qui prend une température en degrés Celsius et renvoie `"Froid"` si la température est inférieure à `0`, `"Tempéré"` si elle est entre `0` et `25`, et `"Chaud"` si elle est supérieure à `25`.

## Exercice 7  
Écrire une fonction `check_mot_de_passe` qui prend en paramètre `tentative`.  
Dans votre fonction commencé par définir une variable nommée `mdp` en lui attribuant la valeur que vous souhaitez.  
Votre fonction doit renvoyer `True` si `tentative` est égal à `mdp` et `False` sinon.    

Bonus : Réecrire cette fonction sur une seule ligne.  


