import conexao as con

"""
Exercício 1. 
Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
comando_model = """
    CREATE TABLE IF NOT EXISTS alunos
      (
         id    INTEGER PRIMARY KEY,
         nome  VARCHAR(100),
         idade INTEGER,
         curso VARCHAR(30)
      ) 
"""

# Executar comandos
con.executar_comando(conexao, comando_model)

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)