import React, { useState, useEffect } from "react";
import { io } from "socket.io-client";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

const socket = io("http://192.168.2.1:5000"); // Remplace par l'IP du serveur

export default function App() {
  const [players, setPlayers] = useState({});
  const [isGameMaster, setIsGameMaster] = useState(false);

  useEffect(() => {
    socket.on("update", (data) => {
      setPlayers(data);
    });

    fetch("http://192.168.2.1:5000/players")
      .then((res) => res.json())
      .then(setPlayers);

    return () => socket.off("update");
  }, []);

  return (
    <div className="p-4 space-y-4">
      <h1 className="text-xl font-bold">JDR Game</h1>
      <Button onClick={() => setIsGameMaster(!isGameMaster)}>
        {isGameMaster ? "Passer en mode Joueur" : "Passer en mode MJ"}
      </Button>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {Object.entries(players).map(([id, player]) => (
          <PlayerCard key={id} id={id} player={player} isGameMaster={isGameMaster} />
        ))}
      </div>
    </div>
  );
}

function PlayerCard({ id, player, isGameMaster }) {
  const [hp, setHp] = useState(player.hp);
  const [mana, setMana] = useState(player.mana);

  const updateStats = () => {
    socket.emit("update", { id, stats: { hp, mana } });
  };

  return (
    <Card className="p-4">
      <CardContent>
        <h2 className="text-lg font-semibold">{player.name}</h2>
        <p>HP: {isGameMaster ? <Input value={hp} onChange={(e) => setHp(e.target.value)} /> : hp}</p>
        <p>Mana: {isGameMaster ? <Input value={mana} onChange={(e) => setMana(e.target.value)} /> : mana}</p>
        {isGameMaster && <Button onClick={updateStats}>Mettre à jour</Button>}
      </CardContent>
    </Card>
  );
}
