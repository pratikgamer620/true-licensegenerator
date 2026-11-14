#License Genrator Gamer
#Made by Pratik Kumar

import time
import random
import os


print("Welcome to True License Company!")
time.sleep(1)

print("Let's go ahead and get you a license!")
time.sleep(1)

while True:
    proceed = input("Do you want to proceed (yes/no)? ")
    if proceed.lower() == "yes":
        print("Great! Let's get started.")
        time.sleep(1)
        break
    elif proceed.lower() == "no":
        print("Understood. Have a great day!")
        exit()
    else:
        print("Please enter a valid response (yes/no).")

name = input("Please enter your full name as your government ID: ")
print(f"Thank you, {name}, for providing your name. Let's move on to the next step.")
time.sleep(1)

while True:
    age = input("Please enter your age: ")
    if int(age) < 18:
        print("Sorry, you must be at least 18 years old to obtain a license.")
        exit()
    elif int(age) > 18 or int(age) == 18:
        print("Great! You meet the age requirement for a license. Let's go ahead and move on to the next step.")
        break
    else:
        print("Please enter a valid age.")

while True:
    adhaar = input("Please enter your adhaar number: ")
    if len(adhaar) == 12 and adhaar.isdigit():
        print("Thank you for providing your adhaar number. Let's move on to the next step.")
        break
    else:
        print("Please enter a valid 12-digit adhaar number.")

while True:
    phone = input("Please enter your phone number: ")
    if len(phone) == 10 and phone.isdigit():
        print("Thank you for providing your phone number. Let's move on to the next step.")
        break
    else:
        print("Please enter a valid 10-digit phone number.")

while True:
    email = input("Please enter your email address: ")
    if "@" in email and "." in email:
        print("Thank you for providing your email address. Let's move on to the next step.")
        break
    else:
        print("Please enter a valid email address.")

while True:
    pan = input("Please enter your PAN number: ")
    if len(pan) == 10 and pan.isalnum():
        print("Thank you for providing your PAN number. Let's move on to the next step.")
        break
    else:
        print("Please enter a valid 10-character PAN number.")

while True:
    address = input("Please enter your address: ")
    if len(address) > 0:
        print("Thank you for providing your address. Let's move on to the next step.")
        break
    else:
        print("Please enter a valid address.")

while True:
    license_type = input("Please enter the type of license you are applying for (e.g., Driver's License, Business License, etc.): ")
    if len(license_type) > 0:
        print(f"Thank you for providing the license type: {license_type}. Let's move on to the next step.")
        break
    else:
        print("Please enter a valid license type.")

while True:
    license_duration = input("Please enter the duration of the license in years (e.g., 1, 2, 3, etc.): ")
    if license_duration.isdigit() and int(license_duration) > 0:
        print(f"Thank you for providing the license duration: {license_duration} years. Let's move on to the next step.")
        break
    else:
        print("Please enter a valid duration in years.")


def get_unique_10_digit_code():
    file_name = "used_codes.txt"
    
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            used_codes = file.read().splitlines()
    else:
        used_codes = []

    while True:
        new_code = str(random.randint(1000000000, 9999999999))
        
        if new_code not in used_codes:
            with open(file_name, "a") as file:
                file.write(new_code + "\n")
            
            return new_code

final_code = get_unique_10_digit_code()
print("You unique 10-digit license code is:", final_code)


