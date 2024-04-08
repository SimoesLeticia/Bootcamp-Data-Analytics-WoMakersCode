import conexao as con

"""
Exercício 4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
comando_a_view = """
    SELECT nome,
           idade
    FROM   alunos
    WHERE  id = 4
"""
comando_a_model = """
    UPDATE alunos
    SET    idade = idade + 10
    WHERE  id = 4
"""
comando_b_view = """
    SELECT id,
           nome
    FROM   alunos
    ORDER  BY id    
"""
comando_b_model = """
    DELETE FROM alunos
    WHERE  id = 4
"""

# Executar comandos - (a)
print('\na) Atualize a idade de um aluno específico na tabela. (ANTES DA ATUALIZAÇÃO).')
con.mostrar_dados(conexao, comando_a_view)

con.executar_comando(conexao, comando_a_model)

print('\na) Atualize a idade de um aluno específico na tabela. (APÓS ATUALIZAÇÃO).')
con.mostrar_dados(conexao, comando_a_view)

# Executar comandos - (b)
con.executar_comando(conexao, comando_b_model)
    
print('\nb) Remova um aluno pelo seu ID (4. Ana Clara Silva Gomes). (APÓS EXCLUSÃO).')
con.mostrar_dados(conexao, comando_b_view)

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)
