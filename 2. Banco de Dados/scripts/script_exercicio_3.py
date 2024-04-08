import conexao as con

"""
Exercício 3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
d) Contar o número total de alunos na tabela.
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
comando_a_view = """
    SELECT *
    FROM   alunos
    ORDER  BY id
"""
comando_b_view = """
    SELECT nome,
           idade
    FROM   alunos
    WHERE  idade > 20
    ORDER  BY idade,
              nome
"""
comando_c_view = """
    SELECT *
    FROM   alunos
    WHERE  curso = 'Engenharia'
    ORDER  BY nome
"""
comando_d_view = """
    SELECT Count(*) AS 'Total de Alunos'
    FROM   alunos
"""

# Executar comandos - (a)
print('\na) Selecionar todos os registros da tabela "alunos".')
con.mostrar_dados(conexao, comando_a_view)
    
# Executar comandos - (b)
print('\nb) Selecionar o nome e a idade dos alunos com mais de 20 anos.')
con.mostrar_dados(conexao, comando_b_view)
    
# Executar comandos - (c)
print('\nc) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.')
con.mostrar_dados(conexao, comando_c_view)
    
# Executar comandos - (d)
print('\nd) Contar o número total de alunos na tabela.')
con.mostrar_dados(conexao, comando_d_view)    

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)
