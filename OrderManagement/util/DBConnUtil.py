import pyodbc

# Function to get the database connection
def get_db_connection():
    # Define the connection string
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=localhost;'          
        r'DATABASE=OrderManagementDB;' 
        r'Trusted_Connection=yes;'     
    )

    # Establish the connection
    try:
        conn = pyodbc.connect(conn_str)
        print("Connection successful!")
        return conn
    except pyodbc.Error as e:
        print("Error while connecting to SQL Server:", e)
        raise
