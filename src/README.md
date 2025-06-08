# Customer Experience Analytics for Fintech Apps

This project provides tools and scripts for collecting, converting, cleaning, and analyzing customer review data from fintech mobile apps. The workflow is designed to support end-to-end data processing, from scraping app reviews to performing sentiment analysis.

## Structure

- **src/scrapy.py**  
  Contains the [`Scrapy`](src/scrapy.py) class for scraping reviews from Google Play using `google_play_scraper`.  
  - `get_data(app_id)`: Fetches all reviews for a given app.
  - `save_data_json(path, filename, app_id)`: Saves reviews as a JSON file, with custom datetime serialization.

- **src/convert_json_csv.py**  
  Contains the [`ConvertJSONToCsv`](src/convert_json_csv.py) class for converting JSON review data to CSV format.  
  - `to_csv(json, filename)`: Writes a list of review dictionaries to a CSV file in the `../data/` directory.

- **src/preprocess.py**  
  Provides data cleaning and preprocessing utilities:
  - `find_and_replace_outliers_with_median(df, cols, threshold=3)`: Replaces outliers in specified columns with the median.
  - `find_columns_with_missing_value(df, threshold)`: Identifies columns with excessive missing values.
  - `normalize_date(df, date_col)`: Normalizes date columns.
  - `clean_data(df)`: Cleans the DataFrame, drops columns with too many missing values, and normalizes dates.
  - `drop_column(df, cols)`: Drops specified columns from a DataFrame.

- **src/sentiment.py**  
  Provides sentiment analysis using NLTK's VADER:
  - `sentiment_analysis(content)`: Returns the compound sentiment score for a given text.

## Typical Workflow

1. **Scrape Reviews**  
   Use [`Scrapy`](src/scrapy.py) to fetch and save reviews for each app as JSON.

2. **Convert to CSV**  
   Use [`ConvertJSONToCsv`](src/convert_json_csv.py) to convert JSON files to CSV format.

3. **Preprocess Data**  
   Use functions from [`preprocess.py`](src/preprocess.py) to clean and prepare the data for analysis.

4. **Sentiment Analysis**  
   Use [`sentiment_analysis`](src/sentiment.py) to compute sentiment scores for review content.

## Example Usage

```python
from scrapy import Scrapy
from convert_json_csv import ConvertJSONToCsv
from preprocess import clean_data
from sentiment import sentiment_analysis

# Scrape and save reviews
scraper = Scrapy()
scraper.save_data_json('../data/', 'data-com.boa.boaMobileBanking.json', 'com.boa.boaMobileBanking')

# Convert JSON to CSV
converter = ConvertJSONToCsv()
with open('../data/data-com.boa.boaMobileBanking.json') as f:
    import json
    reviews = json.load(f)
    converter.to_csv(reviews, 'boa.csv')

# Preprocess and analyze
import pandas as pd
df = pd.read_csv('../data/boa.csv')
df_clean = clean_data(df)
df_clean['sentiment'] = df_clean['content'].apply(sentiment_analysis)