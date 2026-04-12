from flask import Blueprint, request, jsonify
from models import db, User, Category, Transaction, AuditLog

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"status": "API Financeira Ativa"}), 200


# ROTA lancamen tos
@main.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    
    if data.get('value', 0) <= 0:
        return jsonify({"error": "O valor deve ser positivo"}), 400
    
    if data.get('type') not in ['entrada', 'saída']:
        return jsonify({"error": "Tipo deve ser 'entrada' ou 'saída'"}), 400

    new_transaction = Transaction(
        description=data['description'],
        value=data['value'],
        type=data['type'],
        user_id=data['user_id'],
        category_id=data['category_id']
    )
    
    db.session.add(new_transaction)
    db.session.add(AuditLog(action=f"Transação criada: {data['description']}"))
    db.session.commit()
    
    return jsonify({"message": "Lançamento realizado com sucesso!"}), 201

# ROTA PARA LISTAR 
@main.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    output = []
    for t in transactions:
        output.append({
            "id": t.id,
            "descricao": t.description,
            "valor": t.value,
            "tipo": t.type,
            "usuario_id": t.user_id,
            "categoria_id": t.category_id
        })
    return jsonify(output), 200

#rota de saldo 
@main.route('/balance', methods=['GET'])
def get_balance():
    transactions = Transaction.query.all()
    total_input = sum(t.value for t in transactions if t.type == 'entrada')
    total_output = sum(t.value for t in transactions if t.type == 'saída')
    balance = total_input - total_output
    
    return jsonify({
        "total_entradas": total_input,
        "total_saidas": total_output,
        "saldo_atual": balance
    }), 200