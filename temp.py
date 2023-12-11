from transformers import pipeline
text = 'Hello!'
classifier = pipeline('sentiment-analysis', model='nvsl/bert-for-harsh')
result = classifier(text)
label = result[0]['label']
print(result)