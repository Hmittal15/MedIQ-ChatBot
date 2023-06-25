import json 
import numpy as np
from tensorflow import keras
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from flask import Flask, request
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app=Flask(__name__)

def preprocess_text(text):
    # Load stop words
    stop_words = set(stopwords.words('english'))

    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Remove special characters and numbers
    text = re.sub('[^a-zA-Z]', ' ', text)
    
    # Tokenize the text
    words = nltk.word_tokenize(text)
    
    # Lemmatize and remove stop words
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words]
    
    return ' '.join(words)

@app.route('/chat', methods=['POST'])
def chat():
    inp = request.json['input']

    with open("intents.json") as file:
        data = json.load(file)

    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 200
    
    while True:
        preprocessed_input = preprocess_text(inp)
        sequence = tokenizer.texts_to_sequences([preprocessed_input])
        padded_sequence = keras.preprocessing.sequence.pad_sequences(sequence, truncating='post', maxlen=max_len)
        result = model.predict(padded_sequence)
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        probability = np.max(result)

        for i in data['intents']:
            if (len(i['tags'])>0):
                if i['tags'][0] == tag:
                    response = {'response': i['answer'], 'score': str(probability)}
                    return response

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8090)