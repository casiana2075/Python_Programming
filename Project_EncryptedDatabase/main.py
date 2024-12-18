from encryption import gen_keys, encrypt, decrypt

if __name__ == "__main__":
    print("Generating RSA keys...")
    public_key, private_key = gen_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter a message to encrypt: ")
    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)