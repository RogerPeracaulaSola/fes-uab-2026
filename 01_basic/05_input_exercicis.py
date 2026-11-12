###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic, nom_xarxa = input("escriu el nom del tecnic i el de la xarxa separats per un espai: ").split()
print(f"el tecnic es diu {nom_tecnic} i el nom de la xarxa es {nom_xarxa}")



# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud, velocitat = input("escriu la longitud de l'enllaç en km i la velocitat de transmissió en Gbps separats per un espai: ").split()
longitud = float(longitud)  
velocitat = float(velocitat)/8.0
temps=longitud/velocitat
print(f"per transmetre 1 GB de dades caldrien {temps} segons")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores, preu_hora, preu_material = input("escriu el nombre d'hores de feina, el preu per hora i el preu del material separats per un espai: ").split()
hores = float(hores)
preu_hora = float(preu_hora)
preu_material = float(preu_material)
cost_total = hores * preu_hora + preu_material
print(f"el cost total de la instal·lació és de {cost_total} €")