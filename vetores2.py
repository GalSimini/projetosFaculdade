#Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui.

vetor10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
par = 0


for i in range(10):
    if vetor10[i]%2 != 1:
        par += 1
        print(vetor10[i])
print(f'esse vetor possui {par} numeros pares')