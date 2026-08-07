semana 09: adiciona documentação inicial

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo ao site de pontos turísticos de Brasília!"

if __name__ == "__main__":
    app.run(debug=True)
