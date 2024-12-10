import seed
import mysql.connector

def stream_users_in_batches(batch_size):
    query = f'''
                SELECT * FROM user_data LIMIT {batch_size};
            '''
    connection_to_database = seed.connect_to_prodev()
    try:
        if connection_to_database and connection_to_database.is_connected():
            with connection_to_database.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    yield row
    except mysql.connector.Error as err:
        return (f"Error is {err}")
            


def batch_processing(batch_size):
    query = f'''
                SELECT * FROM user_data WHERE user_data.age > 25 LIMIT {batch_size};
            '''
    connection_to_database = seed.connect_to_prodev()
    try:
        if connection_to_database and connection_to_database.is_connected():
            with connection_to_database.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    yield row
    except mysql.connector.Error as err:
        return (f"Error is {err}")


stream_users_in_batches(5)
batch_processing(5)