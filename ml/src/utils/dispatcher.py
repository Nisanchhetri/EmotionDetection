from sklearn.naive_bayes import MultinomialNB # Baseline model for 1st Iteration
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Dictionary to hold models
def ml_model_dispatcher(model):
    '''
    Return ML model given a key

    Parameters
    ----------
    model: String 
            Name/key for the Ml model ('softmax_l1', 'softmax_l2', 'naive_bayes', 'svc')
    
    Returns
    -------
    model_dict[model]: Sklearn's predictor object
                    Respective ML model 
    
    '''
    model_dict={
        'softmax_l1': LogisticRegression(penalty='l1', multi_class="multinomial", solver='saga'),
        'softmax_l2': LogisticRegression(penalty='l2', multi_class="multinomial"),
        'naive_bayes': MultinomialNB(),
        'svc': SVC(probability=True),
        'rand_clf': RandomForestClassifier()
    }

    return model_dict[model]