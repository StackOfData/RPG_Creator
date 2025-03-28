"""
routes.py
Contain HTTP link to the app. For exemple diplay online player
"""

from flask import jsonify

def init_routes(app):
    @app.route('/players', methods=['GET'])
    def get_players():
        # Logique pour récupérer les joueurs
        return jsonify({"players": ["Player1", "Player2"]})
