#Faca um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a media geral

notas = []

for i in range(15):
    nota = float(input("digite a nota dos alunos para obter a media: "))
    notas.append(nota)
somaDasNotas = sum(notas)
media = somaDasNotas/15
print(f'a meida das notas dos alunos e {media}')
