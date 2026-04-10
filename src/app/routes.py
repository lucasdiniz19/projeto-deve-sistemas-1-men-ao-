from flask import Blueprint, request, jsonify
from .extensions import db
from .models import User, Categoria, Lancamento, Historico


bp = Blueprint('main', __name__)

@bp.route('/lancamentos', methods=['POST'])
def criar_lancamento():

    dados = request.json
    valor = dados.get('valor')
    tipo = dados.get('tipo')
    cat_id = dados.get('categoria_id')
    user_id = dados.get('usuario_id')

    if not valor or valor <= 0:
        return jsonify({"erro": "O lançamento deve possuir valor positivo!"}), 400
    
    if not cat_id:
        return jsonify({"erro": "Todo lançamento deve ser associado a uma categoria!"}), 400

    if tipo not in ['entrada', 'saida']:
        return jsonify({"erro": "Classifique obrigatoriamente como 'entrada' ou 'saida'!"}), 400

    novo = Lancamento(
        valor=valor, 
        tipo=tipo, 
        categoria_id=cat_id, 
        usuario_id=user_id, 
        descricao=dados.get('descricao')
    )
    
    log = Historico(acao=f"Criou {tipo} de R$ {valor}", usuario_id=user_id)
    
    db.session.add(novo)
    db.session.add(log)
    db.session.commit()
    
    return jsonify({"msg": "Lançamento registrado com sucesso!"}), 201

@bp.route('/lancamentos', methods=['GET'])
def listar_lancamentos():
    lista = Lancamento.query.all()
    output = []
    for l in lista:
        output.append({
            "id": l.id,
            "valor": l.valor,
            "tipo": l.tipo,
            "categoria": l.categoria.nome,
            "data": l.data.strftime('%Y-%m-%d')
        })
    return jsonify(output), 200

@app.route('/lancamentos/<int:id>', methods=['PUT'])
def atualizar_lancamento(id):
    lancamento = Lancamento.query.get_or_404(id)
    dados = request.json
    
    if 'valor' in dados and dados['valor'] > 0:
        lancamento.valor = dados['valor']
    if 'descricao' in dados:
        lancamento.descricao = dados['descricao']
        
    db.session.commit()
    return jsonify({"msg": "Lançamento atualizado!"}), 200

@app.route('/lancamentos/<int:id>', methods=['DELETE'])
def deletar_lancamento(id):
    lancamento = Lancamento.query.get_or_404(id)
    db.session.delete(lancamento)
    db.session.commit()
    return jsonify({"msg": "Lançamento removido!"}), 200
