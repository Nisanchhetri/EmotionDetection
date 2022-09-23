# file to operate the training and prediction
import os
import sys
import argparse

# Appending path to libraries
sys.path.append(os.path.join(os.path.abspath(os.curdir),'ml'))
sys.path.append(os.path.join(os.path.abspath(os.curdir),'api'))

from models.train_model import ml_model_training
from settings import PORT
from app import app
from models.predict_model import get_prediction

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--train", "-t", help="Trains the model with dataset and stores the model")
parser.add_argument("--model", "-m", help="Model to train the dataset value = \"softmax_l1\", \"softmanx_l2\", \"svc\", \"naive_bayes\", \"rand_clf\"")
parser.add_argument("--save", "-s", help="whether to save classification report or not (y or n)")
parser.add_argument("--feature", "-f", help="takes value \"count\" or \"tfidf\"")

# Read arguments from the command line
args = parser.parse_args()

# Training the model if user wants to.
if args.train=='yes':
    if args.model not in ["softmax_l1", "softmax_l2", "svc", "naive_bayes", 'rand_clf']:
        raise Exception('Enter valid algorithm')
    if args.feature not in ["count" or "tfidf"]:
        raise Exception('Enter valid feature extraction method')
    if args.save=='y':
            ml_model_training(model=args.model , save_report=True,  feature_method=args.feature, n_gram=(1,1))
    elif args.save=='n':
            ml_model_training(model=args.model , save_report=False,  feature_method=args.feature, n_gram=(1,1))
    else:
        raise Exception('Enter only y or n for saving the report')

print('----------------Starting Server-----------------')
# Starting the server
if __name__ == '__main__':
    app.run(port=PORT)







