n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

if n1 > 0.0 and n2 <= 10.0:
    media = (n1 + n2) / 2
    print(f'A media das notas é: {media}')
else:
    print("A nota não é valida.")
