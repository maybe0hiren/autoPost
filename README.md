# AutoPost 
Automated journaling agent using AI...


## Project Description

AutoPost is an AI-powered automation system that generates short
journal-style captions from daily tasks and posts them automatically to
X (formerly Twitter).

The system consists of:

-   A React frontend where users can submit, edit, and manage tasks
-   A Node.js + Express backend that stores tasks, generates captions
    using Gemini, and posts them via Ayrshare
-   A built-in scheduler that runs automatically at a configured time on alternate days
-   A live status logging system, so the frontend always shows the
    latest posting updates

AutoPost is modular, extendable, and designed for fully automated
content workflows.

---

## Key Features

-   Gemini-2.5-flash caption generation
-   Automated posting to X using Ayrshare
-   Task submission + edit + delete support
-   Alternate-day scheduled posting
-   Persistent status updates (success, failure, last run, caption)
-   JSON-based local task storage

---

## Packages

Backend Dependencies

-   express
-   cors
-   dotenv
-   fs, path
-   http-proxy-middleware (for ngrok multi-project support)

AI + Posting

-   @google/generative-ai
-   node-fetch (or built-in fetch in Node 18+)

---

## Ayshare

1.  Create an account at Ayrshare
2.  Link your X (Twitter) profile
3.  Generate an API key
4.  Add it to your .env file

---

## Keys

Store these in your backend .env:

-   GEMINI_API_KEY
-   AYRSHARE_KEY
-   KEY (frontend authentication key)

---

## Backend Endpoints

AutoPost Core


| Endpoint      | Method | Description                     |
|-------------|--------|---------------------------------|
| `/status`     | GET    | Server online check             |
| `/dayStatus`  | GET    | Alternate-day posting status    |
| `/getTasks`   | GET    | Retrieve all saved tasks        |
| `/task`       | POST   | Submit a new task               |
| `/editTask`   | PATCH  | Edit an existing task           |
| `/deleteTask` | DELETE | Delete a task                   |
| `/logs`       | GET    | Fetch latest status log         |


---

## Task Storage

Tasks are stored locally in:
    /data/tasks.json

Status logs are stored in:
    /data/status.json

Day counter is stored in:
    /data/day.txt

---

## Scheduler

autoPost v3 includes a built-in scheduler that:

-   Runs daily
-   Posts only on alternate days
-   Generates captions from tasks
-   Retries posting if failures occur
-   Clears tasks after successful posting
-   Updates frontend-visible logs

Posting time is configurable inside the scheduler module.

---

## Setup Instructions

1. Clone Repository
    git clone <repo-url>
    cd autoPost

2. Install Backend Dependencies
    npm install

3. Configure Environment Variables
Create a .env file:
    GEMINI_API_KEY=your_key
    AYRSHARE_KEY=your_key
    KEY=your_private_access_key

4. Start Backend
    nodemon app.js

5. Start Frontend
    npm start