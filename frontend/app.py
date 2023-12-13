from flask import Flask, render_template, request
import requests
from apify_client import ApifyClient

app = Flask(__name__)
PORT = 5000

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_2QGQH8DkI54nayPr5grpIauvPmWqFL3NwQ4M")

# Function to extract text from a Twitter link using Apify
def extract_text_from_twitter_link(tweet_url):
    run_input = {
        "startUrls": [{"url": tweet_url}],
        "tweetsDesired": 1,
        "addUserInfo": False,
    }

    run = client.actor("KVJr35xjTw2XyvMeK").call(run_input=run_input)

    # Fetch and return the full_text of the tweet
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        return item.get("full_text", None)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/sentiment-analyzer', methods=['POST'])
def predict_sentiment():
    try:
        if request.method == 'POST':
            text_input = request.form.get('text_input', '')

            # Check if the input is a Twitter link
            if text_input.startswith('https://twitter.com/'):
                # Extract text from the Twitter link
                tweet_text = extract_text_from_twitter_link(text_input)
                if tweet_text:
                    text_input = tweet_text
                else:
                    raise Exception("Error extracting text from Twitter URL")

            # Perform sentiment analysis using the backend API
            response = requests.post("backend:6000/", files={'user_text': text_input})

            label = 'The statement is '

            if response.status_code == 200:
                predictions = response.json().get('predictions')

                n = len(predictions)

                for i, key in enumerate(predictions):
                    key = str(key)
                    if key.startswith('NOT_'): key = 'not ' + key.split('_')[-1]
                    label += str(key)
                    if i < n-2: label += ', '
                    elif i == n-2: label += ' and '
                    elif i == n-1: label += '.'

                return render_template("result.html", label=label, text_input=text_input)

            else:
                error = "Error in prediction request. Status code: {}".format(response.status_code) + response.json().get('error')
                return render_template("result.html", err=error)

    except Exception as e:
        error = "Error: Text can't be processed"
        return render_template("result.html", err=e)

if __name__ == "__main__":
    app.run(port=PORT, debug=True, host='0.0.0.0')

