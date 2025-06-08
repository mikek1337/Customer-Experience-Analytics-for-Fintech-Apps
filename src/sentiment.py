from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import nltk
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')

def sentiment_analysis(content):
    vader = SentimentIntensityAnalyzer()
    score = vader.polarity_scores(content)
    return score['compound']
