import pandas as pd
import numpy as np

from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
from tensorflow.keras.models import load_model

pd.set_option('display.unicode.east_asian_width', True)
# data load
df = pd.read_csv('C:/Users/gkghk/PycharmProjects/food classification/datasets/datasets/first_concat_data/first_data.csv',index_col=0)
print(df.head())
print(df.tail())
