a = int(input("Un nombre de secondes : "))
nombre_d_heures = a//360
a = a%360
nombre_de_minutes = a//60
a = a%60
nombre_de_secondes = a
print(nombre_d_heures, nombre_de_minutes, nombre_de_secondes)