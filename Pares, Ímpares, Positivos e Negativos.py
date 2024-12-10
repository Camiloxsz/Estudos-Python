contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0


for i in range(5):
    n1 = int(input("Digite um valor inteiro: "))

    if n1 < 0:
        contador1 += 1
    elif n1 > 0:
        contador2 += 1
    if n1 % 2 == 1:
        contador3 += 1
    if n1 % 2 == 0:
        contador4 += 1
        
print(f'{contador4} valor(es) par(es)')
print(f'{contador3} valor(es) impar(es)')
print(f'{contador1} valor(es) negativ(os)')
print(f'{contador2} valor(es) positivo(s)')


