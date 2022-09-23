import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from configs import config
from features.build_features import feature_engineer
from evaluate.evaluation import conf_matrix_plot, report_classification
from utils.dispatcher import ml_model_dispatcher
import pickle

def ml_model_training(model='naive_bayes', save_report=False, feature_method='count', n_gram=(1,1)):
    """Conducts training of the Machine learning model and upload metric to mlflow

    Conducts the training of machine learning model using either
    Naive_bayes or Support_vector_machine.

    Parameters
    ----------
    model: 'String'
            either "naive_bayes" or "svc"
    
    save_report: bool
            if true saves the classification report and heatmap in CSV file 
            if false just prints the report
    
    feature_method: String
                'count' or 'tfidf'; method to create features from senteces
    
    n_gram: tuple (min_n, max_n), default=(1, 1)
            The lower and upper boundary of the range of n-values for different
            word n-grams or char n-grams to be extracted. All values of n such
            such that min_n <= n <= max_n will be used. For example an
            ``ngram_range`` of ``(1, 1)`` means only unigrams, ``(1, 2)`` means
            unigrams and bigrams, and ``(2, 2)`` means only bigrams.
            Only applies if ``analyzer is not callable``
    """
    features, enc_labels, labels = feature_engineer(method=feature_method, n_gram=n_gram)
    trained_model = None

    try:
        trained_model = ml_model_dispatcher(model)
        X_train, X_test, y_train, y_test = train_test_split(features,
                                        enc_labels.ravel(),
                                        test_size=0.2)
        
        with mlflow.start_run(run_name=model+"_"+feature_method):
            print('------------Starting Model Training------------')
            trained_model.fit(X_train, y_train)

            print('------------Training Completed---------------')
            predicted_label_train = trained_model.predict(X_train)
            predicted_label_test = trained_model.predict(X_test)

            train_accuracy = accuracy_score(y_train, predicted_label_train)
            test_accuracy = accuracy_score(y_test, predicted_label_test)

            # storing the test report only
            train_report, test_report =  report_classification(model, y_train, y_test, predicted_label_train, predicted_label_test, save=save_report)

            # logging metrics
            mlflow.log_metric('train_accuracy', train_accuracy)
            mlflow.log_metric('test_accuracy', test_accuracy)
            mlflow.log_metric('Train_precision', train_report['weighted avg']['precision'])
            mlflow.log_metric('Train_recall', train_report['weighted avg']['recall'])
            mlflow.log_metric('Train_f1_score', train_report['weighted avg']['f1-score'])
            mlflow.log_metric('Test_precision', test_report['weighted avg']['precision'])
            mlflow.log_metric('Test_recall', test_report['weighted avg']['recall'])
            mlflow.log_metric('Test_f1_score', test_report['weighted avg']['f1-score'])


            mlflow.log_param('classifier', model)

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(trained_model, "model", registered_model_name=model)
            else:
                mlflow.sklearn.log_model(trained_model, "model")

            if save_report==True:
                conf_matrix_plot(model, y_test, predicted_label_test, labels)
                report_classification(model, y_train, y_test, predicted_label_train, predicted_label_test, save=save_report)
        
    except KeyError:
        print('Please enter a valid model, either \'naive_bayes\', \'softmax_l1\', \'softmax_l2\', \'svc\'')

    with open(os.path.join(config.MODEL_PATH, model+"_"+feature_method+".pkl"), 'wb') as file:
        pickle.dump(trained_model, file)


