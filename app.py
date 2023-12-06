# from flask import Flask, render_template, request
# from transformers import pipeline
# import pandas as pd
# app = Flask(__name__)
# PORT = 5500 

# @app.route("/", methods = ["GET", "POST"])
# def home():
#     if request.method == "POST":
#         txt = request.form["TEXt"]
#     return "<p>Hello World</p>"
#     # return render_template("index.html")

# if __name__ == "__main__":
#     app.run()
    
    
    

from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
PORT = 5000

# Load the sentiment analysis model
classifier = pipeline("sentiment-analysis")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    try:
        if request.method == 'POST':
            # Get the text input from the form
            text_input = request.form['text_input']

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
