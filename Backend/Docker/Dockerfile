FROM python:3.10

# Définir le dossier de travail
WORKDIR /app

# Copier uniquement les dépendances pour optimiser le cache Docker
COPY requirements.txt .

# Installer les dépendances
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du projet
COPY . .

# Ajouter un utilisateur non-root pour la sécurité
RUN useradd -m flaskuser

# Passer à cet utilisateur
USER flaskuser

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application Flask avec le serveur de développement intégré
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
