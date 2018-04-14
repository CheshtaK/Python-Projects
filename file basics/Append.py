filename = "file.txt"

file = open(filename, 'a')

for i in range(0, 5):
    name = input("Enter a name: ")
    file.write(name + "\n")

file.close()
