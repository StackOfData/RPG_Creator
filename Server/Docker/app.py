import signal
import sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Serveur Flask fonctionne !"})

# Fonction pour gérer les signaux d'arrêt (SIGTERM)
def handle_exit(signum, frame):
    print("Arrêt du serveur Flask proprement...")
    sys.exit(0)

# Capturer SIGINT (Ctrl+C) et SIGTERM (docker stop)
signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)