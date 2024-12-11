import seed
import mysql.connector
from decimal import Decimal

def stream_user_ages():
    query = '''
        SELECT age from user_data;
    '''
    connect_to_database = seed.connect_to_prodev()
    try:
        if connect_to_database and connect_to_database.is_connected():
            with connect_to_database.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    age = row[0]
                    yield age
    except mysql.connector.Error as err:
        return (f"Error is {err}")

def check_average_age():
    result_from_query = stream_user_ages()
    Ages = [item for item in result_from_query if item is not None]
    average = sum(Ages)/ len(Ages)
    return average
    




print(check_average_age())