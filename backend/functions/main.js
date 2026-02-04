const fs = require("fs");
const path = require("path");

const getTasks = require("./retrieve-tasks");
const getCaption = require("./get-caption");
const postToX = require("./post-to-X");
const updateStatus = require("./update-status");


function getDay() {
  const filePath = "./data/day.txt";

  if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, "1");
    return 1;
  }

  const day = parseInt(fs.readFileSync(filePath, "utf-8").trim());
  return day;
}

function incrementDay() {
  const filePath = "./data/day.txt";
  const day = getDay();
  fs.writeFileSync(filePath, String(day + 1));
}

async function mainFunction() {
  let tasks = getTasks();

  if (!tasks || tasks.length === 0) {
    console.log("NOTHING TODAY!");
    return;
  }

  tasks = tasks.map((t) => t.task);

  const taskString = tasks.join(", ");

  const prompt = "Here is a list of tasks id did: " + tasks + " Make a twitter caption journaling about the tasks. Keep it brief. The number of characters must not exceed 230. Don't give me options or other conversational lines, just the caption... Short and concise, not more than 230"

  const maxRetries = 5;
  updateStatus("running", "Generating caption...");
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    console.log(`Attempt ${attempt}...`);

    let caption = await getCaption(prompt);

    caption = `Day ${getDay()}: ${caption}`;

    if (caption.length >= 250) {
      console.log("Caption too long, retrying...");
      continue;
    }
    updateStatus("running", "Posting to Twitter...", caption);
    const response = await postToX(caption);

    if (response === "success") {
      updateStatus("success", "Posted successfully!", caption);  
      console.log(`Posted: ${caption}`);
      fs.writeFileSync(
        "./data/tasks.json",
        JSON.stringify([], null, 2)
      );
      incrementDay();
      console.log("Tasks cleared + Day incremented.");
      return;
    }

    console.log("Post failed, retrying...");
  }
  updateStatus("failed", "Posting failed.", caption);
  console.log("Failed after maximum retries.");
}

module.exports = mainFunction;
