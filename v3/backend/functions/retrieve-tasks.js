const fs = require("fs");
const path = require("path");

function retrieveTasks() {
    const filePath = "./data/tasks.json";

    if (!fs.existsSync(filePath)) {
        return [];
    }

    const data = fs.readFileSync(filePath, "utf-8");
    return JSON.parse(data || "[]");
}

module.exports = retrieveTasks;
