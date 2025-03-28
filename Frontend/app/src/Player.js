import React, { useState } from 'react';

function Player() {
  // Définir l'état initial pour les statistiques
  const [stats, setStats] = useState({
    life: 100,
    magic: 50,
    speed: 30,
    strength: 70,
  });

  return (
    <div className="player-stats">
      <h2>Player Stats</h2>
      <div className="stat">
        <strong>Life:</strong> {stats.life}
      </div>
      <div className="stat">
        <strong>Magic:</strong> {stats.magic}
      </div>
      <div className="stat">
        <strong>Speed:</strong> {stats.speed}
      </div>
      <div className="stat">
        <strong>Strength:</strong> {stats.strength}
      </div>
    </div>
  );
}

export default Player;
