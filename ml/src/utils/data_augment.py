import nlpaug.augmenter.word as naw
from nlpaug.util import Action
import pandas as pd
import nltk

nltk.download('averaged_perceptron_tagger', quiet=True)
def data_augment(corpus, label):
    syn_aug = naw.SynonymAug(aug_src="wordnet")
    rand_aug = naw.RandomWordAug(action="swap")
    data_struc = {'emotion_label': [], 'emotion_text': []}
    aug_dataframe = pd.DataFrame(data_struc)
    print('Augmenting data')
    for label, sentence in zip(label, corpus):
        if sentence.find("\n") > 0:
            sentence = sentence.replace("\n", "")

            aug_dataframe = aug_dataframe.append(
                {'emotion_label': label, 'emotion_text': sentence},
                ignore_index=True
            )
            
            augmented_sent = syn_aug.augment(sentence)
            aug_dataframe = aug_dataframe.append(
                {'emotion_label': label, 'emotion_text': augmented_sent},
                ignore_index=True
            )
        
            
            augmented_sent1 = rand_aug.augment(sentence)
            aug_dataframe = aug_dataframe.append(
                {'emotion_label': label, 'emotion_text': augmented_sent1},
                ignore_index=True
            )
        else:
            aug_dataframe = aug_dataframe.append(
                {'emotion_label': label, 'emotion_text': sentence},
                ignore_index=True
            )
            augmented_sent = syn_aug.augment(sentence)
            aug_dataframe = aug_dataframe.append(
                {'emotion_label': label, 'emotion_text': augmented_sent},
                ignore_index=True
            )
            aug1 = naw.RandomWordAug(action="swap")
            augmented_sent1 = rand_aug.augment(sentence)
            aug_dataframe = aug_dataframe.append(
                {'emotion_label': label, 'emotion_text': augmented_sent1},
                ignore_index=True
            )
    print('Augmentation Completed')
    return aug_dataframe['emotion_text'], aug_dataframe['emotion_label']