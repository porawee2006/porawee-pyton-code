"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("Personal infomation validator")

name = input("Enter your name")
age = input("Enter your age")
phone_number = input("Enter your phone number")

nameflag = True
for char in name:
    if char.isalpha() or char == " ":
        nameflag = False
    else:
        nameflag = False

ageflag = True   
if int(age) < 18 or int(age) >65:
    ageflag = False

phoneflag = True 
if len(phone_number) != 10:
    phoneflag = False
else:
    for char in phone_number:
        if char .isdigit() == False:
           phoneflag = False
           break
print("validation results")
if nameflag:
    print("Name: Vaid (contaions only letter a nd spces)")
else:
    print("Name: Invaid (not contaions only letter a nd spces)")

if ageflag:
    print(f"Age: Vaid ({age} year old)")
else:
    print("Age: Invaid (less then 18 or more thae 65)")  

if phoneflag:
    print("phone: Vaid (10-digit number)")
else:
    print("phone: Invaid (not 10-digit number)")

print("formatter Information:")
print("Name: ",name.upper(), name.lover(), name.capital)
if int(age) >=18 and int(age) <=30:
    print("Age group: Young Adult (18-30)")
else:
    print("Age group: (not Adult)")

print("Phone +66-%s" % phone_number)