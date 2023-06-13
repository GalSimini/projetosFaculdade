#Faca um programa que receba 6 numeros inteiros e mostre:
#• Os numeros pares digitados;
#• A soma dos numeros pares digitados;
#• Os numeros  ́ımpares digitados;
#• A quantidade de numeros ́ımpares digitados


par = []
impar = []

for i in range(6):
    numero = int(input("digite 6 numeros inteiro: "))
    if numero %2 !=1:
        par.append(numero)
    else:
        impar.append(numero)

print(f'foram digitados esses numeros pares {par}')
print(f'a soma de todos os numeros pares e {sum(par)}')
print(f'esses foram os numeros impares digitados {impar}')
print(f'a quantia de numeros impares digitados e {len(impar)}')