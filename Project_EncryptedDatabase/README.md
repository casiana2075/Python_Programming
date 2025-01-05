# File Encryption System

A secure file encryption system using RSA encryption algorithm with PostgreSQL metadata storage.

## Project Overview

This project implements a file encryption system that allows users to:
- Encrypt and store files using RSA encryption
- Decrypt and display encrypted files
- Delete encrypted files and their associated metadata
- Store file metadata in a PostgreSQL database

## Installation Requirements

```
pip install psycopg2-binary
pip install emoji
```

## Configuration

The database system is managed through `config.py`:

```python
# Directory for encrypted files storage
ENCRYPTED_FILES_DIR = os.path.join(os.getcwd(), "encrypted_files")

# Database configuration
DB_CONFIG = {
    "host": "your_host",
    "port": your_port,
    "database": "your_database_name",
    "user": "your_username",
    "password": "your_password"
}
```

## Project Structure

### Main Components

1. `main.py`: Entry point of the application providing a command-line interface
2. `config.py`: Configuration settings for file storage and database connection
3. `database.py`: PostgreSQL database operations and metadata management
4. `encryption.py`: RSA encryption/decryption implementation
5. `files.py`: File handling operations including encryption, decryption, and deletion

### Database Schema

The system uses a PostgreSQL table `file_metadata` with the following structure:

```sql
CREATE TABLE file_metadata (
    id SERIAL PRIMARY KEY,
    file_path TEXT NOT NULL UNIQUE,
    encryption_method TEXT NOT NULL,
    encryption_key TEXT NOT NULL,
    file_size BIGINT NOT NULL,
    file_type TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Core Functionality

### Encryption Implementation

The system uses RSA encryption with the following key features:
- Dynamically generate prime numbers to later generate keys
- Generate public/private key pair
- Base64 encoding for binary file handling
- Support for multiple file types (.txt, .img, .png, .jpg, .pdf)

### File Operations

1. Encryption Process:
   - Validates file existence and type
   - Reads and encodes file content
   - Applies RSA encryption
   - Stores encrypted file with .enc extension
   - Records metadata in database

2. Decryption Process:
   - Validates metadata existence
   - Decrypts content using private key
   - Decodes from base64
   - Creates decrypted file with original extension and content

3. Deletion Process:
   - Validates file extension (.enc)
   - Removes encrypted file
   - Deletes associated metadata

## Usage

Run the application using:

```bash
python main.py
```

The interactive menu provides four options:
1. 🔒 Encrypt and store a file
2. 🔓 Decrypt and display a file
3. 🗑️ Delete an encrypted file
4. 🚪 Exit


## Error Handling

The system implements comprehensive error handling for:
- File operations (FileNotFoundError)
- Database connections
- Encryption/decryption processes
- Invalid file types
- Metadata management

## Security Considerations

- RSA key pairs are generated uniquely for each session
- Encrypted files are stored separately from original files
- Database credentials should be properly secured in production
- File metadata is tracked for audit purposes

## Limitations

- Supports only specific file extensions
- Keys are session-based and not persisted
- Basic command-line interface
- Local file system storage only
