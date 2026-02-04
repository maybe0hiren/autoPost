const fs = require("fs");
const path = require("path");

function updateStatus(status, message, caption = "") {
  const filePath = "../data/status.json";

  const data = {
    lastRun: new Date().toISOString(),
    status: status,
    message: message,
    caption: caption
  };

  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
}

module.exports = updateStatus;
