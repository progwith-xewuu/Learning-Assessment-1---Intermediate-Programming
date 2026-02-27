user = input("\nEnter Sentence: ").strip()

print(f"\nupper Case: {user}".upper())
print(f"upper Lower: {user}".lower())
print(f"title case: {user}".title())
print("letter 'a' appears:", user.count("a"))
print(f"Without extra spaces: {user}".strip())
print("With Underscore:", user.strip().replace(" ", "_"))

print("\n Splitted Sentence: ")
for word in user.strip().split():
    print(word)