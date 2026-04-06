
@app.route('/lancamento', methods=['POST'])
def criar_lancamento():
    dados = request.json
    valor = dados.get('valor')
    tipo = dados.get('tipo') # 'entrada' ou 'saida'
    categoria_id = dados.get('categoria_id')

  
    if not valor or valor <= 0:
        return {"erro": "O valor deve ser positivo!"}, 400

 
    if not categoria_id:
        return {"erro": "Categoria é obrigatória!"}, 400

    # [cite: 24]
    if tipo not in ['entrada', 'saida']:
        return {"erro": "Tipo inválido! Use 'entrada' ou 'saida'."}, 400

    novo_lancamento = Lancamento(
        valor=valor,
        descricao=dados.get('descricao'),
        tipo=tipo,
        categoria_id=categoria_id,
        usuario_id=dados.get('usuario_id')
    )
    
    db.session.add(novo_lancamento)
    
    #[cite: 39, 47]
    log = Historico(acao=f"Lancamento de R$ {valor} criado.", usuario_id=dados.get('usuario_id'))
    db.session.add(log)
    
    db.session.commit()
    return {"msg": "Lançamento criado com sucesso!"}, 201