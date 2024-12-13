import sqlite3, mysql.connector


class DatabaseConnection():
    # Context manager for database connection
    def __init__(self, database):
        # __init__ method to initialize the connection attribute
        Opening = sqlite3.connect(
            database=database
        )
        self.Opening = Opening
        
    def __enter__(self):
        # Returns the connection only if it successfully connected
        return self.Opening

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Closes the connection after the completion of the operation
        ConnectionClosed = self.Opening.close()
        return ConnectionClosed
    
with DatabaseConnection('users.db') as connected:
    cursor = connected.cursor()
    cursor.execute("SELECT * FROM users")
    for rows in cursor:
        print(rows) # Print the value based on the query executed above


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
