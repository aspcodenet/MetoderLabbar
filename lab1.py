#Skapa ett program med en ny metod. 
# Metoden skall ta emot två inparametrar
#  av typen string och slå ihop dom till en sträng
#  och returnera det nya värdet. Anropa den
#  nya metoden från Main och skriv ut resultatet på
#  skärmen.

def PlussaStrings(string1, string2):
    r = string1 + string2
    return r

a = "sdasdad"
b = "42324243"
resultat = PlussaStrings(a,b)
print(resultat)


