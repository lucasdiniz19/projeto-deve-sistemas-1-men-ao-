from database import db
from datetime import datetime

class Lancamento(db.Model):
    __tablename__ = 'lancamentos'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False) # Regra: deve ser positivo 
    descricao = db.Column(db.String(100))
    tipo = db.Column(db.String(10), nullable=False) # 'entrada' ou 'saida' 
    data = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Chaves Estrangeiras (Relacionamentos) [cite: 41]
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    