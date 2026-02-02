const express = require("express");
const cors = require("cors");
require("dotenv").config();

const acceptTasks = require('./functions/accept-tasks');


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

app.post("/task", acceptTasks.acceptTasks);

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