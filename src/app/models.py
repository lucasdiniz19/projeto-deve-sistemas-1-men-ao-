from .extensions import db
from sqlalchemy.sql import func
from sqlalchemy import Enum, CheckConstraint

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, server_default=func.now())

    # Relacionamentos
    categorias = db.relationship("Categoria", back_populates="usuario", cascade="all, delete-orphan")
    lancamentos = db.relationship("Lancamento", back_populates="usuario", cascade="all, delete-orphan")
    historicos = db.relationship("HistoricoAtividade", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario {self.nome}>"

class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(150), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    # Relacionamentos
    usuario = db.relationship("Usuario", back_populates="categorias")
    lancamentos = db.relationship("Lancamento", back_populates="categoria")

    def __repr__(self):
        return f"<Categoria {self.nome}>"

class Lancamento(db.Model):
    __tablename__ = "lancamentos"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data_lancamento = db.Column(db.Date, nullable=False)
    tipo = db.Column(
        Enum("entrada", "saída", name="tipo_lancamento"), 
        nullable=False
    )
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)

    # Regra de negócio: Valor deve ser positivo
    __table_args__ = (
        CheckConstraint('valor > 0', name='chk_valor_positivo'),
    )

    # Relacionamentos
    usuario = db.relationship("Usuario", back_populates="lancamentos")
    categoria = db.relationship("Categoria", back_populates="lancamentos")

    def __repr__(self):
        return f"<Lancamento {self.descricao}: {self.valor}>"

class HistoricoAtividade(db.Model):
    __tablename__ = "historico_atividades"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    acao = db.Column(db.String(100), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False, server_default=func.now())

    # Relacionamentos
    usuario = db.relationship("Usuario", back_populates="historicos")

    def __repr__(self):
        return f"<Historico {self.acao} em {self.data_hora}>"