import mysql.connector

db = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'fuckthepolice123',
    database = 'pessoas'
)
cursor = db.cursor()
"""
insert = '''INSERT INTO caracteristicas
(nome,nascimento,peso,altura)
VALUES (%s,%s,%s,%s)'''
values = ('Cassilda','1993-03-27','53.76','1.69')
cursor.execute(insert, values)
db.commit()
"""
#Usando dicionarios
dicionario = {}
atributos = ('nome', 'nascimento', 'peso', 'altura')
lista = ('Juliana','1988-05-15','67.01','1.67')
cont = 0
for item in atributos:
    dicionario[item] = lista[cont]
    cont = cont + 1
insert = '''INSERT INTO caracteristicas
(nome,nascimento,peso,altura)
VALUES (%s,%s,%s,%s)'''
values = []
for item in atributos:
    values.append(dicionario[item])
cursor.execute(insert, values)
db.commit()