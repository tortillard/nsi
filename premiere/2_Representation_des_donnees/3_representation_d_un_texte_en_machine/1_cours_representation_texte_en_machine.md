# Représentation d'un texte en machine  

## Généralités  
Chaque information sur un ordinateur finit par être convertit en nombre. Il en va de même pour les caractères qui compose un texte.  
Ainsi, selon le système d'encodage utilisé un caractère possède un code.  

## 1er système d'encodage : ASCII  

- Le code __ASCII__ (American Standard Code for Information Interchange) a été proposé dans les années 60 pour standardiser la représentation des caractères.   
- Chaque caractère possède __un code__ représenté en binaire sur 7 bits. 

Voici la table ASCII. 


![table ascii](img/ascii.png)  

Dans la table ASCII on compte 128 caractères différents, parmi eux on à :
- 95 caractères imprimables(minuscules, majuscules, caractères spéciaux, nombres)   
- 33 caractères non imprimables. Ces caractères sont surtout utile pour la syntaxe du texte par exemple on à le caractère espace

 
La table ASCII est très pratique pour représenter les __textes écrits en Anglais__. 
En revanche, on remarque que les caractères accentuées ne peuvent pas être représentée. Il n'est donc pas possible d'écrire un texte en français.  


## 2ème système d'encodage : ISO-8859-1   

__L'Organisation Internationale de Normalisations(ou ISO en anglais)__ à défini une norme informatique afin de représenter plus de caractères que ne le permet la table ASCII.   
La première partie de cette norme se nomme __ISO-8859-1__ également appelée __Latin 1__.



Voici la table __ISO-8859-1__  

![iso 88591](img/iso88591.png)

Chaque code est représenté sur 8 bits c'est à dire 1 octet.  
Dans la table ISO-8859-1 on a: 

- __Les 128 caractères de la table ASCII__  
- __128 nouveaux caractères__ parmis eux on a les caractères accentuées en minuscules et majuscule, des symboles mathématiques etc...


## Unicode : standard  

L'ensemble de tout les caractères utilisés à travers chaque langages du monde à fait naître un standards informatique appelé __Unicode__.  
Ce standard est développé par le consortium du même nom : __Consortium Unicode__.  
__Unicode__ n'est __pas__ un système d'encodage, c'est un __standard__ qui à pour but d'attribuer un point de code à chaque caractère.  
__Unicode__ à ensuite crée différent systèmes d'encodage dont le plus utilisé est l'__UTF-8__.  

## 3ème système d'encodage : UTF-8 

UTF-8 code chaque caractère sur 1,2,3 ou 4 octets.
Au maximum on peut utiliser 32 bits ce qui donne $2^{32} \approx 4 \text{milliards}$.   
Avec une telle représentation on est certain que l'ensemble des caractères utilisable dans le monde possède un code unique.  

Les 128 premiers caractères d'UTF-8 sont ceux de la table ASCII qui tiennent sur 1 octet. Les caractères accentuée eux sont codés sur plusieurs octets.  



> [!TIP]  
> Remarque : __Des problèmes de conversion peuvent survenir entre 2 textes qui n'utilisent pas le même format d'encodage.__    
> En utilisant l'__ISO-8859-1__, n'importe quel caractère possède un code représenté sur 1 octet.   
> Ce n'est pas le cas pour l'__UTF-8__.    
> Ainsi le caractère `ù` à pour code :  
> - `F9` en `ISO-8859-1`   
> - `C3 B9` en `UTF-8`  


Le standard Unicode est constitué :
- d'un répertoire de 159 801 caractèrescouvrant plus de 150 écritures,
- etc...


Les différentes tables Unicode sont disponibles sur le site wikipédia juste [ici](https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode_(0000-0FFF))



Note : Il existe également d'autre système d'encodage Unicode :
- UTF-16 : code chaque caractère sur __2 octets minimum__. 
- UTF-32 : code chaque caractère sur __4 octets__