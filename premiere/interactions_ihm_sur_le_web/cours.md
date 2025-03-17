# Interactions entre l'humain et la machine sur le web  

Lorsque l'on navigue sur le web en tant qu'utilisateur on passe notre temps à __interagir à l'aide de notre machine avec les pages Web__.  
__L'interface Homme-Machine(ou Humain-Machine "IHM")__ est un principe clé concernant le web puisqu'avant son arrivée les pages web était "statique".  
Il était possible de les consulter de la même manière que l'on consulte les livres d'une bibliothèque.  
__L'IHM repose sur la gestion d'événements sur des éléments graphiques.__
Par exemple si un bouton est présent sur une page cela peut déclencher un événement qui fait apparaitre une image.  

# HTML, CSS, JS  

## HTML  

### Généralités  

Le langage __HTML__ (HyperText Markup Language) est un langage de description.  
Il permet de créer des pages Web et plus précisément de décrire leur __contenu__.  
C'est dans le code HTML que l'on précise  __le texte, la vidéo, le son, le lien, etc...__ que l'on souhaite inclure dans notre page.
Enfin, il est possible d'écrire le code nécessaire pour séparer correctement les éléments(différentes zones) de notre page(section, div, ...).   

### Syntaxe  
Le langage HTML est un langage de __balisages__. On entoure de __balises__ les _éléments_ de notre site.  
On définit une balise avec les caractères `<` et `>`.  
Par exemple, la balise `<p>` permet de définir un paragraphe.  

> [!WARNING] 
> Chaque __balise ouvrante__ est associée à une __balise fermante__ (sauf quelques exceptions).  
> De manière générale on a `<balise ouvrante> contenu </balise fermante>` 
> Exemple : `<p> Dans le murmure des feuilles, le temps s'éveille en douceur. </p>` 

> [!TIP]
> Il n'y a pas d'histoire d'indentation ou de : concernant le langage HTML.
> Ainsi, il est totalement possible d'écrire le contenu d'une page web sur une seule ligne !
> Cela fait évidemment le bonheur des élèves, mais également le cauchemar de tous les professeurs.
> __Autrement dit, l'écriture d'un code "propre" repose sur vous__. Il est essentiel de passer des lignes quand c'est nécessaire, mais également de fournir une indentation pour obtenir une hiérarchie visuelle des balises."

Par exemple les deux codes HTML suivants sont équivalents : 
Exemple 1 :
```HTML
<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Exemple de Page HTML</title></head><body><h1>Bienvenue sur ma page web</h1><h2>Introduction</h2><p>Ceci est un exemple de paragraphe pour illustrer l'utilisation des balises HTML.</p><h2>À propos</h2><p>HTML est le langage de balisage standard pour créer des pages web.</p></body></html>

```
Exemple 2 :
```HTML
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemple de Page HTML</title>
</head>
<body>
    <h1>Bienvenue sur ma page web</h1>
    <h2>Introduction</h2>
    <p>Ceci est un exemple de paragraphe pour illustrer l'utilisation des balises HTML.</p>
    <h2>À propos</h2>
    <p>HTML est le langage de balisage standard pour créer des pages web.</p>
</body>
</html>

```

### Code HTML  

Après avoir créer un fichier `index.html`(en général c'est le nom qu'on donne à la page principale) le code minimum qui doit être présent dans notre fichier est le suivant.  
```HTML
<!DOCTYPE html> <!-- On précise que le fichier est en HTML  -->
<html lang="fr"> <!-- On ouvre une balise nommé html, ici l'attribut "lang" précise la langue utilisé dans ce fichier  -->

    <head> <!-- Déclaration de la tête de notre page. La tête de page sert à contenir les métadonnées de notre page -->
        <meta charset="UTF-8"> <!-- Par exemple la balise meta précise l'ensemble de caractère utilisé ici "UTF-8" -->
    </head>

    <body> <!-- Déclaration du corps de notre page --> 

        <!-- Ici on écrit le contenu de notre page -->            

    </body>
</html>

```

Une liste __non exhaustive__ des balises HTML est disponible ![ici](../../../snt/le_web/activite_html_css.md) dans la section __Glossaire des balises HTML__.  

## CSS  

### Généralités  

Le langage __CSS__ (Cascading Style Sheet) permet de se concentrer sur la __forme__ de notre page web.
Les langages __HTML et CSS__ vont très souvent de pair puisqu'une fois que le contenu de notre page est écrit, on souhaite modifier son apparence.    
C'est dans le code CSS que l'on précise, par exemple, __la couleur de notre texte, la taille que doit prendre une image ou encore si l'on souhaite positionner une vidéo en haut à droite de notre page.__

### Syntaxe  

Le code CSS s'écrit dans un autre fichier que le HTML. Généralement appelé `style.css` on définit à l'intérieur des __règles de style__ pour agir sur le style de notre fichier.  
Une règle css est définie par __un sélecteur__ sur lequel on souhaite agir(pour nous ce sera généralement le nom d'une balise), on écrit ensuite des accolades `{}` à l'intérieur desquelles on définit __les propriétés__ sur lesquelles on souhaite agir ainsi que __la valeur__ dont qu'on leur donne. 

> [!WARNING]
> A la fin de la modification d'une propriété on mets toujours un `;`. 

Exemple :

```CSS

p { /* On agit sur toutes les balises p*/
    color : blue; /* La couleur du texte est bleue */
}

```


### Code CSS  

La première chose à faire lorsqu'on créer un fichier CSS est de le _lier_ à la page HTML dont on souhaite modifier le style.  

Pour cela il faut aller dans le fichier HTML dans la balise `<head>` et ajouter cette ligne :
```HTML
<link rel="stylesheet" href="chemin_vers_le_fichier.css"> <!--Pas besoin de fermer cette balise ! -->
```

Il est maintenant possible de modifier le style de notre page. 
Une liste __non exhaustive__ des propriétés CSS est disponible ![ici](../../../snt/le_web/activite_html_css.md) dans la section __Glossaire des propriétés CSS__.  


## JS  

### Généralités 

### Syntaxe  

### Code  