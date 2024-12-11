import time
import sqlite3 
import functools

def with_db_connection(func):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect("users.db")
            return func(connection, *args, **kwargs)
        finally:
            connection.close()
    return wrapper

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        def retryWrapper(*args, **kwargs):
            for attempt in range(1, retries+1):
                try:
                    return func(*args, *kwargs)
                except sqlite3.Error as err:
                    print(f"Error is {err}")
                    if attempt < retries:
                        time.sleep(delay)
                    else:
                        print("All retry attempts failed")
        return retryWrapper
    return decorator
            

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()    

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)