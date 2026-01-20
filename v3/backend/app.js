const express = require("express");
const cors = require("cors");
require("dotenv").config();


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

app.post("/task", (req, res, next) => {
    const { task, key } = req.body;
    if (key !== process.env.KEY){
        const error = new HttpError("Invalid Key...", 401);
        return next(error)
    } 
    else if (!task){
        const error = new HttpError("Empty Task...", 400);
        return next(error);
    }
    console.log(task);
    res.status(201).json({
        success: "ok",
        message: "Task saved successfully"
    });
})

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