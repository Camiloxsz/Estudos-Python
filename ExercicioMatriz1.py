#Escreva um programa para ler duas matrizes (A e B), ambas de ordem 2x4, contendo
#números inteiros. Seu programa deverá gerar uma matriz C resultante da soma de A com B.
#Ao final exiba todas as matrizes.


#Declara a Matriz A
linhas = 2
colunas = 4

matriz_A = []

for i in range(linhas):
    matriz_A.append([None] * colunas)

for i in range(linhas):
    for j in range(colunas):
        matriz_A[i][j] = int(input(f'elemento {i}, {j}: '))
print('Agora você ira digitar os elementos da matriz B')

#Declara a Matriz B
matriz_B = []

for i in range(linhas):
    matriz_B.append([None] * colunas)
for i in range(linhas):
    for j in range(colunas):
        matriz_B[i][j] = int(input(f'elemento {i}, {j}: '))

#Declara a Matriz C
matriz_C = []

for i in range(linhas):
    matriz_C.append([None] * colunas)
for i in range(linhas):
    for j in range(colunas):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]
        
#Exibição        
print('Matriz A:')     
for linha in matriz_A:
    print(linha)
print('-------')
print('Matriz B:')     
for linha in matriz_B:
    print(linha)
print('-------')
print('Matriz C:')     
for linha in matriz_C:
    print(linha)
    
