score = int(input("Entrer le score :"))
nb_zeros = 0
gain = int(input("Entrer le gain :"))

nouveau_score = score + gain

if nouveau_score < 51:
    print("Nouveau score :", nouveau_score )
elif nouveau_score == 51:
    print("Gagne !")
else:
    nouveau_score = 25
    print("Trop grand ! Nouveau score : 25")
if nouveau_score == nb_zeros:
    print("Perdu !")
    
    
print("Fin du Tour")

