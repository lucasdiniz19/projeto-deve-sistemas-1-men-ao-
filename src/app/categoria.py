from database import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    # Aqui a gente cria o relacionamento 1:N [cite: 40]
    # Uma categoria pode ter vários lançamentos
    lancamentos = db.relationship('Lancamento', backref='categoria', lazy=True)
    