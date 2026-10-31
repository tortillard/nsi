Ce TP à pour but de découvrir l'utilisation de la variable globale ?


> [!WARNING]
> En Python, pour __définir__ des variables global il suffit de les écrire en dehors de toutes fonctions(généralement tout en haut du script).  
> __En revanche__, lorsque l'on souhaite __modifier__ ces variables à l'intérieur d'une fonction il faut préciser au code que l'on utilise la variable global. Sans cela Python ne comprend pas de quelle variable on parle.  
> Exemple : 
> ```Python
> NB_FIGURINES = 12
> PRIX_FIGURINES = 4.7
> 
> def total_prix_figurines():
>   global NB_FIGURINES    
>   global PRIX_FIGURINES
>   return NB_FIGURINES * PRIX_FIGURINES
> ```


Le restaurant 

## Partie 1
Le restaurant doit gérer son stock d'ingrédient.
Pour cela, il lui faut un programme qui évalue le stock pour un `budget_initial` donné.  

| Produit  | STOCK_INITIAL | STOCK_MAXIMUM | PRIX  |
| :------: | :-----------: | :-----------: | :---: |
| TOMATES  |      127      |      350      | 0.32  |
| CAROTTES |      74       |      200      | 0.24  |
|  PATES   |      49       |      100      | 1.27  |


Enfin, on estime un budget de 3700€ 

> [!IMPORTANT]
> __Q1__
> Sans définir de fonction.
> Tout en haut de votre script, définissez des variables 'global' associées aux valeurs dans le tableau ainsi qu'au budget estimé.   
> Chaque variable doit posséder un nom judicieusement choisi et être écrit en majuscule(un peu comme sur la première ligne et colonne du tableau).  

> [!IMPORTANT]
> __Q2__  
> Définissez une fonction nommée `stock_apres_achat_tomates` qui prend en paramètre `nb_tomates` achetés. 
> Cette fonction ne renvoie __rien__(pas de return).  
> Elle doit simplement __modifier__ les valeurs des variables qui s'occupe du stock des tomates, ainsi que celle pour le budget.  

> [!IMPORTANT]
> __Q3__  
> De la même manière définissez les fonctions `stock_apres_achat_carottes`, et `stock_apres_achat_pates`.  

> [!IMPORTANT]
> __Q4__  
> Définissez une fonction nommée `prix_stock_tomates` qui calcule et __renvoie__ le coût des tomates dans le stock. 

> [!IMPORTANT]
> __Q5__  
> De la même manière définissez les fonctions `prix_stock_carottes` et `prix_stock_pates`

> [!IMPORTANT]
> __Q6__  
> Définissez une fonction nommée `prix_stock_total` qui calcule et __renvoie__ le coût des total du stock.  


## Partie 2

Le restaurant doit préparer des repas à partir des ingrédients dans son stock.  
Voici le menu, composé des noms de chaque plat, les ingrédients nécessaire à la préparation et le prix du plat.  


|    Nom     | Sac de pates | Tomates | Carottes | Prix  |
| :--------: | :----------: | :-----: | :------: | :---: |
|   Macola   |      1       |    1    |    2     | 6.5€  |
|   Sathé    |              |    2    |    3     | 2.9€  |
|  Bonvivre  |              |    2    |    2     | 2.3€  |
| Simplement |      3       |         |          | 4.3€  |

de la même manière que dans la partie 1 nous allons définir les fonctions permettant de diminuer nos stock d'ingrédient lorsqu'un plat est commandé. 

> [!IMPORTANT]
> __Q7__  
> Définissez une fonction nommée `macola_commande` qui diminue le budget et le stock des ingrédients en conséquence.  

> [!IMPORTANT]
> __Q8__  
> De la même manière créer définissez les fonctions `sathe_commande`,`bonvivre_commande` et `simplement_commande`. 



## Partie 3 - conditions 

> [!IMPORTANT]
> __Q9__  
> ...

