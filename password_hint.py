# Ask the user to enter their secret password
password = input("Enter your secret password: ") 

# Remove any accidental spaces at the beginning or end
password = password.strip() 

# Get the first and last letters
first_letter = password[0]
last_letter = password[-1] 

# Display the password hint in uppercase
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}.") 