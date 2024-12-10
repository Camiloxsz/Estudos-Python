honestos = 0
desonestos = 0

for i in range(10):
    a, b = input("Digite o preço do produto antes e durante a promoção: ").split()
    a = float(a)
    b = float(b)

    if b > a:
        desonestos += 1  
    else:
        honestos += 1

porcentagem = (honestos * 1000) / 100
porcentagem2 = (desonestos * 1000) / 100

print(f'honestos: {honestos} ({porcentagem}%)')
print(f'desonestos: {desonestos} ({porcentagem2}%)')
