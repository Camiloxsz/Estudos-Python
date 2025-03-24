import random 
#Escreva um programa para gerar uma matriz 40 x 6, contendo valores aleatórios entre 1
#e 20. Leia um número do usuário e exibia:
#● Quantas vezes esse valor aparece na matriz;
#● Qual é o maior valor e o menor valor da matriz.


#Variaiveis
qt = 0

maior = -1
menor = 21

#Declarando a matriz

linhas = 40
colunas = 6

matriz = []

for i in range(linhas):
    matriz.append([None] * colunas)
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(0, 20)

#Ler do usuario
numero = int(input("Informe um numero de 0 a 20: "))

#Encontrando o maior e menor valor e a quantidade de vez que N aparece

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == numero:
            qt += 1
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]
#Exibiçãp
            
for linha in matriz:
    print(linha)
print(f'Quantidade de vez que {numero} aparece na matriz:', qt)
print('Maior numero da matriz:', maior)
print('Menor numero da matriz:', menor)

