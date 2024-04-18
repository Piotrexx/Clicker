import React, { useState } from 'react';
import Image from "next/image";
import mario_idle from "@/public/img/mario/mario_idle.png";
import mario_jump from "@/public/img/mario/mario_jump.png";

const Clicker = () => {
  const [count, setCount] = useState(0);
  const [jumping, setJumping] = useState(false);

  const handleClick = () => {
    setJumping(true);
    setTimeout(() => {
      setJumping(false);
      setCount(count + 1);
    }, 500);
  };

  return (
<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
    <div style={{ position: 'relative', top: jumping ? '-30px' : '0' }}>
      <Image onClick={handleClick} src={jumping ? mario_jump : mario_idle} width={100} height={100} alt='mario' />
    </div>
    <p>Count: {count}</p>
  </div>
);
};
export default Clicker;