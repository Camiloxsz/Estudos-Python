n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
nf = int(input("Digite a nota final: "))

media_semestral = (n1 + n2 + n3) / 3
media_final =  (media_semestral + nf) / 2

print("------------------------------------------------")
print(f"Sua media semestral é: {media_semestral:.2f}")
print(f'Sua media final é: {media_final:.2f}')
print("------------------------------------------------")

if media_final >= 70:
    print("Aprovado.")
if media_final >= 40:
    print("Apto a fazer final.")
else:
    print("Reprovado.")