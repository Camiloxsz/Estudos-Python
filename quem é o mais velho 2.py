nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

if idade1 > idade2:
    mais_velho = idade1
    print(f'{nome1} é mais velho')
if idade2 > idade1:
    mais_velho = idade2
    print(f'{nome2} é mais velho')

if idade1 == idade2:
    print("As idades são iguais")
