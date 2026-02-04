const cron = require("node-cron");

const mainFunction = require("./main");
const altDayCheck = require("./alt-day-check");

function startScheduler() {
  console.log("Scheduler started... Will check every day at 10 PM.");

  cron.schedule("0 22 * * *", async () => {
    console.log("\n10 PM Trigger Fired...");

    if (altDayCheck()) {
      console.log("Even day → Running posting job...");
      await mainFunction();
    } else {
      console.log("Odd day → Skipping today (alternate day rule).");
    }
  });
}

module.exports = startScheduler;
