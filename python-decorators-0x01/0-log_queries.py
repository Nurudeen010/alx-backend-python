import sqlite3
from datetime import datetime
#### decorator to log SQL queries
def log_queries(func):
    def wrapper(*args, **kwargs):
        print(f'''The query is: {kwargs}\n
              time is {datetime.hour}
              ''')
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


fetch_all_users(query="SELECT * FROM user_data limit 4")