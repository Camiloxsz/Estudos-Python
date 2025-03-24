import random


## FUNÇÕES ##

def soma_negativos(numeros): #Somar todos os numeros negativos
    soma = 0
    for i in range(len(numeros)):
        if numeros[i] < 0:
            soma = sum(numeros)
    return soma

def media_valores(numeros): #Média de todos os valores
    media = sum(numeros) / len(numeros)
    return media

def menor_maior(numeros): #Menor e maior valor
    menor = 101
    maior = -101
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
    return menor, maior

def verificar_se_tem_100(numeros): #Verificar se tem 100 no vetor
    for i in range(len(numeros)):
        if numeros[i] == 100:
            print("Tem o numero 100")
            break
        
def verificar_zero(numeros): #Verificar se tem 0 no vetor
    qt = 0
    for i in range(len(numeros)):
        if numeros[i] == 0:
            qt += 1
    return qt

def numeros_pares(numeros): #Gerar um novo vetor contendo numeros pares
    numeros_pares = []
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            numeros_pares.append(numeros[i])
    return numeros_pares

def numeros_distintos(numeros): #Gerar um novo vetor contendo numeros distintos
    distintos = []
    for i in range(len(numeros)):
        if numeros[i] not in distintos:
            distintos.append(numeros[i])
    return distintos
        

## MAIN ##

numeros = [None] * 10

for i in range(10):
    numeros[i] = random.randint(-100, 100)

soma_neg = soma_negativos(numeros)
print(f'Soma de todos os numeros negativos', soma_neg)
print('-----------------------------------------')

media_geral = media_valores(numeros)
print(f'Média de todos os valores:', media_geral)
print('-----------------------------------------')

maior_menor = menor_maior(numeros)
print(f'O menor e o maior numero respectivamente:', maior_menor)
print('-----------------------------------------')

verificador = verificar_se_tem_100(numeros)

verificador_0 = verificar_zero(numeros)
print(f'Quantidade de 0 no vetor:', verificador_0)
print('-----------------------------------------')

vetor_pares = numeros_pares(numeros)
print(f'Novo vetor contendo numeros pares:', vetor_pares)
print('-----------------------------------------')

distintos = numeros_distintos(numeros)
print(f'Novo vetor com numeros distintos:', distintos)

ordenados = ordenados(numeros)
print(ordenados)

print('-----------------------------------------')
print(numeros)
