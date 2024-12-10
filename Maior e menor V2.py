n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
    print(f'O {n1} é maior que o {n2}.')
elif n2 > n1:
    print(f'O {n2} é maior que o {n1}.')

diferença = n1 - n2
print(f'A diferença entre eles é de: {diferença}')
