n1 = int(input("Digite um número: "))

if n1 > 0:
    resultado = n1 ** 2
    resultado2 = n1 ** 0.5
    print('---------------------------------------------')
    print(f'O número digitado ao quadrado é: {resultado}')
    print('---------------------------------------------')
    print(f'A raiz quadrada do numero digitado é: {resultado2:.2f}')
else:
    print("O numero é invalido.")
