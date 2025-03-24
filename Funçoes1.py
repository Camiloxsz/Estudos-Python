import random

## FUNÇOES ##

def gerar_lista(tam):
    lista = []
    for i in range(tam):
        valores = random.randint(0, 100)
        lista.append(valores)
    return lista

def exibir_lista(lista):
    print(lista)

def elementos_acima_media(lista):
    acima_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] > media:
            acima_media.append(lista[i])
    return acima_media

def elementos_abaixo_media(lista):
    abaixo_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] < media:
            abaixo_media.append(lista[i])
    return abaixo_media

def elementos_igual_media(lista):
    igual_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] == media:
            igual_media.append(lista[i])
    return igual_media

def qtd_acima_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] > media:
            qtd += 1
    return qtd

def qtd_abaixo_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] < media:
            qtd += 1
    return qtd

def qtd_igual_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] == media:
            qtd += 1
    return qtd

## MAIN ##

lista_gerada = gerar_lista(20)
print(lista_gerada)

exibir_lista = exibir_lista(lista_gerada)
print(exibir_lista)
print('----------------------------------')
el_acima_media = elementos_acima_media(lista_gerada)
print(el_acima_media)

el_abaixo_media = elementos_abaixo_media(lista_gerada)
print(el_abaixo_media)

el_igual_media = elementos_igual_media(lista_gerada)
print(el_igual_media)

print('----------------------------------')
qtd_acima = qtd_acima_media(lista_gerada)
print(qtd_acima)

qtd_abaixo = qtd_abaixo_media(lista_gerada)
print(qtd_abaixo)

qtd_igual = qtd_igual_media(lista_gerada)
print(qtd_igual)

print('----------------------------------')
print('O PROGRAMA ENCERROU')
