import psycopg2
from config import DB_CONFIG

def get_connection():
    """ 
    Establishes a connection to the database using the configuration provided in the DB_CONFIG dictionary.

    Returns:
        A connection to the database.
    """
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

def initialize_database():
    """
    Establishes a connection to the database, executes the SQL statement to create the table,
    commits the transaction, and then closes the connection.

    Columns in the 'file_metadata' table:
        - id: a unique identifier for each record (is a primary key).
        - file_path: path to the file (must be unique).
        - encryption_method: method used to encrypt the file.
        - encryption_key: key used when encrypt.
        - file_size: size of the file (in bytes).
        - file_type: type of the file.
        - timestamp: timestamp when the record was created.

    Returns:
        None
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_metadata (
            id SERIAL PRIMARY KEY,
            file_path TEXT NOT NULL UNIQUE,
            encryption_method TEXT NOT NULL,
            encryption_key TEXT NOT NULL,
            file_size BIGINT NOT NULL,
            file_type TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_or_update_file_metadata(file_path, encryption_method, encryption_key, file_size, file_type):
    """
    Add or update metadata for a specific file.

    Parameters:
        file_path (str): path to the file.
        encryption_method (str): method used to encrypt the file.
        encryption_key (str): key used for encryption.
        file_size(int): size of the file in bytes.
        file_type(str): type of the file.

    Returns:
        None
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO file_metadata (file_path, encryption_method, encryption_key, file_size, file_type)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (file_path) DO UPDATE SET
            encryption_method = EXCLUDED.encryption_method,
            encryption_key = EXCLUDED.encryption_key,
            file_size = EXCLUDED.file_size,
            file_type = EXCLUDED.file_type,
            timestamp = CURRENT_TIMESTAMP
    """, (file_path, encryption_method, encryption_key, file_size, file_type))
    conn.commit()
    cursor.close()
    conn.close()

def get_file_metadata(file_path):
    """
    Retrieves metadata for a specific file from the database.

    Parameters:
        file_path(str): The path of the file for which metadata is to be retrieved.

    Returns:
        tuple: A tuple containing the metadata of the file if found, otherwise None.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM file_metadata WHERE file_path = %s
    """, (file_path,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def delete_file_metadata(file_path):
    """
    Deletes metadata for a specific file from the database.
    
    Parameters:
        file_path(str): The path of the file for which metadata is to be deleted.
        
    Returns:
        None
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM file_metadata WHERE file_path = %s
    """, (file_path,))
    conn.commit()
    cursor.close()
    conn.close()