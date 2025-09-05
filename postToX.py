import tweepy

apiKey = "TOKEN HERE"
apiSecret = "SECRET HERE"
accessToken = "TOKEN HERE"
accessSecret = "SECRET HERE"

auth = tweepy.OAuth1UserHandler(apiKey, apiSecret, accessToken, accessSecret)
api = tweepy.API(auth)

client = tweepy.Client(
    consumer_key=apiKey,
    consumer_secret=apiSecret,
    access_token=accessToken,
    access_token_secret=accessSecret
)

def post(captionFile, images=None):
    with open(captionFile, "r", encoding="utf-8") as f:
        caption = f.read().strip()
    imagePaths = images or []

    mediaIDs = []
    for path in imagePaths:
        media = api.media_upload(filename=path)
        mediaIDs.append(media.media_id)
    
    api.update_status(status=caption, media_ids=mediaIDs)


#Only Text
# def post(captionFile):
#     with open(captionFile, "r", encoding="utf-8") as f:
#         caption = f.read().strip()
    
#     api.update_status(status=caption)

if __name__ == "__main__":
    post("etc/trial.txt")
    post("etc/trial.txt", ["etc/image.png"])
        