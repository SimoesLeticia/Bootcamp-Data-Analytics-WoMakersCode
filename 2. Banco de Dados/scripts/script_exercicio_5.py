import conexao as con

"""
Exercício 5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
Insira alguns registros de clientes na tabela.
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
comando_create_model = """
    CREATE TABLE IF NOT EXISTS clientes
      (
         id    INTEGER PRIMARY KEY,
         nome  VARCHAR(100),
         idade INTEGER,
         saldo DECIMAL(10, 2)
      ) 
"""
clientes = [
    ('João Silva', 30, 500.95),
    ('Maria Oliveira', 25, 277.80),
    ('Pedro Santos', 40, 875.00),
    ('Ana Sousa', 35, 1800.25),
    ('José Pereira', 28, 2200.50),
    ('Mariana Carvalho', 32, 3000.00),
    ('Carlos Martins', 45, 2500.75),
    ('Juliana Ferreira', 29, 1700.25),
    ('Fernando Almeida', 33, 2600.50),
    ('Patrícia Costa', 27, 2100.00),
    ('Rafael Barbosa', 38, 3200.75),
    ('Camila Gomes', 31, 98.00),
    ('Gabriel Ribeiro', 36, 440.15),
    ('Sara Santos', 26, 2300.00),
    ('Daniel Lima', 34, 2900.75),
    ('Amanda Rodrigues', 18, 3400.25),
    ('Marcos Ferreira', 42, 3600.50),
    ('Patrícia Silva', 37, 3100.00),
    ('Luisa Oliveira', 41, 3800.75),
    ('Ricardo Carvalho', 44, 4000.25),
    ('Zuleide Prado', 88, 12000)
]
comando_insert_model = """
    INSERT INTO clientes
                (nome,
                 idade,
                 saldo)
    VALUES      (?,
                 ?,
                 ?) 
"""
comando_view = """
    SELECT *
    FROM   clientes
    ORDER  BY id
"""

# Executar comandos - Criando a tabela clientes
con.executar_comando(conexao, comando_create_model)

# Executar comandos - Populando a tabela clientes
con.executar_comando_sequencia(conexao, comando_insert_model, clientes)

# Executar comandos - Visualizando a tabela clientes
con.mostrar_dados(conexao, comando_view)

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)