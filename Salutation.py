# exemple de Fonction qui utilise des variables globales = ligne 4 et 5
# dont le resultat depend de la valeur des variables globales  et pas uniquement des parametres déclarés

formulePolitesseMonsieur = "Bonjour Monsieur"
formulePolitesseMadame = "Bonjour Madame"


def saluer(nom, homme=True):
    if homme:
        return formulePolitesseMonsieur + nom
    else:
        return formulePolitesseMadame + nom


message = saluer("Dupont",False)
formulePolitesseMadame=("Bonjour Madame ou mademoiselle")
message2 = saluer("Dupont",False)

print(message)
print(message2)

print("==============")

# voici un example de Fonction pure qui utilise des variable Locales Lig 25 et 26
def saluer2(nom, homme=True):
    formulePolitesseMonsieur="Bonjour Monsieur"
    formulePolitesseMadame="Bonjour Madame"
    if homme:
        return formulePolitesseMonsieur + nom
    else:
        return formulePolitesseMadame + nom

message = saluer2("Hirsh", False)
formulePolitesseMadame = "Bonjour Madame ou Mademoiselle " # ici Variable Globale
message2 = saluer2("Hirsh",False)
print(message)
print(message2)

print("==============")
# exemple de fonction pur
cube = lambda x: x*x*x
exponent = lambda x,n : x**n
repeter = lambda x : x*10
toto= lambda x:x+3

print(cube(4))
print(exponent(10,3))
print(repeter("ok "))
print(toto(5))



