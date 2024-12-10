qt_clientes = 0
qt_cupons =  0
maior_compra = -1
while True:
    valor = float(input("Digite u=o valor da compra: "))

    if valor > 0:
        qt_clientes += 1
    if valor > maior_compra:
        maior_compra = valor
    cupons = valor // 40
    qt_cupons += cupons
    if valor == 0 or valor < 0:
        break

print(qt_clientes)
print(qt_cupons)
print(maior_compra)
