from encryption import gen_keys
from files import encrypt_file, decrypt_file, delete_encrypted_file
from database import initialize_database
import emoji


def main():
    # initialize database
    initialize_database()

    #generate RSA keys
    public_key, private_key = gen_keys()
    # print("Public Key:", public_key)
    # print("Private Key:", private_key)

    while True:
        print("\nOptions:")
        print("1.",emoji.emojize(":locked:"),"Encrypt and store a file")
        print("2.",emoji.emojize(":unlocked:"),"Decrypt and display a file")
        print("3.",emoji.emojize(":wastebasket:"),"Delete an encrypted file")
        print("4.",emoji.emojize(":door:"),"Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the local path of the file to encrypt: ")
            try:
                encrypt_file(file_path, public_key)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            file_path = input("Enter the local path of the encrypted file to decrypt: ")
            try:
                decrypt_file(file_path, private_key)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            file_path = input("Enter the local path of the encrypted file to delete: ")
            try:
                delete_encrypted_file(file_path)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Exiting...Bye Bye", emoji.emojize(":waving_hand:"))
            break
        else:
            print("Invalid choice. Please try again.")

# Main
if __name__ == "__main__":
    main()
