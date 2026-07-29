# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Combine first name and surname
full_name = f"{first_name} {surname}"

# Display greeting
print(f"\nWelcome, {full_name}!")

# Display name in different formats
print(f"Name in UPPERCASE: {full_name.upper()}")
print(f"Name in Titel Case: {full_name.title()}")

# Calculate age in months
age_in_months = age * 12
print(f"Age in months: {age_in_months}")

# Round favourite number to 2 decimal places
rounded_number = round(favourite_number, 2)
print(f"Favourite number (round): {rounded_number}")

# Display data types
print("\nData Types: ")
print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}")
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_number)}")