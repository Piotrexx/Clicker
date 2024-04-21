'use client'

import goomba_img from "@/public/img/mario/goomba.gif";
import { useState, useEffect } from 'react';
import Image from "next/image";

interface GoombaProps {
  fallen: boolean
  setCount: React.Dispatch<React.SetStateAction<number>>
}

const Goomba: React.FC<GoombaProps> = ({ fallen, setCount }) => {
  const [position, setPosition] = useState(1000)
  const [walking, setWalking] = useState(false)
  const [walkingPosition, setWalkingPosition] = useState(Math.floor(Math.random() * 800) + 1)
  const [direction, setDirection] = useState<'left' | 'right'>('right')

  useEffect(() => {
    if (fallen) {
      const fallInterval = setInterval(() => {
        setPosition(prevPosition => {
          if (prevPosition <= 25) {
            clearInterval(fallInterval)
            setWalking(true)
            return prevPosition
          } else {
            return prevPosition - 10
          }
        })
      }, 10)

      const pointsInterval = setInterval(() => {
        setCount(prevCount => prevCount + 5)
      }, 1000)

      return () => {
        clearInterval(fallInterval);
        clearInterval(pointsInterval);
      };
    }
  }, [fallen, setCount]);

  useEffect(() => {
    if (walking) {
      const walkInterval = setInterval(() => {
        setWalkingPosition(prevPosition => {
          if (prevPosition >= 800) {
            setDirection('left')
          } else if (prevPosition <= 0) {
            setDirection('right')
          }

          if (direction === 'right') {
            return prevPosition + 1
          } else {
            return prevPosition - 1
          }
        });
      }, 10)

      return () => clearInterval(walkInterval);
    }
  }, [walking, direction]);

  return (
    <div style={{ position: 'absolute', bottom: `${position}px`, left: `${walkingPosition}px` }}>
      <Image src={goomba_img} width={100} height={100} alt='goomba_img' />
    </div>
  );
}

export default Goomba;