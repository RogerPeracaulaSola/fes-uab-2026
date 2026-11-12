###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
numero= 10
while numero >0:
    print(numero)
    numero-=1
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
numero = 20
suma=0
while numero >0:
    if numero%2 == 0:
        suma += numero
    numero -=1
print(f"la suma de numeros parelles es: {suma}")




# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

num = int(input("escriu un numero enter positiu: "))
num_inicial = num
fact =1
while num>0:
    fact *= num
    num -= 1
print(f"el factoriar de {num_inicial} es: {fact}")







# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

while True:
    contra = input("escriu una contra de 8 caracters: ")
    if len(contra)>7:
        break
print("Contrasenya vàlida")







# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
num = int(input("Introdueix un número: "))
comptador = 1

while comptador <= 10:
    resultat = num * comptador
    print(f"{num} x {comptador} = {resultat}")
    comptador += 1


# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
n = int(input("Introdueix un número enter positiu N: "))
num = 2

while num <= n:
    es_primer = True
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            es_primer = False
            break
        divisor += 1
    if es_primer:
        print(num)
    num += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
suma = 0

while True:
    numero = int(input("Introdueix un número enter: "))
    if numero == 0:
        break
    suma += numero

print(f"La suma total és: {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
num = int(input("Introdueix un número enter positiu: "))
xifres = 0

if num == 0:
    xifres = 1
else:
    while num > 0:
        num //= 10
        xifres += 1

print(f"El nombre de xifres és: {xifres}")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
n = int(input("Quants termes de Fibonacci vols veure?: "))

a = 0
b = 1
comptador = 0

while comptador < n:
    print(a, end=" ")
    seguent = a + b
    a = b
    b = seguent
    comptador += 1
# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
num_secret = 7
while True:
    num_usuari = int(input("endevina el numero: "))
    if num_secret == num_usuari:
        print("molt be, has endevinat el numero ", num_secret)
        break
    elif num_secret > num_usuari:
        print("el numero secret es mes gran")
    else: 
        print("el numero secret es mes petit")

