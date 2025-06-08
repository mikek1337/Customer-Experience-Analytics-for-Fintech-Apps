import google_play_scraper as gps
import pandas as pd
import json
import os

from datetime import datetime

class Scrapy:
    """
    Scrapy class for retrieving and saving app review data.
    Methods
    -------
    __init__():
        Initializes the Scrapy instance.
    default_serializer(obj):
        Serializes datetime objects to ISO format for JSON encoding.
        Raises TypeError for unsupported types.
    get_data(app_id: str):
        Retrieves all reviews for the specified app ID using the gps module.
    save_data_json(path: str, filename: str, app_id: str):
        Saves app reviews as a JSON file at the specified path and filename.
        If the file already exists, skips download and prints a message.
    """
    def __init__(self):
       pass

    def default_serializer(self, obj):
        """
        Serializes objects for JSON encoding.

        If the object is a datetime instance, it returns its ISO 8601 string representation.
        Raises a TypeError for objects that are not serializable by this method.

        Args:
            obj: The object to serialize.

        Returns:
            str: The ISO 8601 string representation of a datetime object.

        Raises:
            TypeError: If the object type is not serializable by this method.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")
        
    def get_data(self, app_id:str):
        """
        Retrieves all reviews for the specified app from the Google Play Store.

        Args:
            app_id (str): The unique identifier of the app whose reviews are to be fetched.

        Returns:
            list: A list of review objects for the specified app.
        """
        reviews = gps.reviews_all(app_id)
        return reviews
    
    def save_data_json(self, path:str, filename:str, app_id:str):
        """
        Saves review data as a JSON file for a given app ID if the file does not already exist.

        Args:
            path (str): The directory path where the file will be saved.
            filename (str): The name of the JSON file to save the data.
            app_id (str): The application ID for which to fetch and save review data.

        Returns:
            list: The list of reviews fetched and saved if the file did not exist, 
                  or an empty list if the file already exists.

        Notes:
            - Uses self.get_data(app_id) to fetch review data.
            - Uses self.default_serializer for JSON serialization.
            - Prints a message if the data has already been imported.
        """
        full_path = path + filename
        reviews = []
        if(os.path.isfile(full_path)==False and full_path != ''):
            reviews = self.get_data(app_id)
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(reviews, f, default=self.default_serializer)
        else:
            print('Data already imported')
            return reviews

