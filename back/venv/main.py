from flask import Flask, jsonify, request, render_template, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LUCASADASC'

usuarios = []

@app.route('/')
def home():
    flash(usuarios)
    return render_template('index.html', usuarios=usuarios)

# Excluir
@app.route('/excluirUsuario', methods=['POST'])
def excluirUsuario():
    usuario_nome = request.form.get('nomechave')
    for usuario in usuarios:
        if usuario_nome == usuario[0]:
            usuarios.remove(usuario)

    return redirect('/')

# Criar
@app.route('/adduser', methods=['POST'])
def incluir_novo_usuario():
    nome = request.form.get('nome')
    senha = request.form.get('email')

    userNovo = [nome, senha]
    usuarios.append(userNovo)
    return redirect('/')

app.run(debug=True)