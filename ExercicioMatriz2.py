#Escreva um programa para resolver os seguintes pontos.
#01) Declarar a matriz;
#02) Exibir o elemento que está na linha 1 coluna 3;
#03) Adicionar o valor 10 ao elemento que está na linha 2 coluna 2;
#04) Alterar todos os elementos que estão na linha 2 para 200;
#05) Exibir a soma dos elementos que estão na linha 1;
#06) Exibir a soma dos elementos que estão na coluna 3.



#declarar a matriz
matriz = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
for linha in matriz:
    print(linha)
print('-------------')

#exbir o elemento que esta na linha 1 coluna 3
print('Elemento linha 1 coluna 3:', matriz[1][3])
print('-------------')

#adicionar o valor 10 ao elemento que esta na linha 2 coluna 2
matriz[2][2] = 10
print('Matriz atualizada:')
for linha in matriz:
    print(linha)
print('-------------')

#Alterar todos os elementos que estão na linha 2 para 200
for i in range(3):
    for j in range(4):
        matriz[2][j] = 200
print('Matriz atualizada 2:')       
for linha in matriz:
    print(linha)
print('-------------')

#Exibir a soma dos elementos que estão na linha 1
soma = 0
for num in matriz[1]:
    soma += num
print("A soma de todos os elementos na linha 1 é:", soma)

#Exibir a soma dos elementos que estão na coluna 3
soma_coluna = 0
for i in range(len(matriz)):
    soma_coluna += matriz[i][3]
print("A soma de todos os elementos na coluna 3 é:", soma_coluna)

