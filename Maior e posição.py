maior = -1
posicao = 0

for i in range(1,101):
    n = int(input("Digite um valor inteiro: "))
    if n > maior:
        maior = n
        posicao = i
print(maior)
print(posicao)