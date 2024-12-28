import psycopg2
from config import DB_CONFIG

def get_connection():
    """Return a connection to the database."""
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
    """Create table file_metadata if not exists"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_metadata (
            id SERIAL PRIMARY KEY,
            file_path TEXT NOT NULL,
            encryption_method TEXT NOT NULL,
            encryption_key TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_file_metadata(file_path, encryption_method, encryption_key):
    """Add metadata for a specific file."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO file_metadata (file_path, encryption_method, encryption_key)
        VALUES (%s, %s, %s)
    """, (file_path, encryption_method, encryption_key))
    conn.commit()
    cursor.close()
    conn.close()

def get_file_metadata(file_path):
    """Return metadata for a specific file."""
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
    """Delete metadata for a specific file."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM file_metadata WHERE file_path = %s
    """, (file_path,))
    conn.commit()
    cursor.close()
    conn.close()
