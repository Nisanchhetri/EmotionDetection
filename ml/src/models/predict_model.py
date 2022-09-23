import pickle
import os
import pandas as pd

from features.build_features import feature_engineer
from utils.lower_case import lower_casing
from utils.symbol_removal import removal
from utils.tokenizer import nltk_tokenizer
from configs import config

def get_prediction(sentence):
    """
    Returns emotion prediction given the sentence

    Parameters
    ----------
    sentence: String
            Sentence that's emotion is to be predicted
    
    Returns
    -------
    prediction: String
                Predicted emotion
    confidence: float
                Prediction probability of the classifier
    """
    with open(os.path.join(config.MODEL_PATH, "svc_count.pkl"), 'rb') as file:
        trained_model = pickle.load(file)

    with open(os.path.join(config.MODEL_PATH, "label_encoder.pkl"),  'rb') as file:
        label_encoder = pickle.load(file)

    with open(os.path.join(config.MODEL_PATH, "vectorizer.pkl"),  'rb') as file:
        vectorizer = pickle.load(file)

    series = pd.Series(sentence)

    processed_sentence =  nltk_tokenizer(removal(lower_casing(series)), join=True)
    
    feature = vectorizer.transform(processed_sentence)

    encoded_prediction = trained_model.predict(feature)
    
    confidence = trained_model.predict_proba(feature).max()
    prediction = label_encoder.inverse_transform(encoded_prediction.reshape(1,-1))[0][0]

    return prediction, confidence
