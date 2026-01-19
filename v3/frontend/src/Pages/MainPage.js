import React from "react";
// import { useEffect, useState } from "react";

import './MainPage.css';
import Card from "../Components/Card";

function MainPage(){
    const dummyServerMessage = {
        message: "Server Running"
    }


    // const [serverMessage, setServerMessage] = useState("");
    // useEffect(() => {
    //     getServerMessage();
    // }, []);

    // async function getServerMessage(){
    //     try{
    //         const res = await fetch("");
    //         const data = await res.json();
    //         setServerMessage(data.message);
    //     } catch(err) {
    //         setServerMessage("Server Offline");
    //     }
    // }


    function buttonClicked(){
        console.log("Button Clicked");
    }


    return(
        <>
        <div className="inputBox">
            <Card width="700px" height="auto">
                <h1>AutoPost</h1>
                <br />
                <input className="inputBar" type="text" placeholder="Task" />
                <br />
                <input className="inputBar" type="password" placeholder="Key" />
                <button className="submit" type="submit" onClick={buttonClicked}>Submit</button>
                <br />
                <p>Server Message: {dummyServerMessage.message}</p>
                {/* <p>Server Message: {serverMessage}</p> */}
            </Card> 
        </div>
        </>
    )
}

export default MainPage;