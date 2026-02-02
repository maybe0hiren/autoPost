import React from "react";
import "./TaskCard.css";

function TaskCard({ task, onEdit, onDelete }) {
  return (
    <div className="taskCard">
      <p className="taskText">{task}</p>

      <div className="cardButtons">
        <button className="cardBtn editBtn" onClick={onEdit}>
          Edit
        </button>

        <button className="cardBtn deleteBtn" onClick={onDelete}>
          Delete
        </button>
      </div>
    </div>
  );
}

export default TaskCard;
