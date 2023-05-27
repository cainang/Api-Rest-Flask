from app import db
from flask import jsonify, make_response

class Aluno(db.Model):
    # Configuração do nome e colunas da tabela
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

    # Retorna um json do model
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
    
    # Função para adicionar aluno no banco
    def salvar_aluno(self):
        try:
            db.session.add(self)
            # Salva as alterações no banco
            db.session.commit()
        except Exception as e:
            print(e)

    # Função para alterar aluno no banco
    def modificar_aluno(self, cpf, nome, data_nascimento, sexo, idade, AV1, AV2, media):
        try:
            # Busca o aluno pelo cpf, se ele existir atualiza e retorna TRUE, senão ele retorna FALSE
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
                # Salva as alterações no banco
                db.session.commit() 
                return True
            else:
                return False
        except Exception as e:
            print(e)
    
    # Função para deletar aluno no banco
    def deletar_aluno(self, cpf):
        try:
            # Busca o aluno pelo cpf, se ele existir deleta e retorna TRUE, senão ele retorna FALSE
            alunoSelecionado = [alunos.json() for alunos in db.session.query(Aluno).filter(Aluno.cpf==cpf).all()]
            if(len(alunoSelecionado) == 1):
                db.session.query(Aluno).filter(Aluno.cpf==cpf).delete()
                # Salva as alterações no banco
                db.session.commit() 
                return True
            else:
                return False
        except Exception as e:
            print(e)