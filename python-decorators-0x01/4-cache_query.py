import time
import sqlite3 
import functools


query_cache = {}
def with_db_connection(func):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect("users.db")
            return func( connection, *args, **kwargs)
        finally:
            connection.close()
    return wrapper

def cache_query(func):
    def cacheWrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Releasing the catched query now")
            return query_cache[query]
        else:
            print("Executing query result and caching")
            result = func(conn, query, *args, **kwargs)
            query_cache[query] = result
            return result
    return cacheWrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")