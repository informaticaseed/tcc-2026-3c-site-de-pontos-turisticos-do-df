import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pontos_turisticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            categoria TEXT NOT NULL,
            endereco TEXT,
            horario TEXT,
            imagem TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            tipo_comida TEXT,
            endereco TEXT,
            horario TEXT,
            imagem TEXT
        )
    """)


    conexao.commit()
    conexao.close()
def inserir_ponto_turistico(nome, descricao, categoria, endereco, horario, imagem):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
            "SELECT id FROM pontos_turisticos WHERE nome = ?",
            (nome,)
    )

    existe = cursor.fetchone()

    if existe is None:
        cursor.execute("""
            INSERT INTO pontos_turisticos
            (nome, descricao, categoria, endereco, horario, imagem)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, descricao, categoria, endereco, horario, imagem))

        conexao.commit()
    conexao.close()
def inserir_restaurante(nome, descricao, tipo_comida, endereco, horario, imagem):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
            "SELECT id FROM restaurantes WHERE nome = ?",
            (nome,)
    )

    existe = cursor.fetchone()

    if existe is None:
        cursor.execute("""
            INSERT INTO restaurantes
            (nome, descricao, tipo_comida, endereco, horario, imagem)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, descricao, tipo_comida, endereco, horario, imagem))

        conexao.commit()

    conexao.close()
def atualizar_ponto_turistico(nome, endereco, horario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pontos_turisticos
        SET endereco = ?, horario = ?
        WHERE nome = ?
    """, (endereco, horario, nome))

    conexao.commit()
    conexao.close()


def atualizar_restaurante(nome, endereco, horario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE restaurantes
        SET endereco = ?, horario = ?
        WHERE nome = ?
    """, (endereco, horario, nome))

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_tabelas()

    inserir_ponto_turistico(
        "Memorial JK",
        "Espaço histórico dedicado a Juscelino Kubitschek e à história de Brasília.",
        "Histórico",
        "Eixo Monumental, Brasília - DF",
        "Consultar horário de funcionamento",
        "memorial-jk.jpeg"
    )
    inserir_ponto_turistico(
        "Palácio do Planalto",
        "Sede do Poder Executivo Federal e local de trabalho do Presidente da República.",
        "Histórico",
        "Praça dos Três Poderes, Brasília - DF",
        "Consultar horário de visitação",
        "palacio-planalto.jpeg"
    ) 
    inserir_ponto_turistico(
        "Itamaraty",
        "Sede do Ministério das Relações Exteriores, conhecida por sua arquitetura e importância política.",
        "Histórico",
        "Esplanada dos Ministérios, Brasília - DF",
        "Consultar horário de visitação",
        "itamaraty.jpeg"
    )
    inserir_ponto_turistico(
        "Congresso Nacional",
        "Sede do Poder Legislativo brasileiro e um dos principais símbolos arquitetônicos de Brasília.",
        "Histórico",
        "Praça dos Três Poderes, Brasília - DF",
        "Consultar horário de visitação",
        "congresso-nacional.jpeg"
    )
    inserir_ponto_turistico(
        "Catedral Metropolitana de Brasília",
        "Um dos principais símbolos arquitetônicos de Brasília, projetado por Oscar Niemeyer.",
        "Histórico",
        "Esplanada dos Ministérios, Brasília - DF",
        "Consultar horário de visitação",
        "catedral-brasilia.jpeg"
    )
    inserir_ponto_turistico(
        "SESI Lab",
        "Espaço cultural e interativo voltado à ciência, tecnologia, arte e inovação.",
        "Cultural",
        "Setor Cultural Sul, Brasília - DF",
        "Consultar horário de funcionamento",
        "sesi-lab.jpeg"
    )
    inserir_ponto_turistico(
        "Biblioteca Nacional de Brasília",
        "Espaço cultural destinado ao acesso à informação, leitura, pesquisa e atividades culturais.",
        "Cultural",
        "Setor Cultural Sul, Brasília - DF",
        "Consultar horário de funcionamento",
        "biblioteca-nacional.jpeg"
    )
    inserir_ponto_turistico(
        "Museu Nacional da República",
        "Espaço cultural de Brasília que recebe exposições e manifestações artísticas.",
        "Cultural",
        "Esplanada dos Ministérios, Brasília - DF",
        "Consultar horário de funcionamento",
        "museu-nacional.jpeg"
    )
    inserir_restaurante(
        "Pizzas Dom Bosco",
        "Tradicional pizzaria de Brasília, conhecida por servir pizzas em estilo simples e popular.",
        "Pizzaria",
        "Brasília - DF",
        "Consultar horário de funcionamento",
        "pizzas-dom-bosco.jpeg"
    )
    inserir_restaurante(
        "Pastel da Viçosa",
        "Tradicional estabelecimento de Brasília conhecido por pastéis e lanches rápidos.",
        "Pastelaria",
        "Brasília - DF",
        "Consultar horário de funcionamento",
        "pastel-vicosa.jpeg"
    )
    inserir_restaurante(
        "Rossoni",
        "Estabelecimento tradicional de Brasília conhecido por lanches e refeições.",
        "Lanchonete",
        "Brasília - DF",
        "Consultar horário de funcionamento",
        "rossoni.jpeg"
    )

    atualizar_ponto_turistico(
        "Memorial JK",
        "Eixo Monumental - Lado Oeste - Praça do Cruzeiro, Brasília - DF, 70070-300",
        "Terça a domingo, das 9h às 18h. Fechado às segundas."
    )

    atualizar_ponto_turistico(
        "Palácio do Planalto",
        "Praça dos Três Poderes, Brasília - DF, 70150-900",
        "Consultar horário de visitação pública antes da visita."
    )

    atualizar_ponto_turistico(
        "Itamaraty",
        "Esplanada dos Ministérios - Bloco H, Brasília - DF, 70170-900",
        "Consultar horário de visitação e agendamento."
    )

    atualizar_ponto_turistico(
        "Congresso Nacional",
        "Praça dos Três Poderes, Zona Cívico-Administrativa, Brasília - DF, 70165-900",
        "Visitação geralmente das 9h às 17h, conforme programação."
    )

    atualizar_ponto_turistico(
        "Catedral Metropolitana de Brasília",
        "Esplanada dos Ministérios, Brasília - DF, 70050-000",
        "Terça a sexta: 8h às 16h45. Sábado: 8h às 16h30. Domingo: 9h às 17h30."
    )

    atualizar_ponto_turistico(
        "SESI Lab",
        "Setor Cultural Sul, Bloco A, Asa Sul, Brasília - DF, 70070-150",
        "Terça a sexta: 9h às 18h. Sábado, domingo e feriados: 10h às 19h."
    )

    atualizar_ponto_turistico(
        "Biblioteca Nacional de Brasília",
        "Setor Cultural Sul - SCTS Lote 2, Brasília - DF",
        "Segunda a sexta: 9h às 19h. Sábado e domingo: 8h30 às 13h30."
    )

    atualizar_ponto_turistico(
        "Museu Nacional da República",
        "Setor Cultural Sul, Lote 2, próximo à Rodoviária do Plano Piloto, Brasília - DF",
        "Terça a domingo, das 9h às 18h30."
    )

    atualizar_restaurante(
        "Pizzas Dom Bosco",
        "CLS 107, Bloco D, Loja 20, Asa Sul, Brasília - DF, 70346-540",
        "Todos os dias, das 8h às 23h."
    )

    atualizar_restaurante(
        "Pastel da Viçosa",
        "SCRN 704/705, Bloco D, Asa Norte, Brasília - DF, 70730-640",
        "Todos os dias, das 6h às 20h."
    )

    atualizar_restaurante(
        "Rossoni",
        "V. RE, 2, Quadra 1, Cruzeiro Velho, Cruzeiro Center, Brasília - DF, 70640-515",
        "Segunda: 11h às 21h30. Demais dias: consultar horário atualizado."
    )

    print("Dados atualizados com sucesso!")
   