for number in range(1,11):
    print(number) 

print("-" * 50)

for i in range(2, 20 + 1, 2):
    print(i)

print("-" * 50)

basket = ['banana', 'apple', 'Pineapple', 'Manggo']
for index, fruit in enumerate(basket):
    print(f"{index}.{fruit}")

print("-" * 50)

count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

print("-" * 50)

print("--- Guess the name ---")
print("\nThe Word is: a_g_s\n")
word = "angas"
guess = ""

while True:
    guess = input("Enter your guess: ")
    if guess.lower() == word.lower():
        print("Congratulations! angas boi!")
        break
    else:
        print("Wrong! Try again.")