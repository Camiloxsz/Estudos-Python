#O programa irá receber a altura e o sexo de uma determinada pessoa
#em seguida irá informar o peso ideal para essa pessoa.


altura = float(input("Digite sua altura(X.XX): "))
sexo = input("Digite seu sexo: ")

if sexo == 'homem':
    peso_ideal = (72.7 * altura) - 58
    print(f'O seu peso ideal é: {peso_ideal:.2f}')
if sexo == 'mulher':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é: {peso_ideal:.2f}')


    
