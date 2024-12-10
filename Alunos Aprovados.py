qt_aprovados = int(input("Digite a quantidade de alunos aprovados: "))
qt_reprovados = int(input("Digite a quantidade de alunos reprovados: "))

qt_alunos = qt_aprovados + qt_reprovados

qt = qt_alunos - qt_reprovados

porcentagem = (qt / qt_alunos) * 100

print("A porcentagem de alunos aprovados na discplina é:", porcentagem, "%")