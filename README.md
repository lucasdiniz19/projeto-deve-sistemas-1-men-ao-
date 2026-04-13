# Sistema de Controle Financeiro Pessoal 

Este projeto é uma API Backend desenvolvida para a 1ª Menção da disciplina de Desenvolvimento de Sistemas. O objetivo é permitir que usuários gerenciem suas finanças através do controle de receitas, despesas e categorias.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.10
- **Framework:** Flask
- **Banco de Dados:** SQLite (Relacional)
- **ORM/Migrations:** Flask-SQLAlchemy e Flask-Migrate

##  Estrutura do Banco de Dados
O banco de dados é composto por 4 tabelas principais:
1. **User:** Armazena dados dos usuários (ID, Nome, Email).
2. **Category:** Categorias para classificação (Ex: Moradia, Lazer).
3. **Transaction:** Registros financeiros vinculados a um usuário e uma categoria.
4. **AuditLog:** Tabela de histórico que registra ações relevantes no sistema.

## 🛠️ Regras de Negócio Implementadas
Conforme os requisitos do projeto:
- **Consistência de Valor:** Todo lançamento financeiro deve possuir obrigatoriamente um valor positivo.
- **Vínculo Obrigatório:** Nenhuma transação pode existir sem estar associada a uma categoria válida.
- **Classificação Semântica:** Cada lançamento é categorizado estritamente como "Entrada" ou "Saída".
- **Integridade:** Operações de deleção e atualização são registradas para fins de auditoria.

##  Rotas da API
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| **GET** | `/users` | Lista todos os usuários |
| **POST** | `/users` | Cadastra um novo usuário |
| **POST** | `/transactions` | Cria um novo lançamento financeiro |
| **GET** | `/transactions/<id>` | Visualiza detalhes de um lançamento |
| **PUT** | `/transactions/<id>` | Atualiza um lançamento existente |
| **DELETE** | `/transactions/<id>` | Remove um lançamento do sistema |

## Como Executar o Projeto
---------------------------------------------------------------------------------------------------------------------------
1. **Clonar o repositório:**

   git clone [https://github.com/lucasdiniz19/projeto-deve-sistemas-1-men-ao-](https://github.com/lucasdiniz19/projeto-deve-sistemas-1-men-ao-)
   cd projeto-deve-sistemas-1-men-ao-
   ---------------------------------------------------------------------------------------------------------------------------
Configurar o ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
---------------------------------------------------------------------------------------------------------------------------
Instalar dependências:
pip install -r requirements.txt
---------------------------------------------------------------------------------------------------------------------------
Executar Migrations:
flask db upgrade
---------------------------------------------------------------------------------------------------------------------------
Iniciar o servidor:
flask run
--------------------------------------------------------------------------------------------------------------------------
  
    
    
