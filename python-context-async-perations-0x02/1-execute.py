import sqlite3

class ExecuteQuery():
    # Context Manager For Database Connection and also for query execution
    def __init__(self,database, query):
        # __init__ method for initializing the connection and the attrinute needed
        ConnectionInitialized = sqlite3.connect(
            database = database
        )
        self.query = query
        self.ConnectionInitialized = ConnectionInitialized
        
    def __enter__(self):
        cursor = self.ConnectionInitialized.cursor()
        cursor.execute(self.query)
        self.cursor = cursor
        return self.cursor

    def __exit__(self,exc_type, exc_value, exc_traceback):
        closedConnection = self.cursor.close()
        return closedConnection


query = "SELECT * FROM users WHERE age > 25"
with ExecuteQuery('users.db', query=query) as queried:
    for rows in queried:
        print(rows)
