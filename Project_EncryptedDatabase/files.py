import os
import base64
from encryption import encrypt, decrypt
from database import add_or_update_file_metadata, get_file_metadata, delete_file_metadata
from config import ENCRYPTED_FILES_DIR

#make sure the encrypted files directory exists
os.makedirs(ENCRYPTED_FILES_DIR, exist_ok=True)

def encrypt_file(file_path, public_key):
    """encrypt a file and save it to the encrypted files directory"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} dont exist.")
    
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    # Encode the binary data to base64
    plaintext_base64 = base64.b64encode(plaintext).decode('utf-8')

    # Encrypt the content of the file
    encrypted_content = encrypt(plaintext_base64, public_key)
    
    # save encripted content to a new file
    encrypted_file_path = os.path.join(ENCRYPTED_FILES_DIR, os.path.splitext(os.path.basename(file_path))[0] + ".enc")
    with open(encrypted_file_path, 'w') as enc_file:
        enc_file.write(' '.join(map(str, encrypted_content)))

    # get file size and type
    file_size = os.path.getsize(file_path)
    file_type = os.path.splitext(file_path)[1]

    # save metadata
    add_or_update_file_metadata(encrypted_file_path, "RSA", str(public_key), file_size, file_type)
    print(f"File '{os.path.basename(file_path)}' encrypted and saved as '{os.path.basename(encrypted_file_path)}'.")

def decrypt_file(file_path, private_key):
    """Decryt an encrypted file and display its content"""
    metadata = get_file_metadata(file_path)
    if not metadata:
        raise ValueError(f"No metadata found for file {file_path}.")

    with open(file_path, 'r') as enc_file:
        encrypted_content = list(map(int, enc_file.read().split()))

    # dcrypt content
    decrypted_base64 = decrypt(encrypted_content, private_key)

    # decode from base64 to binary
    decrypted_content = base64.b64decode(decrypted_base64)

    # save decrypted content to a new file (usefull for images, pdfs)
    decrypted_file_path = os.path.splitext(file_path)[0] + "_decrypted" + metadata[5]
    with open(decrypted_file_path, 'wb') as dec_file:
        dec_file.write(decrypted_content)
    try:
        print(f"Decrypted content of '{os.path.basename(file_path)}':\n{decrypted_content}")
    except UnicodeDecodeError:
        ProcessLookupError(f"See decrypted content of '{os.path.basename(file_path)}' saved as '{os.path.basename(decrypted_file_path)}'.")

def delete_encrypted_file(file_path):
    """Deletee an encrypted file and itsd metadata"""
    if os.path.exists(file_path):
        if file_path.endswith(".enc"):
            os.remove(file_path)
            print(f"Encrypted file '{os.path.basename(file_path)}' deleted.")
        else:
            print(f"File '{os.path.basename(file_path)}' is not an encrypted file.")
    else:
        print(f"File '{os.path.basename(file_path)}' does not exist.")

    # delete metadata
    delete_file_metadata(os.path.basename(file_path))
