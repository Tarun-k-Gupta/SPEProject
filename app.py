from flask import Flask, render_template, request
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
PORT = 5000

# Load the sentiment analysis model
classifier = pipeline("sentiment-analysis")

# def extract_text_from_twitter_url(tweet_url):
#     try:
#         # Send a request to the Twitter link
#         response = requests.get(tweet_url)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract the tweet text
#         tweet_text = soup.find('meta', property='og:description')['content']

#         return tweet_text
#     except Exception as e:
#         print(f"Error extracting text from Twitter URL: {e}")
#         return None

# def extract_text_from_twitter_url(tweet_url):
#     try:
#         # Send a request to the Twitter link
#         response = requests.get(tweet_url)
#         response.raise_for_status()  # Raise an HTTPError for bad responses

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract the tweet text if the meta tag exists
#         meta_description = soup.find('meta', property='og:description')
#         if meta_description and 'content' in meta_description.attrs:
#             tweet_text = meta_description['content']
#             return tweet_text
#         else:
#             raise Exception("Meta tag or 'content' attribute not found in HTML")

#     except requests.exceptions.RequestException as req_err:
#         print(f"Error with the request to Twitter URL: {req_err}")
#     except Exception as e:
#         print(f"Error extracting text from Twitter URL: {e}")

#     return None

def extract_text_from_twitter_url(url, div_class='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-1inkyih r-16dba41 r-bnwqim r-135wba7'):
    try:
        # Send a request to the Twitter URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all div elements with the specified class
        tweet_text_divs = soup.find_all('div', {'class': div_class})

        if not tweet_text_divs:
            raise Exception(f"No divs with class '{div_class}' found in HTML")

        # Extract text from the first div (you can customize this logic based on your needs)
        tweet_text_parts = [element.get_text(strip=True) for element in tweet_text_divs[0].find_all(['span', 'img'])]

        # Join the text parts to get the complete tweet text
        tweet_text = ' '.join(tweet_text_parts)
        print("tweet_text", tweet_text)
        return tweet_text

    except requests.exceptions.RequestException as req_err:
        print(f"Error with the request to Twitter URL: {req_err}")
    except Exception as e:
        print(f"Error extracting text from Twitter URL: {e}")

    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    try:
        if request.method == 'POST':
            # Check if the user provided text or a Twitter URL
            print("hellooooooooooooooooo")
            text_input = request.form.get('text_input', '')

            if text_input.startswith('https://twitter.com/'):
                # Extract text from the provided Twitter URL
                tweet_text = extract_text_from_twitter_url(text_input)
                if tweet_text:
                    text_input = tweet_text
                    print(tweet_text)
                else:
                    raise Exception("Error extracting text from Twitter URL")

            # Perform sentiment analysis using the loaded model
            sentiment_prediction = classifier(text_input)

            # Get the predicted label and score
            label = sentiment_prediction[0]['label']
            score = sentiment_prediction[0]['score']

            # Render the result on the website
            return render_template("result.html", label=label, score=score, text_input=text_input)

    except Exception as e:
        error = "Error: Text can't be processed"
        return render_template("result.html", err=error)

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
