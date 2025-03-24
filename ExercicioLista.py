import random

#Variaveis
soma = 0
soma_todos = 0
maior = -11
menor = 11
qtd = 0

# declarar o vetor
numeros = [None] * 10
# preencher o vetor com valores aleatórios
for i in range(10):
    numeros[i] = random.randint(-10,10)
# exibir o vetor
for i in range(len(numeros)):
    print(numeros[i])
#somar todos os numeros negativos
for i in range(len(numeros)):
    if numeros[i] < 0:
        soma += numeros[i]
#media de todos os valores armazenados
for i in range(len(numeros)):
    soma_todos += numeros[i]
    media = soma_todos / len(numeros)
#menor e maior valores armazenados
for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
#verificar se tem 100 no vetor
for i in range(len(numeros)):
    if 10 in numeros:
        print("Tem o numero 10")
        break
    else:
        print("Não tem o numero 10")
        break
#Quantidade de vezes que o 0 aparece
    for i in range(len(numeros)):
        if 0 in numeros[i]:
            qtd =+ 1
#Verificar se uma posição aleatória (p) e seu sucessor (p + 1) possuem valores
#ordenados;
p = random.randint(0, len(numeros) - 2)
print("-----------------------")
print(f"Índice escolhido: {p}")
print(f"Valores: {numeros[p]} e {numeros[p + 1]}")
if numeros[p] < numeros[p + 1]:
    print("Os valores estao ordenados em ordem crescente")
elif numeros[p] > numeros[p + 1]:
        print("Os valores estao ordenados em ordem decrescente")
print('-----------------------')

#Quais são os índices (i) que possuem valores ordenados com seus respectivos
#sucessores (i+1);

ordenados = []
for i in range(len(numeros)):
    if numeros[p] < numeros[p + 1]:
        ordenados.append(i)

# Verificar se o vetor está completamente ordenado


print(f'A soma de todos o numeros negativos é:', soma)
print(f'A media de todos os valores armazenados é:', media)
print(f'O menor valor é:', menor)
print(f'O maior valor é:', maior)
print(f'Numeros ordenados:',ordenados)

