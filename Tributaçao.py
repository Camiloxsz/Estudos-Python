dolar = float(input("Digite a cotaçao do dolar hoje: "))
valor_compra = float(input("Digite o valor da compra em dolar: "))
valor_em_reais = dolar * valor_compra

taxa_importaçao = valor_em_reais * 0.2
taxa_icms = valor_em_reais * 0.17

valor_final = valor_em_reais + taxa_importaçao + taxa_icms

print("O valor da taxa de importaçao em reias é", taxa_importaçao)
print(f'O valor da taxa de icms em reais é: '{taxa_icms:.2f])
print("O valor da total é:", valor_final)

