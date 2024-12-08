import seed

def stream_users():
    connection = seed.connect_to_prodev()
    if connection and connection.is_connected():
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM user_data")
                for row in cursor:
                    yield row
        finally:
            if connection and connection.is_connected():
                connection.close()
                print("Connection closed")

for user in stream_users():
    print(user)

