# print("=== MOVIE TICKET SYSTEM ===")
# day = input("Day: ").lower()
# customer_type = input("Customer: ").lower()
# movie_time = int(input("Show time: "))
# num_ticket = int(input("Number of Tickets : "))

# if day == "weekday" or day == "weekend":
#     if customer_type == "regular" or customer_type == "student" or customer_type == "senior":
#         if 9 <= movie_time or movie_time <= 22:
#             if num_ticket > 0:
#                 if day == "weekday":
#                     baseprice = 200
#                 else:
#                     baseprice = 300
#                     subtotal = baseprice * num_ticket
#                     discount = 0
                
#                 if customer_type == "student":
#                     discount = subtotal * 0.20 #20% discount
#                     percent = "20%"  
#                 else: 
#                     customer_type == "senior"
#                     discount = subtotal * 0.30 #30% discount
#                     percent = "30%"
                    
                
#                     if num_ticket > 5:
#                         ticket_discount = num_ticket * 0.05
#                         percent = "5%"

#                 discount += subtotal * 0.10
                
#                 final_price = subtotal - discount

#                 print("\n=== RECEIPT ===")
#                 print(f"Base price: {baseprice:.2f} x {num_ticket} = {subtotal}")
#                 print(f"{customer_type} discount ({percent}): -{discount} ")

print("\n=== Movie Ticket System ===")

day = input("Enter Day: ").lower()
customer = input("Enter Customer Type: ").lower()
show_time = int(input("Enter Time: "))
num_ticket = int(input("Enter Number of Tickets: "))

print("\n--- Receipt ---")

if day == "weekday":
    price = 200.00 * num_ticket
    print(f"Base Price: 200.00 x {num_ticket} = {price}")
else: 
    day == "weekend"
    price = 300.00 * num_ticket
    print(f"Base Price: 300.00 x {num_ticket} = {price}")

    if customer == "student":
        discount = 0.20
        discounted_price = price * discount
        price = price - discounted_price
        print(f"Student Discount (20%): {discounted_price}")

    else:
        customer == "senior"
        discount = 0.30
        discounted_price = price * discount
        price = price - discounted_price
        print(f"Senior Discount (30%): {discounted_price}")

if show_time < 12:
    discount = 0.10
    discounted_price = price * discount
    price = price - discounted_price
    print(f"Matinee Discount (10%): {discounted_price}")

if  num_ticket >= 5:
    discount = 0.05
    discounted_price = price * discount
    price = price - discounted_price
    print(f"Group Discount (5%): {discounted_price}")

print(f"\nTOTAL: {price:.2f}")
print("Thank you for your purchese!")