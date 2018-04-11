VOWELS = ("a","e","i","o","u")  #Tuple

message = input("Enter your message")
new_message = ""

for letter in message:
    if letter not in VOWELS:
        new_message += letter

    # if letter in VOWELS:
        # print(letter, " is a vowel.")

print(new_message)