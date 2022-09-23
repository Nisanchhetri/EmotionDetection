from data.get_dataset import fetch_dataset
from utils.lower_case import lower_casing
from utils.symbol_removal import removal
from utils.tokenizer import nltk_tokenizer
from utils.data_augment import data_augment
import pandas as pd


def data_preprocess(join=True):
    """
    Function to preprocess the corpus of words in proper format

    This function loads the dataset and drops any missing value, 
    then applies, lower_casing, symbol_removal and tokenization(tokenization,
    stop_word removal and lemmitization).

    Parameters
    ----------
    join: bool
        if True joins the tokens.

    Returns
    -------
    processed_corpus: pd.Series
                    column with processed document on each row.
    
    label: pd.Series
        column with each row consisting the respective emotion label/target with the processed corpus.
    """
    

    dataset = fetch_dataset()
    print('Preprocessing text')
    dataset.dropna(axis=0, inplace=True)
    
    corpus = dataset['sentences']
    label = dataset['emotion']
    corpus, label = data_augment(corpus, label)
    processed_corpus = nltk_tokenizer(removal(lower_casing(corpus)), join=join)

    print('Preprocessing Completed')
    return processed_corpus, label