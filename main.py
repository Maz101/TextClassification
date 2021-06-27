from flask import Flask, jsonify, request
from typing import Literal
import pickle
import pandas as pd
from normalize import normalizesentence

app = Flask(__name__)


LABELS = Literal[
    "Dementia",
    "ALS",
    "Obsessive Compulsive Disorder",
    "Scoliosis",
    "Parkinson’s Disease",
]

vectorizer = pickle.load(open('vectorizer.pk','rb'))
loaded_model = pickle.load(open('logistic_.pk','rb'))
encoder = pickle.load(open('encoder.pk','rb'))



def predict(description: str) -> LABELS:
    """
    Function that should take in the description text and return the prediction
    for the class that we identify it to.
    The possible classes are: ['Dementia', 'ALS',
                                'Obsessive Compulsive Disorder',
                                'Scoliosis', 'Parkinson’s Disease']
    """

    description = normalizesentence(description)
    tfidf_str = vectorizer.transform(pd.Series(description))
    prediction_v = loaded_model.predict(tfidf_str)

    return encoder.inverse_transform(prediction_v)[0]

    raise NotImplementedError()


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/predict", methods=["POST"])
def identify_condition():
    data = request.get_json(force=True)
    prediction = predict(data["description"])

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run()