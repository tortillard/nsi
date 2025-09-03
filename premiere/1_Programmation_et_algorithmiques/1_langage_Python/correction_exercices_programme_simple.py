# Exercice 1  

a = 4
b = -7
c = a + b
print(c)

# Exercice 2 - le résultat doit être 4
#a = 4
#b = a -7
#c = b*-3
#d = c-1
#e = d/2 
#print(e)

#a = a -7
#a = a * - 3
#a = a - 1
#a = a / 2
#print(a)

#a = 4 
#a = (((a -7) * -3) - 1) / 2
#print(a)

# Exercice 3  
a = 2 
b = 7 

c = a
a = b 
b = c 

# Exercice 4 
nom = "Jedusor"
prenom = "Tom"
print("Bonjour je m'appelle " + prenom + " " + nom)
 
 
# Exercice 5 
age = 15 
print("Vous avez " + str(age) + " ans")


# Exercice 6
numerateur = 10
denominateur = 3  
quotient = numerateur // denominateur
reste = numerateur % denominateur
print("La division de " + str(numerateur) + " par " + str(denominateur) + " à pour quotient " + str(quotient) + " et pour reste " + str(reste))


# Exercice 7  
a = -9 
b = -3
c = 11
d = -7
# 1.
print((a-b)**2)
# 2. 
print(a**2 + 2*a*b + b**2) 
# 3.
print((a+c)/(c+d))  
# 4.
print((3)/(c+4))  


# Exercice 8  
#temperature_en_celsius = int(input("Entrez une température en degré Celsius"))
#temperature_en_farenheit = (temperature_en_celsius*1.8) + 32
#print(temperature_en_celsius, "degré Celsius équivaut à" + temperature_en_farenheit + "degré Farenheit")  


# Comparaisons   

# Exercice 9
#nombre_entree = input("Entrez un nombre : ")
#print(nombre_entree <= 0)

# Exercice 10 
#premier_nombre = input("Entrez un nombre : ")
#deuxieme_nombre = input("Entrez un nombre : ")
#print(premier_nombre > 0 and deuxieme_nombre <= 0)

# Exercice 11 
#nombre_entree = input("Entrez un nombre : ")
#print(nombre_entree%2 == 0)

# Exercice 12  
a = True
b = False
#print(not a)
#print(a and b)
#print(a or b)

# Exercice 13  
#premier_nombre = input("Entrez un nombre : ")
##deuxieme_nombre = input("Entrez un nombre : ")
#troisieme_nombre = input("Entrez un nombre : ")
#print(premier_nombre > 0 or (deuxieme_nombre < 0 and troisieme_nombre == 0))  

# Exercice 14  
#premier_nombre = input("Entrez un nombre : ")
#deuxieme_nombre = input("Entrez un nombre : ")
#troisieme_nombre = input("Entrez un nombre : ")
##print(not (premier_nombre > 5 and deuxieme_nombre < 12) or troisieme_nombre == 3)  # Affichera True

# Exercice 15 
def est_majeur():
    age = int(input("votre age ? : "))
    if age < 18:
        return "Vous êtes mineur"
    else:
        return "Vous êtes majeur"

# Exo 16
def est_positif():
    nb_entre = int(input("Entrez un nombre :"))
    if nb_entre == 0:
        return "Nul"
    elif nb_entre > 0:
        return "Positif"
    else:
        return "Négatif"

# Exo 17  
def compare():
    nb_1 = int(input("Entrez un nombre :"))
    nb_2 = int(input("Entrez un nombre :"))
    if nb_1 == nb_2 :
        return "égal"
    elif nb_1 > nb_2:
        return "plus grand"
    else:
        return "plus petit"

# Exo 18  
def nb_mystere():
    nb_secret = 7 
    nb_entre = int(input("Entrez un nombre :"))
    if nb_1 == nb_2 :
        return "égal"
    elif nb_1 > nb_2:
        return "plus grand"
    else:
        return "plus petit"  

# Exo 19  
def molky():
    score_precedent = int(input("score précédent ? "))
    nb_points_marques = int(input("nombre de points marqués ? "))
    nouveau_score = score_precedent + nb_points_marques
    if nouveau_score == 51:
        print("gagné !")
    else:
        if nouveau_score < 51:
            print("nouveau_score :", nouveau_score)
        else:
            print("nouveau_score : 25")


# Exo 20  
def bowling_v1():
    nb_quille_apres_boule_1 = int(input("nombre de quilles renversées après première boule :"))
    nb_quille_apres_boule_2 = int(input("nombre de quilles renversées après deuxième boule :"))
    if nb_quille_apres_boule_1 == 10:
        return "X"
    elif nb_quille_apres_boule_1 + nb_quille_apres_boule_2 == 10:
        return "/"
    else :
        return nb_quille_apres_boule_1 + nb_quille_apres_boule_2  

# Exo 21
def bowling_v2():
    nb_quille_apres_boule_1 = int(input("nombre de quilles renversées après première boule :"))
    if nb_quille_apres_boule_1 == 10:
        return "X"
    else:
        nb_quille_apres_boule_2 = int(input("nombre de quilles renversées après deuxième boule :"))
        if nb_quille_apres_boule_1 + nb_quille_apres_boule_2 == 10:
            return "/"
        else :
            return nb_quille_apres_boule_1 + nb_quille_apres_boule_2  
    
# Exo 22  
def bowling_v2():
    nb_quille_apres_boule_1 = int(input("nombre de quilles renversées après première boule :"))
    if nb_quille_apres_boule_1 < 0 or nb_quille_apres_boule_1 > 10:
        return "!"
    elif nb_quille_apres_boule_1 == 10:
        return "X"
    else:
        nb_quille_apres_boule_2 = int(input("nombre de quilles renversées après deuxième boule :"))
        if nb_quille_apres_boule_2 < 0 or nb_quille_apres_boule_2 > 10:
            return "!"
        elif nb_quille_apres_boule_1 + nb_quille_apres_boule_2 == 10:
            return "/"
        else :
            return nb_quille_apres_boule_1 + nb_quille_apres_boule_2  


from math import sqrt
# Exo 23  
def polynome(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        return "pas de solution"
    elif delta == 0:
        solution = -b / 2*a
        return "la solution est" + str(solution)
    else:
        s_1 = (-b + sqrt(delta)) / 2*a
        s_2 = (-b - sqrt(delta))/ 2*a
        return "les solutions sont s_1 : " + str(s_1) + " et s_2 : " + str(s_2)


# Exo 24 Billard
def billard():
    longueur = 6
    largeur = 10
    x = int(input("abscisse de la bille ? "))
    y = int(input("ordonnee de la bille? "))
    d_x = int(input("deplacement horizontal ? "))
    d_y = int(input("deplacement vertical ? "))
    x = x + d_x
    y = y + d_y 

    if x <= 0:
        x = -x
    elif x > longueur:
        rebond = x - longueur 
        x = longueur - rebond
    if y <= 0:
        y = -y
    elif y > largeur:
        rebond = y - largeur
        y = largeur - rebond

    return "x,y : ", str(x) +","+ str(y)
