const fs = require("fs");
const path = require("path");

function editTask(oldTask, newTask) {
  const filePath = "./data/tasks.json";;

  if (!fs.existsSync(filePath)) {
    return false;
  }

  const data = fs.readFileSync(filePath, "utf-8");
  let tasks = JSON.parse(data || "[]");

  tasks = tasks.map((t) =>
    t.task === oldTask ? { task: newTask } : t
  );

  fs.writeFileSync(filePath, JSON.stringify(tasks, null, 2));

  return true;
}

module.exports = editTask;
