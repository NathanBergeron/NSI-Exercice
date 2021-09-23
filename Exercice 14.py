n = int(input("combien d'oeufs : "))
#print(n // 6) #ce programme n'est correct que pour les multiples de 6
#print(n // 6 + 1) #n est pas non plus correct car on ne rajoute pas de boites pour les multiples de 6
a = n//6
b = n%6
print(a,"boîtes d' oeufs pleines")
print(b,"oeufs restants")