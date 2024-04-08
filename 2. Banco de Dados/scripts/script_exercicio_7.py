import conexao as con

"""
Exercício 7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID.
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
comando_a_view = """
    SELECT nome,
           saldo
    FROM   clientes
    WHERE  id = 18
"""
comando_a_model = """
    UPDATE clientes
    SET    saldo = 0
    WHERE  id = 18
"""
comando_b_view = """
    SELECT id,
           nome
    FROM   clientes
    ORDER  BY id    
"""
comando_b_model = """
    DELETE FROM clientes
    WHERE  id = 18
"""

# Executar comandos - (a)
print('\na) Atualize o saldo de um cliente específico. (ANTES DA ATUALIZAÇÃO).')
con.mostrar_dados(conexao, comando_a_view)

con.executar_comando(conexao, comando_a_model)

print('\na) Atualize o saldo de um cliente específico. (APÓS ATUALIZAÇÃO).')
con.mostrar_dados(conexao, comando_a_view)

# Executar comandos - (b)
con.executar_comando(conexao, comando_b_model)
    
print('\nb) Remova um cliente pelo seu ID (18. Patrícia Silva). (APÓS EXCLUSÃO).')
con.mostrar_dados(conexao, comando_b_view)

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)
