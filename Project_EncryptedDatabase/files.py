import os
from encryption import encrypt, decrypt
from database import add_file_metadata, get_file_metadata, delete_file_metadata
from config import ENCRYPTED_FILES_DIR

#make sure the encrypted files directory exists
os.makedirs(ENCRYPTED_FILES_DIR, exist_ok=True)

def encrypt_file(file_path, public_key):
    """encrypt a file and save it to the encrypted files directory"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} dont exist.")
    
    with open(file_path, 'r') as file:
        plaintext = file.read()

    # encrypt yhe content of a file
    encrypted_content = encrypt(plaintext, public_key)
    
    # save encripted content to a new file
    encrypted_file_path = os.path.join(ENCRYPTED_FILES_DIR, os.path.basename(file_path) + ".enc")
    with open(encrypted_file_path, 'w') as enc_file:
        enc_file.write(' '.join(map(str, encrypted_content)))

    # save metadata
    add_file_metadata(encrypted_file_path, "RSA", str(public_key))
    print(f"File '{file_path}' encrypted and saved as '{encrypted_file_path}'.")

def decrypt_file(file_path, private_key):
    """Decryt an encrypted file and display its content"""
    metadata = get_file_metadata(file_path)
    if not metadata:
        raise ValueError(f"No metadata found for file {file_path}.")

    with open(file_path, 'r') as enc_file:
        encrypted_content = list(map(int, enc_file.read().split()))

    # dcrypt content
    decrypted_content = decrypt(encrypted_content, private_key)
    print(f"Decrypted content of '{file_path}':\n{decrypted_content}")

def delete_encrypted_file(file_path):
    """Deletee an encrypted file and itsd metadata"""
    if os.path.exists(file_path):
        if file_path.endswith(".enc"):
            os.remove(file_path)
            print(f"Encrypted file '{file_path}' deleted.")
        else:
            print(f"File '{file_path}' is not an encrypted file.")
    else:
        print(f"File '{file_path}' does not exist.")

    # delete metadata
    delete_file_metadata(file_path)
