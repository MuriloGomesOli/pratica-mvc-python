from flask import Flask, render_template, request, redirect, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(None, titulo, data_conclusao)
        tarefa.salvarTarefa()

    tarefas = Tarefa.listarTarefas()
    return render_template('index.html', tarefas=tarefas)

@app.route('/editar/<int:idTarefa>', methods=['POST'])
def editar(idTarefa):
    titulo = request.form['titulo']
    data_conclusao = request.form['data_conclusao']

    # Atualiza a tarefa no banco de dados
    Tarefa.editarTarefa(idTarefa, titulo, data_conclusao)
    return redirect('/')

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    Tarefa.apagarTarefa(idTarefa)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
