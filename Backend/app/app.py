"""
app.py
Init Flask server and define links
"""

# =================== IMPORT =====================

import signal
import sys
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# ================= INIT DATABASE ===============
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'  # Assure-toi que le chemin de la base de données est correct
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ================= PLAYER DATABASE ===============

# Modèle de la base de données
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    life = db.Column(db.Integer, nullable=False)
    magic = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Player {self.name}>'

# Route pour obtenir les données du joueur
@app.route('/api/player', methods=['GET'])
def get_player():
    player = Player.query.first()  # On récupère le premier joueur, tu peux adapter pour en récupérer plusieurs
    if player:
        return jsonify({
            'name': player.name,
            'life': player.life,
            'magic': player.magic,
            'speed': player.speed,
            'strength': player.strength
        })
    return jsonify({'message': 'Player not found'}), 404

# Route pour ajouter un joueur (à utiliser une seule fois pour initialiser les données)
@app.route('/api/player', methods=['POST'])
def add_player():
    data = request.get_json()
    new_player = Player(
        name=data['name'],
        life=data['life'],
        magic=data['magic'],
        speed=data['speed'],
        strength=data['strength']
    )
    db.session.add(new_player)
    db.session.commit()
    return jsonify({'message': 'Player added'}), 201

# Créer la base de données
with app.app_context():
    db.create_all()

# =============== SIGNAL HANDLER ====================

@app.route('/')
def home():
    return jsonify({"message": "Serveur Flask fonctionne !"})

# Fonction pour gérer les signaux d'arrêt (SIGTERM)
def handle_exit(signum, frame):
    print("Arrêt du serveur Flask proprement...")
    sys.exit(0)

# Capturer SIGINT (Ctrl+C) et SIGTERM (docker stop)
# signal.signal(signal.SIGINT, handle_exit)
# signal.signal(signal.SIGTERM, handle_exit)

# ============================ MAIN =============================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
