import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)


stop_words = stopwords.words("english")
lemmatizer = nltk.stem.WordNetLemmatizer()

def nltk_tokenizer(document, join=True):
    '''Function to apply tokenization, stop_word removal and lemmetization
    in the provided document.

    Parameters
    ----------
    document: pd.Series
            Series with each row as the document of words
    
    join: bool
        True: Joins the lemmetized words back to sentences.

    Returns
    -------
    lems: list
        list of lemmitized document.
            
    '''
    tokens = document.apply(word_tokenize)
    tokens = tokens.apply(lambda x: [token for token in x if token not in stop_words])
    lems = tokens.apply(lambda x:[lemmatizer.lemmatize(token) for token in x])
    if join==True:
        return lems.apply(lambda x: ' '.join(x))
    else:
        return lems