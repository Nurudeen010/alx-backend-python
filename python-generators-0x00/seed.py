import mysql.connector

def connect_db():
    try:
        newConnection = mysql.connector.connect(
        user='root', password = '@Olanej1996',
        host='localhost',
        allow_local_infile=True
        )
        print("Connected successfully")
        return newConnection
        
    except mysql.connector.Error as err:
            print(f"Error is {err}")
            return None

def create_database(connection=None):
    if connection == None:
        try:
            connection = connect_db()
            if connection and connection.is_connected():
                with connection.cursor() as cursor:
                    cursor.execute("CREATE DATABASE ALX_prodev")
                    print("Database created successfully")
        except mysql.connector.Error as err:
            print(f"Error is {err}")
        finally:
            if connection and connection.is_connected():
                connection.close()
                print("Connection is closed")

def connect_to_prodev():
    connection = connect_db()
    if connection and connection.is_connected():
        with connection.cursor() as cursor:
            cursor.execute("USE ALX_prodev")
            print("Connected to database successfully")
        return connection
            
    else:
        print("Database is not connected")

def create_table(connection=None):
    create_table_query = """
    CREATE TABLE user_data (
    user_id INT PRIMARY KEY,
    name VARCHAR(30),
    email VARCHAR(30) UNIQUE,
    age DECIMAL(10, 3)
    );
    """
    if connection == None:
        try:
            connection = connect_to_prodev()
            if connection and connection.is_connected():
                with connection.cursor() as cursor:
                    cursor.execute(create_table_query)
                    print("Table Created Successfully")
        
        except mysql.connector.Error as err:
            print(f"Error is {err}")

                

def insert_data(connection= None, data=None):
    
    if connection == None and data == None:
        try:
            data = 'alx-backend-python/python-generators-0x00/user_data.csv'
            query = f"""
            LOAD DATA LOCAL INFILE '{data}'
            INTO TABLE user_data
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n' 
            IGNORE 1 ROWS
            (user_id, name, email, age);
            """
            connection = connect_to_prodev()
            if connection and connection.is_connected():
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    print("Data Inserted successfully")
                    connection.commit()
                
        except mysql.connector.Error as err:
            print(f"Error is {err}")

connect_db()
create_database()
connect_to_prodev()
create_table()
insert_data()