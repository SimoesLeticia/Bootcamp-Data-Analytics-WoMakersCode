import conexao as con

"""
Exercício 8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
Insira algumas compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
comando_create_model = """
    CREATE TABLE IF NOT EXISTS compras
      (
         id         INTEGER PRIMARY KEY,
         cliente_id INTEGER,
         produto    VARCHAR(60),
         valor      REAL,
         FOREIGN KEY (cliente_id) REFERENCES clientes(id)
      ) 
"""
compras = [
    (13, 'Smartphone modelo X', 500.00),
    (10, 'Smartwatch modelo Z', 250.50),
    (17, 'Smartphone modelo X', 500.00),
    (3,  'Laptop modelo Y', 1800.00),
    (9,  'Smartphone modelo X', 500.00),
    (12, 'Fone de ouvido modelo A', 99.90),
    (5,  'Laptop modelo Y', 1800.00),
    (14, 'Laptop modelo Y', 1800.00),
    (2,  'Laptop modelo Y', 1800.00),
    (7,  'Laptop modelo Y', 1800.00),
    (15, 'Fone de ouvido modelo A', 99.90),
    (4,  'Smartphone modelo X', 500.00),
    (19, 'Laptop modelo Y', 1800.00),
    (17, 'Laptop modelo Y', 1800.00),
    (21, 'Laptop modelo Y', 1800.00),
    (20, 'Smartphone modelo X', 500.00),
    (10, 'Laptop modelo Y', 1800.00),
    (4,  'Laptop modelo Y', 1800.00),
    (20, 'Smartphone modelo Z', 900.00),
    (16, 'Laptop modelo Y', 1800.00),
    (2,  'Smartwatch modelo Z', 250.50),
    (1,  'Smartphone modelo X', 500.00),
    (12, 'Smartphone modelo X', 500.00),
    (20, 'Tablet modelo B', 3500.00),
    (11, 'Laptop modelo Y', 1800.00),
    (8,  'Smartphone modelo X', 500.00),
    (15, 'Laptop modelo Y', 1800.00),
    (9,  'Laptop modelo Y', 1800.00),
    (12, 'Tablet modelo B', 3500.00),
    (3,  'Smartphone modelo X', 500.00),
    (5,  'Smartphone modelo X', 500.00),
    (13, 'Smartphone modelo Z', 900.00),
    (19, 'Fone de ouvido modelo A', 99.90),
    (13, 'Laptop modelo Y', 1800.00),
    (6,  'Smartwatch modelo Z', 250.50),
    (11, 'Smartphone modelo X', 500.00),
    (8,  'Laptop modelo Y', 1800.00),
    (1,  'Laptop modelo Y', 1800.00),
    (7,  'Fone de ouvido modelo A', 99.90),
    (6,  'Tablet modelo B', 3500.00) 
]
comando_insert_model = """
    INSERT INTO compras
                (cliente_id,
                 produto,
                 valor)
    VALUES      (?,
                 ?,
                 ?) 
"""
comando_view = """
    SELECT a.nome,
           b.produto,
           b.valor
    FROM   clientes a
           JOIN compras b
             ON b.cliente_id = a.id
    ORDER  BY a.nome,
              b.produto 
"""

# Executar comandos - Criando a tabela compras
con.executar_comando(conexao, comando_create_model)

# Executar comandos - Populando a tabela compras
con.executar_comando_sequencia(conexao, comando_insert_model, compras)

# Executar comandos - Visualizando a tabela compras
print('\nEscreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.')
con.mostrar_dados(conexao, comando_view)

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)