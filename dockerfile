# Etapa 1: Builder
FROM python:3.12.3-slim AS builder

WORKDIR /app

# Instala pacotes de sistema necessários
RUN apt-get update && apt-get install -y build-essential libpq-dev curl

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock README.md ./ 

# Instalar o Poetry
RUN pip install poetry==1.4.2

# Copiar arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock ./

# Configurar o Poetry para não criar ambientes virtuais e instalar dependências
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copiar o restante do código da aplicação
COPY . .

# Instalar dependências da aplicação
RUN poetry install --no-interaction --no-ansi

# Copia o projeto e as dependências da primeira etapa
#COPY --from=builder /app /app

# Define a variável de ambiente para o Python do venv
#ENV PATH="/app/.venv/bin:$PATH"

# Copia o código restante
#COPY . /app

# Comando para rodar o servidor FastAPI com Uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8007"]
