import random

VOWELS = ("a", "e", "i", "o", "u")

message = input("Enter your message")
new_message = ""

for letter in message:
    if letter not in VOWELS:
        new_message += letter
    else:
        temp = random.choice(VOWELS)
        while temp == letter:
            temp = random.choice(VOWELS)
        else:
            new_message += temp

print(new_message)