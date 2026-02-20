while True:

    print("\n=== Movie Ticket System ===")

    day = input("Day(weekday/weekend): ").lower().strip()
    customer = input("Customer Type(Regular/Student/Senior): ").lower().strip()
    show_time = int(input("Time(hour in 24-hour format): "))
    num_ticket = int(input("Number of Tickets: "))

    print("\n--- Receipt ---")

    if day == "weekday":
        price = 200.00 * num_ticket
        print(f"Base Price: 200.00 x {num_ticket} = {price:.2f}")
    else: 
        day == "weekend"
        price = 300.00 * num_ticket
        print(f"Base Price: 300.00 x {num_ticket:.2f} = {price}")

        if customer == "regular":
            discount = 0
            discounted_price = price * discount
            price = price - discounted_price
            print(f"Regular: {discounted_price:.2f}")

        if customer == "student":
            discount = 0.20
            discounted_price = price * discount
            price = price - discounted_price
            print(f"Student Discount (20%): {discounted_price:.2f}")

        
        if customer == "senior":
            discount = 0.30
            discounted_price = price * discount
            price = price - discounted_price
            print(f"Senior Discount (30%): {discounted_price:.2f}")

    if show_time < 12:
        discount = 0.10
        discounted_price = price * discount
        price = price - discounted_price
        print(f"Matinee Discount (10%): {discounted_price:.2f}")

    if  num_ticket >= 5:
        discount = 0.05
        discounted_price = price * discount
        price = price - discounted_price
        print(f"Group Discount (5%): {discounted_price:.2f}")

    print(f"\nTOTAL: {price:.2f}")
    print("Thank you for your purchese!")
    print("\n-------------------------------")

    again = input("\nDo you want to make another transaction? (yes/no): ").lower().strip()
    if again != "yes".lower().strip():
        print("Thank you for your purchese! Come Again!")
        break



# print("\n=== Movie Ticket System ===")

# day = input("Day(weekday/weekend): ").lower().strip()
# customer = input("Customer Type(Regular/Student/Senior): ").lower().strip()
# show_time = int(input("Time(hour in 24-hour format): "))
# num_ticket = int(input("Number of Tickets: "))

# print("\n--- Receipt ---")

# if day == "weekday":
#     price = 200.00 * num_ticket
#     print(f"Base Price: 200.00 x {num_ticket} = {price:.2f}")
# else: 
#     day == "weekend"
#     price = 300.00 * num_ticket
#     print(f"Base Price: 300.00 x {num_ticket:.2f} = {price}")

#     if customer == "regular":
#         discount = 0
#         discounted_price = price * discount
#         price = price - discounted_price
#         print(f"Regular: {discounted_price:.2f}")

#     if customer == "student":
#         discount = 0.20
#         discounted_price = price * discount
#         price = price - discounted_price
#         print(f"Student Discount (20%): {discounted_price:.2f}")

        
#     if customer == "senior":
#         discount = 0.30
#         discounted_price = price * discount
#         price = price - discounted_price
#         print(f"Senior Discount (30%): {discounted_price:.2f}")

# if show_time < 12:
#     discount = 0.10
#     discounted_price = price * discount
#     price = price - discounted_price
#     print(f"Matinee Discount (10%): {discounted_price:.2f}")

# if  num_ticket >= 5:
#     discount = 0.05
#     discounted_price = price * discount
#     price = price - discounted_price
#     print(f"Group Discount (5%): {discounted_price:.2f}")

#     print(f"\nTOTAL: {price:.2f}")
#     print("Thank you for your purchese!")
#     print("\n-------------------------------")
