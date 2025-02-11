from database import Database

class Tarefa:
    def __init__(self, titulo, data_conclusao, id):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
        

    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados"""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES(%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    def listarTarefas():
        """Retornar uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM  tarefa'
        tarefas = db.consultar
        db.desconectar()
        return tarefas if tarefas else []
    
    def apagarTarefa(self):
        """Apaga uma tarefa cadastrada no bcd."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (self.id,)
        db.executar(sql, params)
        db.desconectar()

tarefa = Tarefa(2, 'Teste de tarefa', None)
tarefa.apagarTarefa()