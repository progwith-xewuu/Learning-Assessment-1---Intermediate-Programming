user_age = int(input("Your Age: "))
valid_id = input("Do you have a valid ID? yes/no: ")
has_id = valid_id == "yes"

if user_age >= 18 and has_id:
    print("Eligible")
else:
    print("Not Eligble")
if user_age >= 60:
    print("You have a Senior Discount")

# user_age = int(input("Your Age: "))
# valid_id = input("You have Valid ID? (yes/no): ").lower() 
# if user_age >= 18 and valid_id == "yes":
#     print("Eligible")
# else:
#     print("Not Eligble")
# if user_age >= 60:
#     print("You have a Senior Discount.")

#ZYLK MANDOLADO 