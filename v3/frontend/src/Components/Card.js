import React from "react";

import './Card.css';


function Card({ width, height, children}){
    return(
        <>
        <div className="glass-card" style={{width: width, height: height}}>
            {children}
        </div>
        </>
    )
}
export default Card;