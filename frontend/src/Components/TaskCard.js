import React, { useState } from "react";
import "./TaskCard.css";

function TaskCard({ task, onEdit, onDelete }) {
  const [isEditing, setIsEditing] = useState(false);
  const [newTask, setNewTask] = useState(task);

  function handleSave() {
    onEdit(task, newTask);
    setIsEditing(false);
  }

  function handleCancel() {
    setNewTask(task);
    setIsEditing(false);
  }

  return (
    <div className="taskCard">
      
      {isEditing ? (
        <input
          className="taskEditInput"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
        />
      ) : (
        <p className="taskText">{task}</p>
      )}

      <div className="cardButtons">
        {isEditing ? (
          <>
            <button className="cardBtn editBtn" onClick={handleSave}>
              Save
            </button>

            <button className="cardBtn deleteBtn" onClick={handleCancel}>
              Cancel
            </button>
          </>
        ) : (
          <>
            <button
              className="cardBtn editBtn"
              onClick={() => setIsEditing(true)}
            >
              Edit
            </button>

            <button className="cardBtn deleteBtn" onClick={onDelete}>
              Delete
            </button>
          </>
        )}
      </div>
    </div>
  );
}

export default TaskCard;
