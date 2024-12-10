valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= 100:
    cashback = valor_compra * 0.04
    print("O valor do seu cashback será:", cashback)
if valor_compra >= 100.01 and valor_compra <= 200:
    cashback = valor_compra * 0.06
    print("O valor do seu cashback será:", cashback)
if valor_compra >= 201.01 and valor_compra < 400:
    cashback = valor_compra * 0.08
    print("O valor do seu cashback será:", cashback)
if valor_compra >= 400:
    cashback = valor_compra * 0.1
    print("O valor do seu cashback será:", cashback)
