'use client'

import { useState } from 'react';
import Clicker from "@/components/clicker/page";
import Goomba from "@/components/goomba/page";

interface GoombaState {
  id: number
  fallen: boolean
}

export default function Home() {
  const [count, setCount] = useState(0)
  const [goombas, setGoombas] = useState<GoombaState[]>([])

  const handleBuyGoomba = () => {
    if (count >= (100 + (100 * goombas.length))) {
      setCount(count - (100 + (100 * goombas.length)))
      setGoombas([...goombas, { id: Date.now(), fallen: true }])
    } else {
      alert("Nie masz na tyle monet by wynająć kolejnego grzyba panie!")
    }
  };

  return (
    <div className="bg-background bg-cover">
      <nav className="flex items-center justify-between px-[4vw] py-4">
        <button onClick={handleBuyGoomba}>
          BUY GOOMBA: {(100 + (100 * goombas.length))}
        </button>
      </nav>
      <Clicker count={count} setCount={setCount} />
      {goombas.map(goomba => (
        <Goomba key={goomba.id} fallen={goomba.fallen} setCount={setCount} />
      ))}
    </div>
  );
}