# Collect user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio: ") 

# Create username (first initial + last name in lowercase)
username = (first_name[0] + last_name).lower() 

# Format full name in Title Case
full_name = f"{first_name} {last_name}".title() 

# Strip leading/traling whitespace from bio
clean_bio = bio.strip() 

# Count the number of characters in the cleaned bio
bio_length = len(clean_bio) 

# Replace "I am" with "I'm"
formatted_bio = clean_bio.replace("I am", "I'm")

# Display the formatted profile
print("\n===== USER PROFILE =====")
print(f"Full Name : {full_name}")
print(f"Username  : {username}") 
print(f"Bio       : {formatted_bio}")
print(f"Bio Length: {bio_length} character") 