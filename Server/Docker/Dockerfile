FROM python:3.10

# Mettre à jour et installer les dépendances de base
RUN apt-get update && apt-get install -y passwd

# Installer Gunicorn
RUN pip install gunicorn

# Ajouter un utilisateur non-root
RUN useradd -m flaskuser

# Passer à cet utilisateur pour exécuter le serveur
USER flaskuser

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers du projet
COPY requirements.txt .
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

