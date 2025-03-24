import random

#Uma turma tem 40 alunos, cada aluno tem 03 notas. Escreva um programa para
#armazenar todas as notas em uma matriz. Ao final, seu programa deverá:
#● Exibir a média de cada aluno;
#● Calcular e exibir a média da turma;
#● Quantos alunos possuem nota maior do que a média da turma.
#Atenção!
#Para facilitar os testes considere:
#- Gerar as notas aleatoriamente (entre 0 e 100);
#- Reduzir o número de alunos.


#Declara a matriz com numeros aleatorios de 0 a 100
linhas = 3
colunas = 3

matriz = []

for i in range(linhas):
    matriz.append([None] * colunas)
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(0,100)
for linha in matriz:
    print(linha)

#Realiza a soma de cada aluno e da turma respectivamente    
soma_turma = 0

for i in range(linhas):
    soma = 0
    for notas in matriz[i]:
        soma += notas
    media = soma / colunas
    soma_turma += media
    print(f'Aluno {i + 1}: Media = {media:.2f}')
media_turma = soma_turma / linhas
print(f"\nMédia da turma: {media_turma:.2f}")
