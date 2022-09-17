import csv

def media_notas(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

nova_lista = []

with open('alunos.csv', 'r', encoding='utf-8') as file:
    leitor = csv.reader(file)
    num_linha = 0
    for linha in leitor:
        if num_linha == 0:
            linha.append('Média')
        else:
            linha.append(media_notas(float(linha[3]),float(linha[4]),float(linha[5]),float(linha[6]),))
        
        nova_lista.append(linha)
        
        num_linha += 1
        
print(nova_lista)


with open('alunos_media.csv', 'w', encoding='utf-8') as novocsv:
    escritor = csv.writer(novocsv)
    num = 0
    for linha in nova_lista:
        escritor.writerow(nova_lista[num])
        num += 1