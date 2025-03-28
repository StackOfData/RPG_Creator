# Webapp

## File 
### package.json
Contain configuration file for the React project dependencies like *react, react-dom, axios, etc*. Usually create with `npx create-react-app`.

## Run Webapp
* Install dependencies in `Webapp/`, `npm install`
* Run ract app `npm start`
### Communicate Flask - React
* `pip install flask-cors`
* Add CORS config in `app.py` file in directory `Server/app/`
```py
from flask import Flask
from flask_cors import CORS  # Import du module CORS

app = Flask(__name__)
CORS(app)  # Autorise les requêtes CORS

# Définition des routes...
```