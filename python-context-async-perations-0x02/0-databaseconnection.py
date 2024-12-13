import sqlite3

#
class DatabaseConnection():
    def __init__(self, database):
        Opening = sqlite3.connect(
            database=database
        )
        self.Opening = Opening
        
    def __enter__(self):
        return self.Opening

    def __exit__(self, exc_type, exc_value, exc_traceback):
        ConnectionClosed = self.Opening.close()
        return ConnectionClosed
    
with DatabaseConnection('users.db') as connected:
    cursor = connected.cursor()
    cursor.execute("SELECT * FROM users")
    for rows in cursor:
        print(rows)
    