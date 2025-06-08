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
    """
    Analyzes the sentiment of the given text content using VADER sentiment analysis.

    Args:
        content (str): The text content to analyze.

    Returns:
        float: The compound sentiment score ranging from -1 (most negative) to 1 (most positive).
    """
    vader = SentimentIntensityAnalyzer()
    score = vader.polarity_scores(content)
    return score['compound']
