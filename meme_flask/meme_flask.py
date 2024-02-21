# import the Flask class from the flask module #render_template allows
from flask import Flask, render_template
# us to reference and use external html code or script
import requests  # import the requests module
import json  # import the json module

app = Flask(__name__)#create an instance of the Flask class

def get_meme():
    url = "https://meme-api.com/gimme"  # url to meme api
    response = json.loads(requests.request("GET",url).text)# get the response from the url and convert it to a json object
    meme_large = response['preview'][-2] # get the second to last image
    subreddit = response['subreddit'] # get the subreddit
    author = response['author'] # get the author
    return meme_large, subreddit, author  # return the image and subreddit and author

@app.route("/")  # python decorator
def index():
    meme_pic, subreddit, author = get_meme() # get the meme and subreddit and author
    return render_template("meme_index.html", meme_pic = meme_pic, subreddit = subreddit, author = author) # return the meme and subreddit and author

app.run(host="0.0.0.0", port=80)  # run the app
