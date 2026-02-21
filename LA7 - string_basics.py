user = str(input("\nFull name here: "))
print("\nYour first name character is", user[:1], "and your last character is",  user[-1])
print("First Five Chracter:", user[:5])
print("Reverse Name:", user[::-1])
print("Every other character of the name:", user[::2])

length = len(user)
if length % 2 == 0:
    middle_character = user [length//2-1:length//2+1]

else:
    middle_character = user [length//2]

print("Middle Chracter:", middle_character,"\n")    
