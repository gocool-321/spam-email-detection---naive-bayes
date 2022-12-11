import fastapi
from fastapi.middleware.cors import CORSMiddleware
import pickle
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

api = fastapi.FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=['*'],
    allow_credentials=True)


def predict(text):
    t = pickle.load(open('./transformer.pkl', 'rb'))
    m = pickle.load(open('./model.pkl', 'rb'))
    p = np.uint32(m.predict(t.transform([text])))
    n = int(list(p)[0])
    return not bool(n)


@api.get("/check/{email}")
def returnData(email: str):
    return {
        "isSpam": predict(email)
    }
