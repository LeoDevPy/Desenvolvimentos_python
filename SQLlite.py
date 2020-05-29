# APLICAÇÃO COM SQL LITE.

import sqlite3


con = sqlite3.connect('escola.db')

print(type(con))

cur =  con.cursor() # cursos para percorrer as linhas 


#CRIANDO A TABELA
sql_create = 'create table cursos (id integer primary key, titulo varchar(100), categoria varchar(140))'

#EXCUTANDO O CURSOS 
#cur.execute(sql_create)


#INSERINDO OS REGISTROS LOGO ABAIXO
sql_insert = 'insert into cursos values (?,?,?)'

recset = [(1000, 'Ciencias de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Analise de Dados')]

#for rec in recset:
#    cur.execute(sql_insert, rec)
    
#con.commit()

sql_select = 'select * from cursos'

cur.execute(sql_select) #seleciona todos os registros e recupera os registros
dados = cur.fetchall()


# MOSTRA OS DADOS
#for linha in dados:
    #print('Curso id: %d, titulo: %s, categoria: %s \n' % linha) 
    


#recset = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
         # (1004, 'R Fundamentos', 'Analise de Dados')]

#for rec in recset:
  #  cur.execute(sql_insert, rec)
    

#con.commit()

cur.execute('select * from cursos')

recset = cur.fetchall()

for rec in recset:
    print('Curso id: %d, titulo: %s, categoria: %s \n' % rec)
    

con.close()