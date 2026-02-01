# E-commerce FAQ Chatbot - API FastAPI

Une API FastAPI pour un chatbot FAQ e-commerce utilisant ChromaDB pour la recherche sémantique et llama-cpp-python pour la génération de réponses basée sur un modèle local.

## 📋 Architecture du Projet

```
integrator project/
├── main.py                                  # Application FastAPI principale
├── app.py                                   # Script d'initialisation des données
├── requirements.txt                         # Dépendances Python
├── Dockerfile                               # Configuration Docker
├── docker-compose.yml                       # Orchestration des services
├── Ecommerce_FAQ_Chatbot_dataset.json      # Dataset FAQ
├── dolphin-2.6-mistral-7b.Q2_K.gguf        # Modèle GGUF local
└── utils/
    ├── load_data.py                        # Charge les FAQs depuis JSON
    ├── init_chroma.py                      # Initialise ChromaDB
    ├── add_to_chroma.py                    # Ajoute documents à ChromaDB
    ├── search.py                           # Recherche sémantique
    └── generate.py                         # Génération de réponses
```

### 🏗️ Composants Principaux

- **FastAPI** : Framework web pour créer l'API REST
- **ChromaDB** : Base de données vectorielle pour la recherche sémantique
- **llama-cpp-python** : Exécution du modèle LLM local (Dolphin Mistral)
- **Pydantic** : Validation des données

## 🚀 Installation

### Option 1 : Installation Locale (Recommandée)

**Prérequis :**
- Python 3.13+
- pip

**Étapes :**

```bash
# 1. Clonez ou ouvrez le répertoire du projet
cd /Users/macbookair/Desktop/integrator\ project

# 2. Créez un environnement virtuel (si nécessaire)
python3 -m venv .venv

# 3. Activez l'environnement virtuel
source .venv/bin/activate

# 4. Installez les dépendances
pip install -r requirements.txt

# 5. (Optionnel) Si vous avez llama-cpp-python
# pip install llama-cpp-python
```

### Option 2 : Installation avec Docker

**Prérequis :**
- Docker Desktop installé et en cours d'exécution

**Étapes :**

```bash
# 1. Naviguez vers le répertoire du projet
cd /Users/macbookair/Desktop/integrator\ project

# 2. Construisez les images (première fois, ~15-20 minutes)
docker-compose build

# 3. Lancez les services
docker-compose up -d

# 4. Vérifiez que tout fonctionne
docker-compose ps
```

## 🏃 Exécution du Projet

### Option 1 : Exécution Locale

**Démarrer l'API :**

```bash
# Activez l'environnement virtuel
source .venv/bin/activate

# Lancez l'API FastAPI
uvicorn main:app --port 8000 --reload
```

L'API sera disponible sur : **http://127.0.0.1:8000**

**Documentation interactive (Swagger UI) :**
- http://127.0.0.1:8000/docs

### Option 2 : Exécution avec Docker

```bash
# Lancer les services en arrière-plan
docker-compose up -d

# Vérifier les logs
docker-compose logs -f fastapi

# Arrêter les services
docker-compose down
```

L'API sera disponible sur : **http://localhost:8000**

## 📡 Endpoints API

### 1. Health Check
```
GET /
```
Retourne la version et l'URL Swagger.

**Réponse :**
```json
{
  "version": "1.0.0",
  "swagger": "/docs"
}
```

### 2. Rechercher des Documents
```
POST /search
```
Recherche les documents FAQ pertinents pour une requête.

**Requête :**
```json
{
  "query": " What payment methods do you accept?"
}
```

**Réponse :**
```json
{
  "query": "What payment methods do you accept?",
  "top_documents": [...]
}
```

### 3. Générer une Réponse
```
POST /generate
```
Génère une réponse basée sur la recherche sémantique et le modèle LLM.

**Requête :**
```json
{
  "query": "What payment methods do you accept?"
}
```

**Réponse :**
```json
{
  "query": "What payment methods do you accept?",
  "answer": "Pour créer un compte, veuillez...",
  "source_documents": [...]
}
```

## 🔧 Configuration

### Variables d'Environnement (Docker)

Dans `docker-compose.yml` :
```yaml
environment:
  - CHROMA_PERSISTENCE_DIR=/app/chroma_data
```

### Paramètres de Recherche

Modifiez le nombre de documents retournés dans [main.py](main.py#L32):
```python
documents = search_documents(collection, request.query, k=5)  # k = nombre de résultats
```

## 📦 Dépendances

Voir [requirements.txt](requirements.txt) pour la liste complète.

**Principales :**
- fastapi==0.104.1
- uvicorn==0.24.0
- chromadb==0.4.17
- pydantic==2.5.0
- llama-cpp-python==0.2.36 (optionnel, pour la génération)




## 📝 Initialisation des Données

Pour charger les données FAQ dans ChromaDB :

```bash
# Activez l'environnement virtuel
source .venv/bin/activate

# Exécutez le script d'initialisation
python3 app.py
```

Cela va :
1. Charger les FAQs depuis `Ecommerce_FAQ_Chatbot_dataset.json`
2. Créer une collection ChromaDB
3. Ajouter les documents à la base vectorielle

## 🎯 Cas d'Usage

1. **Chatbot FAQ** : Répondre automatiquement aux questions clients
2. **Recherche** : Trouver les articles pertinents de la FAQ
3. **Support Client** : Intégrer l'API dans un système de support

## 📄 Licence

À compléter selon vos besoins.

## 👥 Auteur

Créé le : Février 2026

---

**Questions ?** Consultez la documentation FastAPI : https://fastapi.tiangolo.com/
