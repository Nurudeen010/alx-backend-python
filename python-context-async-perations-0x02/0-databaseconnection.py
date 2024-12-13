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
