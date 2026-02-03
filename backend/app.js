const express = require("express");
const cors = require("cors");
require("dotenv").config();

const acceptTasks = require('./functions/accept-tasks');
const altDayCheck = require("./functions/alt-day-check");
const getTasks = require("./functions/retrieve-tasks");
const deleteTask = require("./functions/dlt-task");
const editTask = require("./functions/edit-task");

const HttpError = require("./models/http-error");
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());


app.get("/status", (req, res, next) => {
  res.status(200).json({
      status: "Server Online"
  })
})

app.get("/dayStatus", (req, res, next) => {
  const dayStatus = altDayCheck().toString();
  res.status(200).json({
      status: dayStatus
  })
})

app.get("/getTasks", (req, res, next) => {
  try {
    const tasks = getTasks();

    res.status(200).json({
      success: "ok",
      tasks: tasks
    });
  } catch (err) {
    console.log("ERROR in /getTasks:", err);

    res.status(500).json({
      success: "fail",
      message: "Could not retrieve tasks"
    });
  }
});

app.post("/task", acceptTasks.acceptTasks);

app.delete("/deleteTask", (req, res, next) => {
  const { task } = req.body;
  deleteTask(task);
  res.status(200).json({
    success: "ok",
  });
});

app.patch("/editTask", (req, res) => {
  const { oldTask, newTask } = req.body;

  editTask(oldTask, newTask);

  res.status(200).json({
    success: "ok",
  });
});

app.use((error, req, res, next) => {
  if (res.headersSent) {
    return next(error);
  }

  res.status(error.code || 500).json({
    message: error.message || "An unknown error occurred"
  });
});

app.listen(PORT, () => {
    console.log("Server Running");
});