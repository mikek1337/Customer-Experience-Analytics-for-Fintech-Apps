This script processes app review data for multiple banking apps. It performs the following steps:

1. Imports necessary modules and custom classes:
    - pandas for data manipulation.
    - sys for modifying the system path.
    - Scrapy (custom class) for scraping app reviews.
    - ConvertJSONToCsv (custom class) for converting JSON data to CSV format.

2. Defines a list of app IDs (`app_ids`) for which reviews will be processed.

3. For each app ID:
    - Uses Scrapy to scrape review data and save it as a JSON file.
    - Prints the number of reviews collected for each app.

4. Loads the JSON review data for each app and converts it to CSV using ConvertJSONToCsv.

5. Preprocesses the CSV data for each app:
    - Cleans the data using the `clean_data` function.
    - Adds 'bank' and 'source' columns.
    - Drops unnecessary columns.
    - Saves the cleaned data back to CSV.

6. Performs sentiment analysis on the review content for each app:
    - Loads the cleaned CSV data.
    - Drops rows with missing 'content'.
    - Applies the `sentiment_analysis` function to the 'content' column if the 'sentiment' column does not already exist.
    - Prints the first few rows of the resulting DataFrame.

Variables:
- app_ids: List of app package names to process.
- bank: The current bank being processed (derived from app_id).
- data: pandas DataFrame containing review data for the current bank.
- id: The current app_id being processed.

Note:
- Custom modules (`scrapy`, `convert_json_csv`, `preprocess`, `sentiment`) must be available in the specified paths.
- The script assumes the presence of review data in JSON format and writes/reads CSV files in the '../data/' directory.
