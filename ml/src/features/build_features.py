import os
import numpy as np
import pickle
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from configs import config
from features.text_preprocesser import data_preprocess

def feature_engineer(method="count", n_gram=(1,1)):
    """Conducts feature engineering on the preprocessed dataset

    Preprocessing involves CountVectorizer/TfIdfVectorizer for features
    and Label Encoding for target labels

    Parameters
    ----------
    method: string, default="count"
            "count" or "tfidf", used to choose the BOG method

    n_gram: tuple (min_n, max_n), default=(1, 1)
            The lower and upper boundary of the range of n-values for different
            word n-grams or char n-grams to be extracted. All values of n such
            such that min_n <= n <= max_n will be used. For example an
            ``ngram_range`` of ``(1, 1)`` means only unigrams, ``(1, 2)`` means
            unigrams and bigrams, and ``(2, 2)`` means only bigrams.
            Only applies if ``analyzer is not callable``

    Returns
    -------
    features: array, [n_samples, n_features]
            Document-term matrix.
    
    encoded_label: array, [n_sample,]
                Label encoded target.

    encoded_category: array
                    consist of names of encoded category
    """
    
    label_encoder = OrdinalEncoder()
    data, label = data_preprocess(join=True)

    print('Starting Feature Engineering')
    encoded_label = label_encoder.fit_transform(np.array(label).reshape(-1,1))

    encoded_category = label_encoder.categories_

    if method == "count":
        vect = CountVectorizer(lowercase=False, ngram_range=n_gram)
        features = vect.fit_transform(data)
    elif method == 'tfidf':
        vect = TfidfVectorizer(lowercase=False, ngram_range=n_gram)
        features = vect.fit_transform(data)
    
    print('Completed')  

    # store the vectorizer
    with open(os.path.join(config.MODEL_PATH, "vectorizer.pkl"), 'wb') as file:
        pickle.dump(vect, file)
    # store the encoder
    with open(os.path.join(config.MODEL_PATH, "label_encoder.pkl"), 'wb') as file:
        pickle.dump(label_encoder, file)
        
    return features, encoded_label, encoded_category