# def display_info():
#     print("Hello, baby")
#     return 'success', 100, 99.99
    
# result, score, price = display_info()
# print(result)
# print(score)
# print(price)

# taon_today = 2025
# def compute_age(birth_year, year_today):
#     global taon_today
#     taon_today = 2027
#     print(f"taon today: {taon_today}\nYear Today: {year_today}")
#     return year_today - birth_year
    
# print(compute_age(2006, 2026))
# print(taon_today)

def print_pyramid(levels, current=1):
    if current > levels:
        return

    def print_spaces(count):
        if count == 0:
            return
        print(' ', end='')
        print_spaces(count - 1)

    def print_stars(count):
        if count == 0:
            return
        print('*', end='')
        if count > 1:
            print(' ', end='')
        print_stars(count - 1)

    print_spaces(levels - current)
    print_stars(current)
    print()
    print_pyramid(levels, current + 1)

base = int(input("how many is the base start?: "))
print_pyramid(base)
print(f"done pyramid with {base} * base")
