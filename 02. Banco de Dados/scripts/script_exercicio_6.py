import conexao as con

"""
Exercício 6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
comando_a_view = """
    SELECT nome,
           idade
    FROM   clientes
    WHERE  idade > 30
    ORDER  BY idade,
              nome
"""
comando_b_view = """
    SELECT Round(Avg(saldo), 2) AS 'Saldo médio clientes'
    FROM   clientes
"""
comando_c_view = """
    SELECT id,
           nome,
           saldo
    FROM   clientes
    ORDER  BY saldo DESC
    LIMIT  1
"""
comando_d_view = """
    SELECT Count(*) AS 'Total de clientes com saldo acima de 1000'
    FROM   clientes
    WHERE  saldo > 1000
    ORDER  BY saldo,
              nome
"""

# Executar comandos - (a)
print('\na) Selecione o nome e a idade dos clientes com idade superior a 30 anos.')
con.mostrar_dados(conexao, comando_a_view)
    
# Executar comandos - (b)
print('\nb) Calcule o saldo médio dos clientes.')
con.mostrar_dados(conexao, comando_b_view)
    
# Executar comandos - (c)
print('\nc) Encontre o cliente com o saldo máximo.')
con.mostrar_dados(conexao, comando_c_view)
    
# Executar comandos - (d)
print('\nd) Conte quantos clientes têm saldo acima de 1000.')
con.mostrar_dados(conexao, comando_d_view)    

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)