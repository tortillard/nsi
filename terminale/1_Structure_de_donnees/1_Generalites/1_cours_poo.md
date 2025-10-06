# Programmation orienté objet  

## Généralités  
Un paradigme de programmation est une __façon(philosophie, manière d'aborder, ...)__ de programmer.    
Lorsqu'un problème doit être résolu informatiquement on choisit un paradigme de programmation __adéquat__ pour le résoudre.  
Parmis ces paradigmes, on retrouve la __Programmation Orienté Objet(POO)__,  impérative, fonctionnelle, etc...
Les types `int`, `float`, `bool`, etc... sont déjà présents dans Python initialement, la POO nous permet de définir nos propres types.  

## Vocabulaire  
En POO, on écrit des __classes__ pour définir des nouveaux types. 
Chaque __instance__ d'une __classe__ permet de créer un __objet__.   
On peut faire l'analogie avec un __model de voiture__(classe), qui permet de créer une __voiture__(objet).  
Évidemment, il est possible de créer plusieurs __voiture__ à partir d'un __model__.  

On définit dans la __classe__ des __attributs__ et des __méthodes__.  
- Les __attributs__ d'une classe sont les caractéristiques communes de chaque objet.  
- Les __méthodes__ d'une classe sont les fonctions qu'il est possible d'appliquer à nos objets.  

## En Python  
Exemple : On souhaite écrire une classe `Voiture`.   

> [!TIP] Le mot clé `class`  
> Pour débuter l'écriture d'une classe en Python on utilise le mot `class` suivi du nom de la classe.   

> [!TIP] Le constructeur  
> Toutes les __fonctions__ écrites dans une classe sont appelées __méthodes__ dans la suite du cours.    
> En l'occurence __le constructeur__ est la première méthode de classe que l'on écrit.    
> Le nom de cette méthode est `__init__` et elle prend comme premier paramètre `self` comme toutes les méthodes d'une classe. Nous verrons dans la suite du cours à quoi sert le mot clé `self`.    
> Il est ensuite _possible_ de rajouter des paramètres au constructeur qui devront prendre obligatoirement une valeur lors de la construction de l'objet, par exemple ici `model` est un paramètre du constructeur.    

> [!TIP] Les attributs  
> Enfin, on déclare __les attibuts__ dans le constructeur. __Les attributs__ se déclarent comme des variables, on leur donne __un nom__ et __une valeur__.   
> La seule différence est que `self.` précède le nom de chaque attribut  

Voici à quoi ressemble le début de l'écriture de la classe `Voiture`.  

```Python
class Voiture:      
    def __init__(self, model):  # Le constructeur

        # Les attributs
        self.nom_model = model
        self.annee_fabrication = 0  
        self.liste_couleurs_disponibles = []
        self.est_hybride = False 
``` 

> [!TIP] Le mot clé `self`  
> Le mot clé `self` est __TOUJOURS__ présent 
>   - En premier paramètre d'une méthode 
>   - Avant le nom d'un attribut  
> Le mot clé `self` est __JAMAIS__ présent lors de __l'appel__ d'une méthode  
> Le mot clé `self` est utilisé pour désigner l'instance actuelle.   
> Par exemple, le code `self.nom_model` peut se traduire en français par `L'attribut nom_model de mon objet` 


> [!TIP] Les méthodes
> On complète l'écriture de notre classe en écrivant des __méthodes__.  
> Les méthodes sont les fonctions que seul notre objet peut appeler.  
> On peut classer en 3 catégories les méthodes.  
> - Les _accesseurs_('getters') : Ces méthodes ont pour unique but de renvoyer la valeur d'un attribut  
> - Les _modificateurs_('setters') : Ces méthodes ont pour unique but de modifier la valeur d'un attribut  
> - Les autres : Toutes les méthodes qui adoptent un comportement différents des accesseurs ou des modificateurs

```Python
class Voiture:      
    def __init__(self, model):  # Le constructeur

        # Les attributs
        self.nom_model = model
        self.annee_fabrication = 0  
        self.liste_couleurs_disponibles = []
        self.est_hybride = False 

    # Les méthodes     

    ## Les accesseurs
    def get_nom_model(self): 
        return self.nom_model

    def get_annee_fabrication(self):
        return self.annee_fabrication

    def get_liste_couleurs_disponibles(self):
        return self.listes_couleurs_disponibles

    def get_est_hybride(self):
        return self.est_hybride

    ## Les modificateurs
    def set_nom_model(self, nouveau_nom_model):
        self.nom_model = nouveau_nom_model

    def set_annee_fabrication(self, nouvelle_annee_fabrication):
        self.annee_fabrication = nouvelle_annee_fabrication

    def set_liste_couleurs_disponibles(self, nouvelle_liste_couleurs_disponibles):
        self.liste_couleurs_disponibles = nouvelle_liste_couleurs_disponibles

    def set_est_hybride(self, hybride):
        self.est_hybride = hybride

    ## Autre méthode  
    def affiche_details_model_annee(self):  
        model = self.get_nom_model()  
        annee = str(self.get_annee_fabrication())  
        liste_couleurs = self.get_liste_couleurs_disponibles()
        est_hybride = self.get_est_hybride()

        chaine_couleur = ""
        for i in range(len(liste_couleurs)-1) :
            chaine_couleur = chaine_couleur + " " + liste_couleurs[i]

        chaine_couleur = chaine_couleur + " et " + liste_couleur[i] 
        
        if est_hybride:
            chaine_hybride = " est hybride "
        else:
            chaine_hybride = " n'est pas hybride "

        return "Le model " + model + " à été construit en " + annee + "\n" \
            "il" + chaine_hybride + "et est disponible dans les couleurs " + chaine_couleur
```

