import csv
import codecs

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv', 'rb')
    leitor = csv.reader(codecs.iterdecode(arquivo,'utf-8'))

    next(leitor)

    for home,como_funciona,contato, comprou in leitor:

        dado = [int(home),int(como_funciona)
            ,int(contato)]
        X.append(dado)
        Y.append(int(comprou))

    return X, Y