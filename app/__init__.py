from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import sqlite3

# Configuração do Flask e do Banco de Dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

from app.models.aluno import Aluno
with app.app_context():
    db.create_all()

# Configuração das rotas da api
from app.controllers.aluno_controller import Index, AlunoCreate, AlunoSearch, AlunoUpdate, AlunoDelete
api.add_resource(Index, '/')
api.add_resource(AlunoCreate, '/criar')
api.add_resource(AlunoSearch, '/todos')
api.add_resource(AlunoUpdate, '/atualizar')
api.add_resource(AlunoDelete, '/deletar')