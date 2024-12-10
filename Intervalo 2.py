contador_in = 0
contador_out = 0
n = int(input("Digite o numero de casos de teste: "))
for i in range(n):
    x = int(input("Digite um valor inteiro: "))
    if x > 20 or x < 10:
        contador_out += 1
    else:
        contador_in += 1
print(f'{contador_in} in')
print(f'{contador_out} out')
