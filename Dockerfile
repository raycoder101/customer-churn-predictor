FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl build-essential gcc git

# Set Poetry version to match local
ENV POETRY_VERSION=2.1.3
ENV PATH="/root/.local/bin:$PATH"

# Install Poetry 2.1.3 explicitly
RUN curl -sSL https://install.python-poetry.org | python3 -

# Disable Poetry virtualenv creation
RUN poetry config virtualenvs.create false

WORKDIR /app

# Copy only pyproject.toml and poetry.lock for caching
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root

# Copy data folder *** Only for NONE Production deployments ***
COPY data/ ./data/

# Copy project files
COPY . .

# Set PYTHONPATH for src imports
ENV PYTHONPATH=/app/src

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
