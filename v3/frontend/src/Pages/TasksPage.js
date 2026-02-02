import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import "./MainPage.css";
import Card from "../Components/Card";
import TaskCard from "../Components/TaskCard";

function TaskPage() {
  const navigate = useNavigate();
  const api = "http://localhost:5000";

  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    function startUp() {
        getTasks();
    }
    startUp();
  }, [])

  function goBackToMain() {
    navigate("/");
  }

  async function getTasks() {
    try {
      const res = await fetch(`${api}/getTasks`);
      const data = await res.json();
      setTasks(data.tasks || []);
      console.log(data.tasks)
    } catch (err) {
      console.log("Error fetching tasks:", err);
    }
  }

  return (
    <>
      <div className="inputBox">
        <Card width="700px" height="550px">
          <div className="tasksPageLayout">
            <div className="tasksContainer">
              {tasks.length === 0 ? (
                <p style={{ color: "white" }}>No tasks found.</p>
              ) : (
                tasks.map((t, index) => (
                  <TaskCard
                    key={index}
                    task={t.task}
                    onEdit={() => alert("Edit clicked")}
                    onDelete={() => alert("Delete clicked")}
                  />
                ))
              )}
            </div>
            <button className="submit backBtn" onClick={goBackToMain}>
              Back
            </button>

          </div>
        </Card>
      </div>
    </>
  );
}

export default TaskPage;
