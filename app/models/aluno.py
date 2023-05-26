from app import db
from flask import jsonify, make_response

class Aluno(db.Model):
    __tablename__ = 'aluno'
    cpf = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    data_nascimento = db.Column(db.String(255))
    sexo = db.Column(db.String(255))
    idade = db.Column(db.Integer)
    AV1 = db.Column(db.Float)
    AV2 = db.Column(db.Float)
    media = db.Column(db.Float)

    def __init__(self, cpf, nome, data_nascimento, sexo, idade, AV1, AV2, media):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.idade = idade
        self.AV1 = AV1
        self.AV2 = AV2
        self.media = media

    def json(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento,
            'sexo': self.sexo,
            'idade': self.idade,
            'AV1': self.AV1,
            'AV2': self.AV2,
            'media': self.media
        }
    
    def salvar_aluno(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
    
    def modificar_aluno(self, cpf, nome, data_nascimento, sexo, idade, AV1, AV2, media):
        try:
            alunoSelecionado = [alunos.json() for alunos in db.session.query(Aluno).filter(Aluno.cpf==cpf).all()]
            if(len(alunoSelecionado) == 1):
                db.session.query(Aluno).filter(Aluno.cpf==cpf).update({'cpf': cpf,
                    'nome': nome,
                    'data_nascimento': data_nascimento,
                    'sexo': sexo,
                    'idade': idade,
                    'AV1': AV1,
                    'AV2': AV2,
                    'media': media})
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
    
    def deletar_aluno(self, cpf):
        try:
            db.session.query(Aluno).filter(Aluno.cpf==cpf).delete()
            db.session.commit()
        except Exception as e:
            print(e)