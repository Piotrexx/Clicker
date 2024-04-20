import React, { useEffect, useState } from 'react';
import Image from "next/image";
import mario_idle from "@/public/img/mario/mario_idle.png";
import mario_jump from "@/public/img/mario/mario_jump.png";
import luckyblock_gif from "@/public/img/mario/luckyblock_gif.gif"
import coin from "@/public/img/mario/coing.gif"
import goomba from "@/public/img/mario/goomba.gif"

const Clicker = () => {


  const [count, setCount] = useState(0);
  const [jumping, setJumping] = useState(false);

  const handleClick = () => {
    setJumping(true);
    setTimeout(() => {
      setJumping(false);
      setCount(count + 1);
      setTimeout(() => {
      }, 100)
    }, 100);
  };
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <div style={{position: 'absolute', bottom: '25px'}}>
      {/* {jumping? <Image src={coin} width={125} height={125} alt='coin' style={{animation: jumping ? 'slide-top 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both': ''}} />: ''} */}
      <Image src={luckyblock_gif} width={100} height={100} alt='luckyblock' style={{animation: jumping ? 'slide-top-block 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both': ''}} />
      <Image onClick={handleClick} src={jumping ? mario_jump : mario_idle} width={100} height={100} alt='mario' style={{animation: jumping ? 'slide-top-mario 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both': ''}} />
      <Image src={goomba} width={50} height={50} alt='goomba'/>
      </div>
      <p><Image src={coin} width={125} height={125} alt='coin'/> {count}</p>
    </div>
  );
};

export default Clicker;