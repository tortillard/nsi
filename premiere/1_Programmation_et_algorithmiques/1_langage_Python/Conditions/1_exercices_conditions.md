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
Écrire une fonction `remarque` qui prend un paramètre `note`.  s
Cette `note` est représenté par un `float` ou un `int`.   
Cette fonction renvoi :    
- `"Excellent"` si la note est supérieure ou égale à 90    
- `"Bien"` si la note est comprise entre 75 et 89  
- `"Suffisant"` si la note est comprise entre 50 et 74  
- `"Insuffisant"` si la note est inférieure à 50  

__Testez votre fonction__ 
 
## Exercice 4  
Si cela n'est pas encore fait, modifiez votre fonction pour que lorsque `note` vaut `-32.5` ou `974.0` le résultat renvoyé est cohérent. Vous pouvez décider dans ce cas de ce qui est renvoyé.  

Note : La bonne pratique veut qu'une fonction renvoie toujours le même __type__  

