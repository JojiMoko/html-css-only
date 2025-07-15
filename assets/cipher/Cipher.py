from cryptography.fernet import Fernet
from getpass import getpass
import json
import os

def generate_key():
    return Fernet.generate_key()

def load_key(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return file.read()
    else:
        key = generate_key()
        with open(filename, 'wb') as key_file:
            key_file.write(key)
        return key
def load_passwords(filename, cipher):
    if os.path.exists(filename):  
        with open(filename, 'rb') as file:
            encrypted_data = file.read()  
            decrypted_data = cipher.decrypt(encrypted_data)  
            return json.loads(decrypted_data.decode())  
    return {} 
def save_passwords(filename, cipher, passwords):
    with open(filename, 'wb') as file:
        
        encrypted_data = cipher.encrypt(json.dumps(passwords).encode())
        file.write(encrypted_data)  
def main():
    key_filename = 'secret.key' 
    key = load_key(key_filename) 
    cipher = Fernet(key)  
    filename = 'passwords.json'  
    passwords = load_passwords(filename, cipher)

    while True: 
        action = input("Enter 'add' to store a password, 'get' to retrieve a password, 'empty' to clear all passwords, or 'exit' to quit:\n").strip().lower()

        if action == 'add':  
            service = input("Enter the service name:\n").strip()  
            password = getpass("Enter your password:\n").strip() 

            passwords[service] = password  
            save_passwords(filename, cipher, passwords)  
            print(f"Password for '{service}' added successfully.") 

        elif action == 'get':  
            service = input("Enter the service name to retrieve the password:\n").strip()  

            if service in passwords:  
                print(f"Password for '{service}': {passwords[service]}") 
            else:
                print(f"No password found for '{service}'.")  

        elif action == 'empty': 
            passwords.clear() 
            save_passwords(filename, cipher, passwords) 
            print("All passwords have been cleared.") 

        elif action == 'exit': 
            print("Exiting the program.") 
            break 

        else:  
            print("Invalid command. Please try again.")  
if __name__ == "__main__":
    main()  
