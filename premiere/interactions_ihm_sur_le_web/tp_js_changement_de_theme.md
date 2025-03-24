# Changement de thèmes  

## Objectif  
Le but de ce TP est d'ajouter des boutons sur notre site afin de modifier __le thème__ de notre page.  

## Travail à faire  
1. En premier lieu, ajouter 2 boutons dans votre code HTML n'oubliez pas de leur attribuer un __identifiant unique__ ! (Par exemple `"dark"` et `"light"`)
2. Créez un fichier `main.js` ce fichier doit être placé dans le même dossier que le fichier html.  
3. Dans le fichier `main.js` écriver le code qui permet de récupérer les 2 boutons crée dans le fichier html.  
4. Ajoutez à chacun de vos boutons un évènement `click` qui fait appel à une fonction unique selon le bouton. 
Par exemple, on attribuera au bouton ayant l'identifiant `"light"` un évènement de click vers une fonction nommée `setThemeLight`, etc...  
5. Nous venons d'attribuer à chaque bouton l'appel d'une fonction, cependant ces fonctions ne sont pas encore créées. Il faut donc écrire une fonction pour chaque bouton, ayant le même nom que celui qui a été attribué précédemment. On rappel que pour définir une fonction en javascript on utilise le mot clé `function`. (voir dans le fichier [html_css_js](html_css_js.md)). Chaque fonction crée ne prend pas de paramètres. 
6. A l'intérieur de chaque fonction nous allons modifier le style de notre page. Pour cela nous allons changer la couleur de fond et du texte du corps de notre page. Le code __javascript__ suivant permet de modifier la propriété `color` CSS de notre fichier html : `document.body.style.color = "red"`. 
7. Toutes les propriétés de style sont accessible grâce au code `document.body.style. ...`. Faite en sortes d'avoir 4 boutons sur votre page. Chaque bouton est associée à un thème(jour, nuit, cyber, retro, floral, ...) faites en sortes de modifier le thème de votre site lors du clique sur un des 4 boutons. Vous pouvez modifier d'autres propriétés de style que les couleurs. 