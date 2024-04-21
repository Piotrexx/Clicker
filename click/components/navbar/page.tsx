import React from 'react'

function NavBar() {
    return (

<div className="fixed top-0 bg-white w-full z-10 h-[100px]">
          <nav className="flex items-center justify-between px-[4vw] py-4">
            {/* THIS IS NAVBAR */}
            <div>
        <button>
          BUY GOOMBA
        </button>
        <button>
          UPGRADE HAT
        </button>
        <button>
          BUT TURTLE
        </button>
      </div>
          </nav>
          
        </div>
      );
}

export default NavBar