from flask import Flask, render_template, request
import requests

app = Flask(__name__)
PORT = 5000

# # Load the sentiment analysis model

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/sentiment-analyzer', methods=['POST'])
def predict_sentiment():
    try:
        if request.method == 'POST':
            text_input = request.form.get('text_input', '')

            response = requests.post("http://backend:6000/", files={'user_text': text_input})


            # label = sentiment_prediction[0]['label']
            # score = sentiment_prediction[0]['score']
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
