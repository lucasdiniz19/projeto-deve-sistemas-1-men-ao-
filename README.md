Single-database configuration for Flask.

Sistema Financeiro Simplificado

Uma API robusta desenvolvida em Python com o framework Flask para o gerenciamento de finanças pessoais. O projeto permite registrar entradas e saídas, categorizar transações e manter um histórico de ações do usuário, utilizando MySQL para persistência de dados.

# Tecnologias Utilizadas

- Linguagem: Python 3.x
- Framework Web: Flask
- ORM: Flask-SQLAlchemy (SQLAlchemy)
- Migrações: Flask-Migrate (Alembic)
- Banco de Dados: MySQL
- Ambiente: Python-dotenv para variáveis de ambiente

# Pré-requisitos

- Antes de começar, você precisará ter instalado em sua máquina:

Python 3.8+

Servidor MySQL (ou Docker rodando uma imagem MySQL)

Pip (Gerenciador de pacotes do Python)

# Configuração e Instalação

# Clone o repositório:

Bash -

git clone https://github.com/seu-usuario/projeto-deve-sistemas-1-men-ao-.git

cd projeto-deve-sistemas-1-men-ao-.git


# Crie e ative um ambiente virtual:

Bash -

python -m venv venv

* * Windows:
.\venv\Scripts\activate

* * Linux/Mac:
source venv/bin/activate


# Instale as dependências:

- Bashpip install -r requirements.txt


# Configure as Variáveis de Ambiente:

- Crie um arquivo .env na raiz do projeto e adicione suas credenciais:

Snippet de código -

SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:sua_senha@localhost:3306/financeiro_db
DATABASE_URL=mysql+pymysql://root:sua_senha@localhost:3306/financeiro_db
SECRET_KEY=sua_chave_secreta


# Prepare o Banco de Dados:

- Certifique-se de que o banco financeiro_db existe no MySQL. Você pode testar a conexão com:Bashpython teste_conexao.py


# Execute as Migrações:

- Bashflask db upgrade


# Executando a API

- Para iniciar o servidor de desenvolvimento, execute:Bashpython run.py
O servidor estará disponível em http://127.0.0.1:5000.


# Rotas da API (Endpoints)

- A API gerencia os recursos através do endpoint principal /lancamentos. Para listar todos os registros, utiliza-se o método GET. Novos lançamentos de entrada ou saída são realizados via POST, enviando os dados do usuário, categoria e valor no corpo da requisição. Caso precise modificar o valor ou a descrição de um registro existente, deve-se utilizar o método PUT acompanhado do ID do lançamento específico. Por fim, a remoção definitiva de um registro é feita através do método DELETE, também referenciando o ID desejado na URL


# Exemplo de JSON para Criação (POST):

- JSON
{
  "valor": 150.50,
  "tipo": "saida",
  "categoria_id": 1,
  "usuario_id": 1,
  "descricao": "Assinatura Streaming"
}


# Estrutura do Projeto

- src/app/__init__.py: Factory da aplicação Flask.
- models.py: Definição das tabelas User, Categoria, Lancamento e Historico.
- routes.py: Lógica dos endpoints e regras de negócio
- extensions.py: Instanciação do SQLAlchemy e Migrate.
- env.py: Script de configuração de ambiente para o Alembic.
- run.py: Ponto de entrada para execução do projeto.


# Regras de Negócio Implementadas

- Validação de Valor: Lançamentos devem possuir valor obrigatoriamente positivo.
- Categorização: Todo lançamento deve estar associado a uma categoria válida.
- Classificação Estrita: Apenas os tipos entrada ou saida são aceitos.
- Auditoria: Cada criação de lançamento gera automaticamente um registro na tabela de Historico.Este projeto foi desenvolvido para fins acadêmicos/práticos de Desenvolvimento de Sistemas
