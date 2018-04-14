filename = "file.txt"

## Writing

file = open(filename, 'w')

for i in range(1, 11):
    file.write("This is line %i \n" % i)
file.close()


file = open(filename, 'r')

for line in file:
    print(line, end = '')
file.close()   