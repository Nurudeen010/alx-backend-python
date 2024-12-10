import seed

def stream_users_in_batches(batch_size=5):
    query = f'''
                SELECT * FROM user_data LIMIT {batch_size};
            '''
    connection_to_database = seed.connect_to_prodev()
    if connection_to_database and connection_to_database.is_connected():
        with connection_to_database.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            print(rows)
            #yield rows
            


def batch_processing(batch_size):
    query = f'''
                SELECT * FROM user_data WHERE user_data.age > 25 LIMIT {batch_size} OFFSET 10;
            '''
    connection_to_database = seed.connect_to_prodev()
    if connection_to_database and connection_to_database.is_connected():
        with connection_to_database.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)


#stream_users_in_batches()
batch_processing(4)