# Este é o módulo responsável pela conexão com o banco de dados. Todas as rotinas que interagem com o banco estão aqui.
import sqlite3
import pandas as pd

caminho_bd = '../data/bootcampDB.db'

def conectar_bd():
    try:
        conexao = sqlite3.connect(caminho_bd)
        if conexao:
            print('----- Conexão com banco de dados estabelecida com sucesso! -----')
        else:
            print('----- Falha ao estabelecer conexão com banco de dados. -----')
    except sqlite3.Error as error:
        print('----- Erro ao estabelecer conexão com banco de dados:', error, ' -----')    
    finally:
        return conexao

def fechar_conexao_bd(conexao):
    conexao.close()

def salvar_alteracoes_bd(conexao):
    conexao.commit()

def executar_comando(conexao, comando):
    cursor = conexao.cursor()
    try:
        cursor.execute(comando)
    except Exception as error:
        print('\n----- Erro ao executar comando:', error, ' -----')
    finally:
        print('\n----- Comando executado com sucesso! -----')    

def executar_comando_sequencia(conexao, comando, parametros):
    cursor = conexao.cursor()
    try:
        cursor.executemany(comando, parametros)        
    except Exception as error:
        print('\n----- Erro ao executar comando:', error, ' -----')
    finally:
        print('\n----- Comando executado com sucesso! -----')        

def mostrar_dados(conexao, comando):
    df = pd.read_sql_query(comando, conexao)
    print(df)

