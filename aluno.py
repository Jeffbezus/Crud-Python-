from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    __tablename__ = 'Alunos'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11))
    nome = db.Column(db.String(60))
    sexo = db.Column(db.String(10))
    idade = db.Column(db.Integer)
    nascimento = db.Column(db.String(10))
    av1 = db.Column(db.Float)
    av2 = db.Column(db.Float)
    media = db.Column(db.Float)

    def __init__(self, cpf, nome, sexo, idade, nascimento, av1, av2, media):
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.nascimento = nascimento
        self.av1 = av1
        self.av2 = av2
        self.media = media
        
    def json(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'nome': self.nome,
            'sexo': self.sexo,
            'idade': self.idade,
            'nascimento': self.nascimento,
            'av1': self.av1,
            'av2': self.av2,
            'media': self.media
        }
 