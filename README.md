# RPG CREATOR

## What is it? 
TODO

## Run app
Go in `RPG_CREATOR`
### Backend
run `docker-compose up --build backend`
### Frontend
run `docker-compose up --build frontend`

Supprime image Docker existant
`docker-compose down --rmi all`
Nettoie les caches des build Docker
`docker builder prune --all`
Supprime les volumes Docker
`docker-compose down -v`

```
docker builder prune --all
docker-compose build --no-cache
```

Si `RUN npm run build` ne fonctionne pas
```
rm -rf node_modules package-lock.json
npm cache clean --force
npm install --legacy-peer-deps
npm run build
```