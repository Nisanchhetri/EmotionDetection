import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import pandas as pd
import os
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings("ignore")

from configs import config

pylab.rcParams.update(config.PLOT_PARAMS)

def conf_matrix_plot(model_name, y_test, y_test_pred, target): 
        """
        Plot the test set confusion matrix

        Parameters
        ----------
        model_name: string
                Name of the model

        y_test: array, [number of observation, 1]
                test set target labels

        y_test_pred: array , [number of observation, 1]
                predicted labels of the test_set

        target: list
                original target labels

        """
        print('Saving confusion Matrix')
        confusion_mat_test = confusion_matrix(y_test, y_test_pred)

        plt.figure(figsize=(12,8))
        ax = sns.heatmap(confusion_mat_test.T, square=True, annot=True, fmt='d', cbar=True)
        ax.set_xticklabels(list(target[0]))
        ax.set_yticklabels(list(target[0]))
        plt.title(model_name+'_train_heatmap')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.savefig(os.path.join(config.OUTPUT_PATH, model_name+'_test_heatmap.png'))
        print('Completed')

                        
def report_classification(model_name, y_train, y_test, y_train_pred, y_test_pred, save=True):
        """Return and/or Save classification report in CSV files

        Parameters
        ----------
        model_name: string
                        Name of the model

        y_train: array, [number of observation, 1]
                train set target labels

        y_train_pred: array , [number of observation, 1]
                        predicted labels of the train_set
                        
        y_test: array, [number of observation, 1]
                test set target labels

        y_test_pred: array , [number of observation, 1]
                        predicted labels of the test_set


        Returns
        -------
        train_report_dict: Dictionary
                        Train set classification report
        
        test_report_dict: Dictionary
                        Test set classification report
        """
        print('Computing Classification Report')
        

        train_report_dict = classification_report(y_train, y_train_pred, digits=3, output_dict=True)
        test_report_dict = classification_report(y_test, y_test_pred, digits=3, output_dict=True)
        print('Completed')
        if save==True:
                print('Saving the classification report')
                train_report = pd.DataFrame(train_report_dict).transpose()

                test_report = pd.DataFrame(test_report_dict).transpose()
                
                train_report.to_csv(os.path.join(config.OUTPUT_PATH,model_name+'_train_report.csv'))
                test_report.to_csv(os.path.join(config.OUTPUT_PATH, model_name+'test_report.csv'))
                print('Completed')
        
        return train_report_dict, test_report_dict