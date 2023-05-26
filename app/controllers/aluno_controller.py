from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, reqparse
from app.models.aluno import Aluno

class Index(Resource):
    def get(self):
        return jsonify({"response": "Bem Vindo a API de Alunos"})

argumentos = reqparse.RequestParser()
argumentos.add_argument('cpf', type=int)
argumentos.add_argument('nome', type=str)
argumentos.add_argument('data_nascimento', type=str)
argumentos.add_argument('sexo', type=str)
argumentos.add_argument('idade', type=int)
argumentos.add_argument('AV1', type=float)
argumentos.add_argument('AV2', type=float)
argumentos.add_argument('media', type=float)

#para atualizar
argumentos_modificar = reqparse.RequestParser()
argumentos_modificar.add_argument('cpf', type=int)
argumentos_modificar.add_argument('nome', type=str)
argumentos_modificar.add_argument('data_nascimento', type=str)
argumentos_modificar.add_argument('sexo', type=str)
argumentos_modificar.add_argument('idade', type=int)
argumentos_modificar.add_argument('AV1', type=float)
argumentos_modificar.add_argument('AV2', type=float)
argumentos_modificar.add_argument('media', type=float)

argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument('cpf', type=int)

class AlunoCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            user = Aluno(**datas)
            user.salvar_aluno()

            return {"message": "Aluno adicionado com sucesso!"}

        except Exception as e:
            return jsonify({'status': 500, 'msg': 'f{e}'}), 500

class AlunoSearch(Resource):
    def get(self):
        try:
            return {"alunos": [alunos.json() for alunos in Aluno.query.all()]}

        except Exception as e:
            return jsonify({'status': 500, 'msg': 'f{e}'}), 500

class AlunoUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_modificar.parse_args()
            atualizar = Aluno.modificar_aluno(self, datas['cpf'], 
                                                   datas['nome'],
                                                   datas['data_nascimento'],
                                                   datas['sexo'], 
                                                   datas['idade'],
                                                   datas['AV1'],
                                                   datas['AV2'],
                                                   datas['media'])
            if(atualizar):
                return {"message": 'Aluno atualizado com sucesso!'}, 200    
            else:
                return {"message": 'Aluno não encontrado!'}, 404
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class AlunoDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            atualizar = Aluno.deletar_aluno(self, datas['cpf'])
            return {"message": 'Aluno deletado com sucesso!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500