full_name = input("Enter your full name: ").strip()
birth_year = input("Enter your birth year: ").strip()

name_parts = full_name.split()

if len(name_parts) < 2:
    print("Error: Please enter at least a first and last name.")
else:
    first_name = name_parts[0].lower()
    last_name = name_parts[-1].lower()

    first_part = first_name[:3]
    last_part = last_name[:3]

    year_part = birth_year[-2:]

    username = first_part + last_part + year_part

    print("Generated username:", username)