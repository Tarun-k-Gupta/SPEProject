import unittest
from transformers import pipeline

harsh_classifier = pipeline("sentiment-analysis", model='nvsl/bert-for-harsh')

class Tester(unittest.TestCase):

    def test1(self):
        
        text = 'Thank you sir! I am grateful.'
        output = harsh_output = 'NOT_harsh'
        result = harsh_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, harsh_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")
    

    def test2(self):
        
        text = 'hey Stupid. shut up your mouth..'
        output = harsh_output = 'harsh'
        result = harsh_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, harsh_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")


if __name__ == '__main__':

    unittest.main()