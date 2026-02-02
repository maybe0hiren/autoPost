const fs = require("fs");
const HttpError = require("../models/http-error");

function saveTask(task) {
    const filePath = "./data/tasks.json";
    let tasks = [];

    if (fs.existsSync(filePath)) {
        const data = fs.readFileSync(filePath, "utf-8");
        tasks = JSON.parse(data || "[]");
    }

    const newTask = {
        task: task
    };
    tasks.push(newTask);
    fs.writeFileSync(filePath, JSON.stringify(tasks, null, 2));
    console.log(`Task: ${task} saved successfully!`);
}

async function acceptTasks(req, res, next) {
    const task = req.body.task;
    const key = req.body.key;

    if (key !== process.env.KEY) {
        return next(new HttpError("Invalid Key...", 401));
    }

    if (!task) {
        return next(new HttpError("Empty Task...", 400));
    }

    saveTask(task);

    res.status(201).json({
        success: "ok",
        message: "Task saved successfully"
    });
}

exports.acceptTasks = acceptTasks;
