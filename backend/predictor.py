import os
from flask import Flask, jsonify, request

from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':

            # path_to_models = 'BERTModels'
            # models = os.listdir(path_to_models)
            
            if 'user_text' not in request.files:
                return jsonify({'error': 'No file found in the request'})

            user_file = request.files['user_text']

            if user_file.filename == '':
                return jsonify({'error': 'Empty filename'})

            # Assuming the file contains text and you want to read its content
            text = user_file.read().decode('utf-8')

            predictions = []
            classifiers = {}

            classifiers['harsh'] = pipeline('sentiment-analysis', model='nvsl/bert-for-harsh')
            # classifiers['threatening'] = pipeline('sentiment-analysis', model='nvsl/bert-for-threatening')
            sentiments = classifiers.keys()


            for sentiment in sentiments:           
                result = classifiers[sentiment](text)
                label = result[0]['label']
                predictions.append(label)

            # To be changed later after integrating remaining models

            final_prediction = {'predictions': predictions}
            return jsonify(final_prediction)
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=6000, debug=True, host='0.0.0.0')
