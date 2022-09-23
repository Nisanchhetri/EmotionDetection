import os

ROOT_DIR = os.path.abspath(os.curdir)

DATA_DIR = os.path.join(ROOT_DIR, 'ml/data/external')

DATASET = 'ISEAR_dataset.csv'

DATASET_URL = 'https://docs.google.com/uc?export=download&id=11VDtm3zI012vFKHiuaJqwsWVwYz_prxF'

MODEL_PATH = os.path.join(ROOT_DIR, 'ml/model')

CHECKPOINT_PATH = os.path.join(ROOT_DIR, "checkpoints")

OUTPUT_PATH = os.path.join(ROOT_DIR, "out")

LOG_PATH = os.path.join(ROOT_DIR, 'logs')

PLOT_PARAMS = {'legend.fontsize': 20,
'figure.figsize': (15, 5),
'axes.labelsize': 20,
'axes.titlesize': 20,
'xtick.labelsize':15,
'ytick.labelsize':15}