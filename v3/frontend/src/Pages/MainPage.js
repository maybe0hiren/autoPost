import React from "react";
import { useEffect, useState } from "react";

import './MainPage.css';
import Card from "../Components/Card";

function MainPage(){
    // const dummyServerStatur = {
    //     status: "Server Running"
    // }
    const api = "DUMMY";
    const [task, setTask] = useState("");
    const [key, setKey] = useState("");
    const [statusColour, setStatusColour] = useState("red");
    const [serverStatus, setServerStatus] = useState("");
    const [serverMessage, setServerMessage] = useState("");
    useEffect(() => {
        getServerStatus();
    }, []);

    async function getServerStatus(){
        try{
            const res = await fetch(`${api}/status`);
            const data = await res.json();
            setServerStatus(data.status);
            setStatusColour("green");
        } catch(err) {
            setServerStatus("Server Offline");
        }
    }

    async function sendTask(){
        try{
            const res = await fetch(`${api}/task`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    task: task,
                    key: key
                })
            });
            const data = await res.json();
            setServerMessage(data.message);
            setTask("");
            setKey("");
        } catch(err) {
            console.error("Failed to send task");
        }
    }


    return(
        <>
        <div className="inputBox">
            <Card width="700px" height="350px">
                <h1>AutoPost</h1>
                <br />
                <input className="inputBar" type="text" placeholder="Task" value={ task } onChange={(e) => setTask(e.target.value)}/>
                <br />
                <input className="inputBar" type="password" placeholder="Key" value={ key } onChange={(e) => setKey(e.target.value)} />
                <button className="submit" type="submit" onClick={sendTask}>Submit</button>
                <br />
                {/* <p>Server Message: {dummyServerStatur.status}</p> */}
                <p style={{ color: statusColour }}>{serverStatus}</p>
                <p>{serverMessage}</p>
            </Card> 
        </div>
        </>
    )
}

export default MainPage;