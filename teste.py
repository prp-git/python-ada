import csv

with open('NovalistaComMedia.csv', 'w', encoding='utf-8') as novocsv:
    escritor = csv.writer(novocsv)
    nova_lista = [1,2,3,4,5,6]
    num = 0
    for linha in nova_lista:
        print(type(linha))