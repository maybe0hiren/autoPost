require("dotenv").config();
const AYRSHARE_KEY = process.env.AYRSHARE_KEY;

async function postToX(caption){
    const url = "https://app.ayrshare.com/api/post";

    try{
        const response = await fetch(url, {
            method: "POST",
            headers: {
                Authorization: `Bearer ${AYRSHARE_KEY}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                post: caption,
                platforms: ["twitter"]
            })
        });

        const result = await response.json();
        console.log(result);
        return result.status;
    } catch (err) {
        console.log("Error posting to X: ", err);
        return "failed";
    }
}


module.exports = postToX;