#Escreva um programa, em Python, para obter 03 (três) notas, calcular e exibir a média
#aritmética dessas notas.

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
print(f"A média é: {media:.2f}")