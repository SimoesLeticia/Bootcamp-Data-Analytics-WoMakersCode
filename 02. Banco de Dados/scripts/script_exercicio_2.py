import conexao as con

"""
Exercício 2.
Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
"""

# Conectar com banco
conexao = con.conectar_bd()

# Comandos SQL
alunos = [
    ('João Miguel dos Santos', 20, 'Administração'),
    ('Maria Carolina Rosa Oliveira', 22, 'Pedagogia'),
    ('Pedro Gabriel Lima Barbosa', 28, 'Direito'),
    ('Ana Clara Silva Gomes', 26, 'Odontologia'),
    ('Carlos Roberto Pereira da Costa', 25, 'Ciências da Computação'),
    ('Luana Lima Simões', 18, 'Engenharia'),
    ('Sueli Sales Gomes de Oliveira Cardoso', 19, 'Pedagogia'),
    ('José Carlos Barbosa Rodrigues', 18, 'Direito'),
    ('Enzo Gabriel da Silva', 35, 'Engenharia'),
    ('Paola Ferreira dos Santos', 19, 'Engenharia')
]

comando_model = """
    INSERT INTO alunos
                (nome,
                 idade,
                 curso)
    VALUES      (?,
                 ?,
                 ?) 
"""

# Executar comandos
con.executar_comando_sequencia(conexao, comando_model, alunos)

# Salvar alterações no banco
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com banco
con.fechar_conexao_bd(conexao)
