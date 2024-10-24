import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'philipi',
    host = 'localhost',
    password = 'projeto_crud',
    db = 'projeto_crud'
)

if conn.is_connected():
    print('Banco de dados conectado com sucesso')
else:
    print('Não conectado com o banco')