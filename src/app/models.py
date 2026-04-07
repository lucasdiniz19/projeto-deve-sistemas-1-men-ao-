from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    lancamentos = db.relationship('Lancamento', backref='usuario', lazy=True)
    historicos = db.relationship('Historico', backref='usuario', lazy=True)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False) [cite: 42]
    tipo_sugerido = db.Column(db.String(20))
    lancamentos = db.relationship('Lancamento', backref='categoria', lazy=True)

class Lancamento(db.Model):
    __tablename__ = 'lancamentos'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(100))
    tipo = db.Column(db.String(10), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Chaves Estrangeiras [cite: 41]
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

class Historico(db.Model):
    __tablename__ = 'historicos'
    id = db.Column(db.Integer, primary_key=True)
    acao = db.Column(db.String(255), nullable=False)
    data_acao = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)