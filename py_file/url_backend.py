import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from joblib import Memory
from functools import lru_cache

memory = Memory("./cachedir", verbose=0)

def makeTokens(f):
    f_str = str(f.encode('utf-8'))
    
    tokens = set()
    for part in f_str.split('/'):
        for subpart in part.split('-'):
            tokens.update(subpart.split('.'))
    
    tokens.discard('com')
    
    return list(tokens)

@lru_cache
def load_and_preprocess_data(file_path):
    urls_data = pd.read_csv(file_path)
    y = urls_data["label"]
    url_list = urls_data["url"]
    return url_list, y
def imp(info):
    url_list, y = load_and_preprocess_data("./data_det/urldata.csv")
    
    vectorizer = TfidfVectorizer(tokenizer=makeTokens, max_features=5000, ngram_range=(1, 2))
    X = vectorizer.fit_transform(url_list)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    logit = LogisticRegression(max_iter=100)
    logit.fit(X_train, y_train)
    
    X_predict1 = vectorizer.transform([info])
    New_predict1 = logit.predict(X_predict1)
    
    accuracy = logit.score(X_test, y_test)
    print(accuracy, New_predict1[0])
    return accuracy, New_predict1[0]



