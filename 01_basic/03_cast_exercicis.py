###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
total_paquets = int(input("Introdueix el nombre de paquets rebuts: ")) + 1200
print("El total de paquets és:", total_paquets)
# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
conexio = float(input("Introdueix la velocitat en Mbps: "))
print("La velocitat es: ", conexio/8, "MB/s")