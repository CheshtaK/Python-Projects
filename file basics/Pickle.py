import pickle

grades = {'andy': ['A', 'A', 'B'],
          'laura': ['B', 'B', 'A'],
          'sam': ['A', 'B', 'C']}

grades['andy'][-1] = 'A*'

filename = "grades.txt"
file = open(filename, 'wb')
pickle.dump(grades, file)

file = open(filename, 'rb')
new_grades = pickle.load(file)

print("Andy's grades: ", new_grades['andy'])


