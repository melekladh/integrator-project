# Utiliser une image Python officielle
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer dépendances système nécessaires pour construire des dépendances Python natives
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	   build-essential \
	   cmake \
	   git \
	   wget \
	   curl \
	   pkg-config \
	   libopenblas-dev \
	   liblapack-dev \
	   libomp-dev \
	   libsqlite3-dev \
	   libffi-dev \
	   libssl-dev \
	   ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

# Copier les fichiers de dépendances
COPY requirements.txt .

# Upgrader pip/setuptools/wheel et installer les dépendances Python
RUN python -m pip install --upgrade pip setuptools wheel cmake \
	&& pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port de l'API
EXPOSE 8001

# Commande pour lancer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
