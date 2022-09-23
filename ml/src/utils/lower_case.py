def lower_casing(document):
    """ Function to convert all words to lowercase

    Parameters
    ----------
    document: pd.Series
            Series with each row as the document of words
    Returns
    -------
    low_document: list
            document with lowercase words
    """
    
    low_document = document.apply(lambda x: ' '.join(x.lower() for x in x.split()))
    return low_document
