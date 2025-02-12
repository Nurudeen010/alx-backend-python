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

def transactional(func):
    def anotherWrapper(conn, *args, **kwargs):
        try:
            conn.commit()
            print("Commited succesfully")
            return func(conn, *args, **kwargs)
        except sqlite3.Error as err:
            conn.rollback()
            print(f"The error is {err}")
        
    return anotherWrapper



@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
