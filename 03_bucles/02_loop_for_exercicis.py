###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nums_parells =[print(num) for num in numeros if num%2 == 0]
# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
numeros = [10, 20, 30, 40, 50]
suma = 0
quant=0
for idx, num in enumerate(numeros):
    suma += num
    quant = idx+1
print(f"la mitjana es {suma/quant}")

    

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
numeros = [15, 5, 25, 10, 20]
maxim = 0
for num in numeros:
    if num > maxim:
        maxim = num
print(maxim) 


# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
llista_5 =[paraula for paraula in paraules if len(paraula)>5]
print(llista_5)

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", 8"arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra = input("escriu la lletra que vols: ")
lletra_m = lletra.upper()
num=0
for paraula in paraules: 
    for lletra_b in paraula:
        if lletra_b==lletra or lletra_b==lletra_m:
            num += 1
        break
print(num)




# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
# tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
suma = 0
quant=0
for idx, num in enumerate(tensions):
    suma += num
    quant = idx+1
print(f"la mitjana es {suma/quant}")



# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
resistencies = [100, 220, 470, 1000]
tensio = 12
for resistencia in resistencies:
    corrent = tensio / resistencia
    print(f"Corrent a través de la resistència {resistencia} Ω: {corrent} A")

# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
# nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
nivells_soroll = [-92, -85, -78, -95, -81, -88]
num=0
for nivell in nivells_soroll:
    if nivell > -80:
        num += 1
print(f"Nombre de mostres que superen el llindar: {num}")

# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
# bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
# bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
bits_dif=0
bits_totals=0
for idx, num in enumerate(bits_transmesos):
    if num != bits_rebuts[idx]:
        bits_dif +=1
    bits_totals +=1
print(f"{bits_dif}/{bits_totals}")


# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
# frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
