import numpy as np
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
class TextCleaner :

    # init
    def __init__(self) -> None:
        pass

    # remove special characters
    def remove_special_characters(self, text):
        cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return cleaned_text
            
    # conveting to lowercase
    def to_lower_case(self, text):
        lowered_text = text.lower()
        return lowered_text

    # tokenize text
    def tokenize_text(self, text):
        tokens = word_tokenize(text)
        return tokens

    # Remove stop words
    def remove_stop_words(self,tokens):
        stop_words = set(stopwords.words("english"))
        filtered_tokens = [token for token in tokens if token not in stop_words]
        return filtered_tokens
    
    # Performing stemming 
    def perform_stemming(self,tokens):
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        return stemmed_tokens
    
    def clean_text(self,text):
        #Applying remove special characters
        cleaned_text = self.remove_special_characters(text)
        #Applying to lowercase
        cleaned_text = self.to_lower_case(cleaned_text)
        #Appling tokenzing
        tokens = self.tokenize_text(cleaned_text)
        #Remove stop words
        tokens = self.remove_stop_words(tokens)
        #Applying stemming
        tokens = self.perform_stemming(tokens)
        # return tokens
        return tokens
