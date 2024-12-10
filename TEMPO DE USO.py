tempo_inicioH = int(input("Digite o a hora que iniciou o uso da maquina(EM HORA); "))
tempo_inicioM = int(input("Digite o a hora que iniciou o uso da maquina(EM MINUTO); "))
tempo_inicioS = int(input("Digite o a hora que iniciou o uso da maquina(EM SEGUNDO); "))

tempo_finalH = int(input("Digite a hora que finalizou o uso da maquina(EM HORA): "))
tempo_finalM = int(input("Digite a hora que finalizou o uso da maquina(EM MINUTO): "))
tempo_finalS = int(input("Digite a hora que finalizou o uso da maquina(EM SEGUNDO): "))


H_inicio = tempo_finalH - tempo_inicioH
H_inicio2 = tempo_finalM - tempo_inicioM
H_inicio3 = tempo_finalS - tempo_inicioS

print(H_inicio, ":", H_inicio2, ":", H_inicio3)
