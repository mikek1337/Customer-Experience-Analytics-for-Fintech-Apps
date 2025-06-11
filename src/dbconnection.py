import oracledb 
import os

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
service_name = os.getenv('SERVICE_NAME')
connection = oracledb.connect(user=username, password=password, host=host,port=port, service_name=service_name)
cursor = connection.cursor()



def insert_review(data:list):
    sql_insert = "INSERT INTO REVIEW(REVIEW_ID, REVIEW_TEXT, RATING, SENTIMENT_LABEL, SENTIMENT, PROCESSED_REVIEW, IDENTIFIED_THEMES, BANK_ID) VALUES(:1, :2, :3, :4, :5, :6, :7, :8)"
    cursor.executemany(sql_insert, data)
    connection.commit()
    print('here')

def insert_bank(data:list):
    sql_insert = "INSERT INTO BANK(BANK_ID, BANK_NAME) VALUES(:1, :2)"
    cursor.executemany(sql_insert, data)
    connection.commit()
    print('there')