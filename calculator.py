# Get two numbers from the user
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 

print("\n========== CALCULATOR RESULTS ==========") 
print(f"{'Operation':<20}{'Result'}") 
print("-" * 35) 

# Addition
print(f"{'Addition (+)':<20}{round(num1 + num2, 2)}") 

# Subtraction
print(f"{'Subtraction (-)':<20}{round(num1 - num2, 2)}")

# Multiplication
print(f"{'Multiplication (*)':<20}{round(num1 * num2, 2)}") 

# Division, Floor Division, and Modulus
if num2 == 0:
    print(f"{'Division (/)':<20}Error: Connot divide by zero.") 
    print(f"{'Floor Division (//)':<20}Error: Cannot divide by zero.") 
    print(f"{'Modulus (%)':<20}Error: Cannot divide by zero.") 
else: 
    print(f"{'Division (/)':<20}{round(num1 / num2, 2)}")
    print(f"{'Floor Division (//)':<20}{round(num1 // num2, 2)}") 
    print(f"{'Modulus (%)':<20}{round(num1 % num2, 2)}") 

print("=" * 35)