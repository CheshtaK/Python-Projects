# A dictionary is similar to a list. They are both collections
# of items but a dictionary has key and values (opposed to just
# values in a list). Think of a dictionary... well as a dictionary.
# You have some "key" (a word let's say) and you "lookup" that
# word in your handy-dandy dictionary to get the word's
# definition or "value".
wordsAndThingsDict = {}

# Add some things to the dictionary
wordsAndThingsDict['Apple'] = 'Red thing that tastes good. Specifically not an orange.'
wordsAndThingsDict['Orange'] = 'Makes great juice!'
wordsAndThingsDict[3] = 'The number 3'
wordsAndThingsDict['A list'] = ['Oh', 'boy!', 'A list in a dictionary!']
wordsAndThingsDict['Inception'] = {'Nested': 'When one dictionary is a VALUE in a dictionary'}

# Print out our dictionary
print(str(wordsAndThingsDict))
print()

print("Loop")
# Loop over all keys in the dictionary
for key in wordsAndThingsDict:
    print("Key: " + str(key))  # Call str to be safe... There is a number 3 in there
    # Print the value by using the key to "look it up"
    print("Value: " + str(wordsAndThingsDict[key]))
    print()