import numpy as np
import pandas as pd
from text_cleaner import TextCleaner
def data_preprocess(df):
    df["body"] = df["body"].apply(TextCleaner().clean_text)
    return df
    
