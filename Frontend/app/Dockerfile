# Utilise une image de Node.js comme base
FROM node:18-alpine

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers package.json et package-lock.json avant d’installer les dépendances
COPY package.json package-lock.json ./

# Installe les dépendances
RUN npm install

# Copie le reste des fichiers du projet
COPY . .

# Expose le port 3000
EXPOSE 3000

# Lance l’application React
CMD ["npm", "start"]
