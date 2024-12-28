import os

#directory in which i have the encrypted files
ENCRYPTED_FILES_DIR = os.path.join(os.getcwd(), "encrypted_files")

#db data to connect
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "STUDENT"
}