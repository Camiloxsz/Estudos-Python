print("Este programa irá ler um numero real. Se o número for positivo ira imprimir a raiz quadrada. Do contrario irá imprimir o numero ao quadrado")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
      

n1 = int(input("Digite um numero real: "))

if n1 > 0:
    resultado = n1 ** 0.5
    print(f'A raiz quadrada de {n1} é: {resultado}')
elif n1 < 0:
    resultado = n1 ** 2
    print(f'O quadrado de {n1} é: {resultado}')
    
