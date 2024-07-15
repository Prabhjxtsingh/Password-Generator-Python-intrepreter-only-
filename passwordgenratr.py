import pandas as pd
import numpy as np
import string
import random
import os.path

generated_file_path = 'generated_passwords.csv'
custom_file_path = 'custom_passwords.csv'

# Create CSV files if they don't exist
for file_path in [generated_file_path, custom_file_path]:
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            f.write('Username,Password\n')

while True:
    print("1. Generate and save a password")
    print("2. Save a custom username and password")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        length = int(input("Enter the length of the password: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)
        data = {'Username': ['Generated'], 'Password': [password]}
        df = pd.DataFrame(data)
        df.to_csv(generated_file_path, mode='a', index=False, header=not os.path.getsize(generated_file_path) > 0)
        print("Password saved successfully!")

    elif choice == '2':
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        data = {'Username': [username], 'Password': [password]}
        df = pd.DataFrame(data)
        df.to_csv(custom_file_path, mode='a', index=False, header=not os.path.getsize(custom_file_path) > 0)
        print("Username and Password saved successfully!")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please choose again.")
