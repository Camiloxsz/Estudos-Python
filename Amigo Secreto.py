import random

nomes = []
email = []

# Pedir o nome e o email
while True:
    nome = input('Digite o nome: ')
    
    # Verificar se o nome está vazio e sair do loop
    if nome == '':
        break
    
    # Pedir o email
    emails = input("Digite o email: ")
    nomes.append(nome)
    email.append(emails)

# Embaralhar os nomes e emails
tamanho = len(nomes)
for i in range(6):  # Embaralhar 6 vezes
    i1 = random.randint(0, tamanho - 1)
    i2 = random.randint(0, tamanho - 1)
    
    # Permutando nomes
    nomes[i1], nomes[i2] = nomes[i2], nomes[i1]

    # Permutando emails
    email[i1], email[i2] = email[i2], email[i1]

# Exibir a lista de quem vai dar presente a quem
for i in range(tamanho):
    proximo = i + 1
    if proximo == tamanho:
        proximo = 0
    print(f'{nomes[i]} ({email[i]}) vai dar presente para {nomes[proximo]} ({email[proximo]})')
