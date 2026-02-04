require("dotenv").config();
const { GoogleGenerativeAI } = require("@google/generative-ai");

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

async function getCaption(prompt) {
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

  const response = await model.generateContent(prompt);

  return response.response.text();
}

module.exports = getCaption;
