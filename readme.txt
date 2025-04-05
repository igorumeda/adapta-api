# Instalar fastApi e Uvicorn
pip install fastapi uvicorn[standard]

# Atualizar as dependências de requeriments.txt
pip freeze > requirements.txt

# Ativar Ambiente venv
venv\Scripts\activate

# Rodar a aplicação
uvicorn src.main:app --reload