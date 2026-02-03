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

  async function handleDelete(taskText) {
    await fetch(`${api}/deleteTask`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ task: taskText })
    });

    getTasks(); 
  }

  async function handleEdit(oldTask, newTask) {
    if (!newTask.trim()) return;

    await fetch(`${api}/editTask`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        oldTask: oldTask,
        newTask: newTask
      })
    });

    getTasks();
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
                    onEdit={handleEdit}
                    onDelete={() => handleDelete(t.task)}
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
