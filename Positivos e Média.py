contador_positivo = 0
soma = 0

for i in range(6):
    n1 = float(input("Digite um numero: "))

    if n1 > 0:
        contador_positivo += 1
        soma = soma + n1
media = soma / contador_positivo
print(soma)
print(f'{contador_positivo} valores positivos')
print(media)
