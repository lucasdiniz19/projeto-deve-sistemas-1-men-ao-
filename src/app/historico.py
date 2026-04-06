from database import db
from datetime import datetime

class Historico(db.Model):
    __tablename__ = 'historicos'
    id = db.Column(db.Integer, primary_key=True)
    acao = db.Column(db.String(255), nullable=False) # Ex: "Usuário X criou lançamento Y"
    data_acao = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    