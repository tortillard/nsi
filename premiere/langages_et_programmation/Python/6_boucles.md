# Les boucles  

Les boucles sont essentielles en programmation elles permettent de répéter une partie d'un programme plusieurs fois.  
C'est un élément clé qui nous permet d'automatiser de nombreuses tâches fastidieuses.  
Par exemple une entreprise de communications ne va pas engager une personne(ou un groupe de personne) pour envoyer des milliers de mails rédiger à la main un à un à différents individus. Elle optera plutôt pour un programme qui récupère l'adresse mail de chaque destinataire et qui envoie le même message. 

## Boucles non bornées 

La boucle non bornée permet de répéter des instructions __tant qu'__ une condition n'est pas vérifiée. 
La condition en question peut être vérifiée à un moment que l'on ne peut déterminer.  
C'est dans ce sens là où on parle de boucle __non__ bornée on parle également de boucle __tant que__.  
En Python, on définit une boucle non bornée :
    - par le mot clé `while`
    - suivie de la condition qui doit être vérifiée pour que la boucle continue de s'exécuter
    - on ajoute `:` au bout de la ligne  
    - on passe une ligne, on indente et on écrit le code qu'on souhaite exécuter lors de la répétition de la boucle 

Exemple :
```Python 
i = 0
while i < 10 : 
    print("Bonjour tout le monde !")
    i = i + 1
```
Ce code permet d'afficher 10 fois la phrase `"Bonjour tout le monde !"`.  


__Remarque__ : Un code qui contient une boucle non bornée peut boucler à l'infini si la condition d'arrêt n'est jamais satisfaite. Il faut donc bien faire attention lorsque l'on programme ! 

Voici un exemple de programme avec une boucle qui ne s'arrête jamais. 
> [!WARNING] Il n'est pas conseillé de tester ce programme si vous n'avez pas sauvegarder au préalable le code déjà écrit.  


```Python  
while True:
    print("boucle infini !")
```



## Boucles bornées   

La boucle bornée permet de répéter des instructions un nombre de fois prédéfini.    
On l'utilise quand on sait le nombre de fois que l'on veut répéter notre code.   

En Python, on définit une boucle bornée :  
    - par le mot clé `for`  
    - suivie d'une variable d'itération 
    - le mot clé `in`  
    - un itérateur (range(n), une chaine de caractères, ...)  
    - on ajoute `:` au bout de la ligne    
    - on passe une ligne, on indente et on écrit le code qu'on souhaite exécuter lors de la répétition de la boucle   


Exemple :
```Python  
for i in range(10):
    print("Bonjour tout le monde !")
```
Ce code permet d'afficher 10 fois la phrase `"Bonjour tout le monde !"`.  

La fonction `range(n)` renvoie un itérateur constitué des nombres allant de `0` à `n-1` autrement dit, l'instruction `for i in range(10):` peut se traduire par `"Pour i allant de 0 à 9 effectue les instructions suivantes"`.  

Il est également possible de s'en convaincre en testant le code suivant.  
```Python  
for i in range(10): 
    print(i)
```
Ce code permet d'afficher les valeurs que prend `i`.  


