import google_play_scraper as gps
import pandas as pd
import json
import os

from datetime import datetime

class Scrapy:
    def __init__(self):
       pass

    def default_serializer(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")
        
    def get_data(self, app_id:str):
        reviews = gps.reviews_all(app_id)
        return reviews
    
    def save_data_json(self, path:str, filename:str, app_id:str):
        full_path = path + filename
        reviews = []
        if(os.path.isfile(full_path)==False and full_path != ''):
            reviews = self.get_data(app_id)
            with open(self.full_path, 'w', encoding='utf-8') as f:
                json.dump(reviews, f, default=self.default_serializer)
        else:
            print('Data already imported')
            return reviews

