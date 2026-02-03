const fs = require("fs");
const path = require("path");

function deleteTask(taskText) {
  const filePath = "./data/tasks.json";
  if (!fs.existsSync(filePath)) {
    return false;
  }

  const data = fs.readFileSync(filePath, "utf-8");
  let tasks = JSON.parse(data || "[]");

  const updatedTasks = tasks.filter((t) => t.task !== taskText);

  fs.writeFileSync(filePath, JSON.stringify(updatedTasks, null, 2));

  return true;
}

module.exports = deleteTask;
