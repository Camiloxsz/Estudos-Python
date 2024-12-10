salario = float(input("Digite seu salario: "))
valor_prestaçao = float(input("Digite o valor da prestação: "))
porcentagem = salario * 0.2 
if valor_prestaçao > porcentagem:
    print("Emprestimo não concedido.")
else:
    print("Emprestimo concedido.")
