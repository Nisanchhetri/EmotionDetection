import requests
import os
import sys
import pandas as pd
from configs import config

dataset_path = os.path.join(config.DATA_DIR, config.DATASET)

def download_dataset(url=config.DATASET_URL):
    """
    Download the dataset from given Google drive's file ID

    This function will download the Dataset file from the given drive's file ID path
    and store in the "data/external" folder of this project. The ID must be fromthe
    sharable link of the file.

    Parameters
    ----------
    id: String
        Valid ID from file's sharable link

    Returns
    -------
    None
    """

    if os.path.exists(dataset_path):
        print(f'{config.DATASET} already exists, fetching dataset!!')
    
    else:
        print('Downloading Dataset')
        response = requests.get(url, stream=True)

        with open(dataset_path, 'wb') as f:
            f.write(response.content)

        print('Download completed, now fetching the dataset')


def fetch_dataset(path=dataset_path):
    """
    Function to load the dataset in proper format

    This function loads the dataset from the given path and 
    adds columns names to the ISEAR dataset

    Parameters
    ----------
    path: String
        Path of the dataset

    Returns
    -------
    dataset: Pandas DataFrame
            Dataframe containing the vanilla dataset
    """
    download_dataset()

    dataset = pd.read_csv(dataset_path, header=None)

    dataset.drop(columns=[0], axis=1, inplace=True)

    dataset.columns = ['emotion', 'sentences']

    return dataset

        





