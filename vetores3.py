#Faca um programa que receba do usuario um vetor com 10 posicoes. Em seguida devera
#ser impresso o maior e o menor elemento do vetor


vetor = []

for i in range(10):
    numeros = int(input("digite 10 numeros: "))
    vetor.append(numeros)
maiorN = max(vetor)
menorN = min(vetor)
print(f'o maior numero do vetor e {maiorN} e o menor numero e {menorN}')