#Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os valores lidos

numeros = []
for i in range(6):
    N = int(input("digite 6 numeros: "))
    numeros.append(N)

for indice in range(6):
    print(numeros[indice])
