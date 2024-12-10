qt_aulas = int(input("Digite a quantidade total de aulas da disciplina: "))
qt_faltas = int(input("Digite a quantidade de faltas na disciplina: "))

aulas_frequentadas = qt_aulas - qt_faltas

frequencia = (aulas_frequentadas / qt_aulas) * 100

print("Sua frequencia na disciplina é de:", frequencia,"%")