import random

string = "the quick brown fox jumped over the lazy dogs"
string = list(string)
jumbled = " "

print(string)

for letter in range(0, len(string)):
    jumbled += string.pop(random.randint(0,len(string) - 1))

print(string)
print(jumbled)
