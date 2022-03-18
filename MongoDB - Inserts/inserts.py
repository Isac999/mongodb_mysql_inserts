import pandas as pd
import pymongo

df = pd.read_csv('dados.csv') #lendo o arquivo csv com pandas

lista = []

for index in df.index: #iterando apenas os indices do data frame
    objeto = { 
        'fechamento': float((df['Último'][index]).replace(',','.')), #localizando na coluna 'Último' cada linha atravéz do indice 
       'abertura': float((df['Abertura'][index]).replace(',','.')),
        'maximo': float((df['Máxima'][index]).replace(',','.')),
        'minimo': float((df['Mínima'][index]).replace(',','.')),
        'var': df['Var%'][index],
        'data': df['Data'][index]
    }
    lista.append(objeto)

try:
    connection = pymongo.MongoClient("localhost", 27017) #conectando ao mongodb no usuário local na porta padrão
    db = connection.trabalho_dolar #conectando ao banco de dados chamado 'trabalho_dolar'
    collection = db.user #conectando o banco de dados 'trabalho_dolar' a collection (tabela) padrão chamada 'user'
    for index, value in enumerate(lista): #buscando o indice e o valor dos elementos da lista
        collection.insert_one(lista[index]) #inserindo os dados na tabela do mongodb
    print('Dados inseridos!')
except:
    print('Houve algum erro na conexão com o Banco de Dados!')