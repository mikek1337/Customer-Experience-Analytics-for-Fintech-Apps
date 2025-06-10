from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk


def TF_IDF(content:str):
    """
    Calculates and prints the TF-IDF (Term Frequency-Inverse Document Frequency) scores for each word in each document.

    Args:
        content (str): A list of documents (strings) to analyze.

    Returns:
        None

    Prints:
        For each document, prints the TF-IDF score of each word in the document.
    """
    vectorize = TfidfVectorizer()
    vectors = vectorize.fit_transform(content)
    feature_names = vectorize.get_feature_names_out()
    for i, doc in enumerate(content):
        print(f"Document {i+1}:")   
        for col, score in enumerate(vectors[i]):     
            print(f"\tWord: {feature_names[col]} - TF-IDF Score: {score:.4f}") 


def stemming(content:str):
    """
    Lemmatizes the given text content using WordNetLemmatizer.

    Args:
        content (str): The text to be lemmatized.

    Returns:
        str: The lemmatized form of the input text.
    """
    lem = WordNetLemmatizer()
    return lem.lemmatize(content)

def tokenize_content(content:str)->list:
    """
    Tokenizes the input text content into a list of words using the English language tokenizer.

    Args:
        content (str): The text content to be tokenized.

    Returns:
        list: A list of word tokens extracted from the input content.
    """
    return word_tokenize(content, 'english')

def remove_stopwords(words:list):
    """
    Removes English stopwords from a list of words.

    Args:
        words (list): A list of words (strings) to filter.

    Returns:
        str: A single string containing the words from the input list with stopwords removed, joined by spaces.

    Note:
        Requires the NLTK stopwords corpus to be downloaded.
    """
    stop_words = set(stopwords.words('english'))
    content = [w for w in words if not w.lower() in stop_words]
    return ' '.join(content)

def perprocess(content:str):
    """
    Preprocesses the input text by applying stemming, tokenization, and stopword removal.

    Args:
        content (str): The input text to preprocess.

    Returns:
        list: A list of tokens after stemming and stopword removal.
    """
    stemmed = stemming(content)
    tokenize = tokenize_content(stemmed)
    final = remove_stopwords(tokenize)
    return final

def get_top_words_for_topics(model, feature_names, n_top_words):
    """
    Extracts the top words for each topic from an LDA model.

    Args:
        model: Trained LatentDirichletAllocation model.
        feature_names: List of feature names from the TF-IDF vectorizer.
        n_top_words: Number of top words to extract for each topic.

    Returns:
        A dictionary where keys are topic indices and values are lists of top words.
    """
    identified_themes = {}
    for topic_idx, topic in enumerate(model.components_):
        # Get the indices of the top words for the current topic
        top_words_indices = topic.argsort()[:-n_top_words - 1:-1]
        # Get the actual words using their indices
        top_words = [feature_names[i] for i in top_words_indices]
        identified_themes[f"Topic #{topic_idx + 1}"] = top_words
    return identified_themes