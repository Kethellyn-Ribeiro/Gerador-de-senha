from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)


def gerar_senha(tamanho, maiusculas, minusculas, numeros, especiais):
    """Gera uma senha com base nas opções escolhidas pelo usuário."""

    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase  # Letras maiúsculas (A-Z)
    if minusculas:
        caracteres += string.ascii_lowercase  # Letras minúsculas (a-z)
    if numeros:
        caracteres += string.digits  # Números (0-9)
    if especiais:
        caracteres += string.punctuation  # Caracteres especiais (!@#$%...)

    if not caracteres:
        return "Erro: Escolha pelo menos um tipo de caractere."

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gerar_senha', methods=['POST'])
def gerar():
    dados = request.json
    tamanho = int(dados['tamanho'])
    maiusculas = dados['maiusculas']
    minusculas = dados['minusculas']
    numeros = dados['numeros']
    especiais = dados['especiais']

    senha = gerar_senha(tamanho, maiusculas, minusculas, numeros, especiais)
    return jsonify({'senha': senha})


if __name__ == '__main__':
    app.run(debug=True)
