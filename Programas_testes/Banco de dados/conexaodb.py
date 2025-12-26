#from sqlalchemy import create_engine #para qualquer banco 
import sqlite3
from pathlib import Path

# https://docs.python.org/3/library/sqlite3.html (acesso a documentação da biblioteca)
'''
#configurar conexão mysql
db_conexao_banco = 'mysql+pymysql://root:@localhost:3306/bootcamp' #endereço e porta do banco de dados no Mysql
db_conexao = create_engine(db_conexao_banco) # cria a conexão por meio do create engine no endereço definido'''

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'bootcamp_magalu.db')
print(conexao.__class__.__name__)

cursor = conexao.cursor()
#cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))') # Cria a tabela

def inserir_registro(conexao,cursor,nome,email):
    data = (nome,email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);',data)
    #conexao.commit() #atualizar os dados inseridos

def update_registro(conexao,cursor,nome,email,id):
    data = (nome,email,id)
    cursor.execute('UPDATE TABLE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()


inserir_registro(conexao,cursor,'nais','asdasd@gmail.com')
#inserir_registro(conexao,cursor,'gustavo','gustavo@gmail.com')