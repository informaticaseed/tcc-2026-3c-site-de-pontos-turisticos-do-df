from flask import Flask, render_template, request
from repositorio import conectar

app = Flask(__name__)


@app.route("/")
def inicio():
    busca = request.args.get("busca", "")
    categoria = request.args.get("categoria", "")

    conexao = conectar()
    cursor = conexao.cursor()

    if busca and categoria:
        cursor.execute(
            "SELECT * FROM pontos_turisticos WHERE nome LIKE ? AND categoria = ?",
            ('%' + busca + '%', categoria)
    )

    elif busca:
        cursor.execute(
            "SELECT * FROM pontos_turisticos WHERE nome LIKE ?",
            ('%' + busca + '%',)
    )

    elif categoria:
        cursor.execute(
            "SELECT * FROM pontos_turisticos WHERE categoria = ?",
            (categoria,)
    )

    else:
        cursor.execute("SELECT * FROM pontos_turisticos")

    pontos_turisticos = cursor.fetchall()

    if busca:
       cursor.execute(
           "SELECT * FROM restaurantes WHERE nome LIKE ?",
           ('%' + busca + '%',)
    )
       restaurantes = cursor.fetchall()

    elif categoria == "Culinária":
        cursor.execute("SELECT * FROM restaurantes")
        restaurantes = cursor.fetchall()

    elif not categoria:
        cursor.execute("SELECT * FROM restaurantes")
        restaurantes = cursor.fetchall()

    else:
        restaurantes = []

    conexao.close()

    return render_template(
        "index.html",
        pontos_turisticos=pontos_turisticos,
        restaurantes=restaurantes
    )
@app.route("/detalhes/<int:id>")
def detalhes(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM pontos_turisticos WHERE id = ?",
        (id,)
    )

    ponto = cursor.fetchone()

    conexao.close()

    return render_template(
        "detalhes.html",
        ponto=ponto
    )
@app.route("/restaurante/<int:id>")
def detalhes_restaurante(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM restaurantes WHERE id = ?",
        (id,)
    )

    restaurante = cursor.fetchone()

    conexao.close()

    return render_template(
        "restaurante.html",
        restaurante=restaurante
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)