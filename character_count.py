import pprint

# Define the message
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# Initialize a dictionary to count character occurrences
count = {}

# Count the occurrences of each character in the message
for character in message:
    count[character] = count.get(character, 0) + 1

# Print the character count using pprint for better readability
print("Character count (plain print):")
print(count)

print("\nCharacter count (pretty print):")
pprint.pprint(count)
