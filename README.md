# autoPost -- v2
Automated journaling agent using AI...


## Project Description

autoPost is an AI-driven automation system designed to generate personalized social media captions using Gemini-2.5-flash model. It includes a react webpage for the client interacting with a python script running on local device to handel the posting. Client and Server communicate through Supabase, enabling seamless automation of content creation and publishing workflows without manual intervention.

Key features include:  
- Gemini-2.5-flash api communication  
- Automated X (formerly twitter) posting  
- Schedule-based automation for timed alternate day posting.   
- Modular, maintainable codebase organized for extension and customization.

---

## Packages

- google-genai 
- supabase  (Python)
- python-dotenv
- requests, os, json, datetime, time, requests

- supabase (React)
- react-router-dom

---

## Supabase

- Create project and get project URL and KEY
- Create a table: {id, task, imageURLs} (Add imageURLs if planning on posting images)
- Disable RLS on database (For personal project)
- Add anon permissions to storage (For personal projects and if planning on posting images)

---

## Ayshare

- Make an account
- Link the social media you want (X for this project)
- Get Ayshare API key

---

## Keys

- Gemini API key
- Supabase Key
- Supabase URL
- Ayshare API Key
