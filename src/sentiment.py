from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import nltk
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('wordnet')

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

def label_sentiment(sentiment):
    """
    Assigns a sentiment label based on the input sentiment score.

    Args:
        sentiment (float or int): The sentiment score to be labeled. 
            Positive values indicate positive sentiment, negative values indicate negative sentiment, and zero indicates neutral sentiment.

    Returns:
        str: A string label representing the sentiment:
            - 'positive' if sentiment > 0
            - 'negative' if sentiment < 0
            - 'neutral' if sentiment == 0
    """
    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'