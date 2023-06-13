#Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
#juntamente com o maior, o menor e a media dos valores.

vetor = []

for i in range(5):
    valores = float(input('digite 5 valores: '))
    vetor.append(valores)
somaV = sum(vetor)
media = somaV/5
print(f'os valores inseridos foram {vetor} o maior valor e {max(vetor)} e o menor e {min(vetor)} contudo a media final dos valores e {media}')