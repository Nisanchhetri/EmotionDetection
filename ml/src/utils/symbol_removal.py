
def removal(document):

    """ Function to remove symbols from document.

    Parameters
    ----------
    document: pd.Series
            Series with each row as the document of words
    Returns
    -------
    rem_document: list
            document of words with removed symbols
    """
    
    rem_document = document.str.replace('.', '')
    rem_document = rem_document.str.replace(',', ' ')

    return rem_document