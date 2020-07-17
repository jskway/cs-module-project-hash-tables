# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

## Most frequent letters in English, sorted by highest frequency, desc
most_frequent_letters = (
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
)


# Open the file and read the words
with open("ciphertext.txt") as f:
    words = f.read()

# Split the words into a list
words_list = words.split()

# Set up a hash table to track letter counts
letter_counts = {}

# Iterative through the words
for word in words_list:
    # Iterative through each character
    for char in word:
        # If the char is alphabetical 
        if char.isalpha():
            # Initialize or increment the count
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] += 1
        # Skip non alphabetical chars
        else:
            continue

# Get a list of tuples (letter: count) in a list
letter_counts_items = list(letter_counts.items())

# Sort the list by count, in descending order
letter_counts_items.sort( key = lambda pair: pair[1], reverse=True )

# Store our keys to decode
keys = {}

# Iterate through the list of letter count tuples
for num in range(len(letter_counts_items)):
    # Map each ciphertext letter to it's decoded letter, based on frequency
    keys[letter_counts_items[num][0]] = most_frequent_letters[num]

def decode(s):
    new_str = ''

    for char in s:
        if char.isalpha():
            new_str += keys[char]
        else:
            new_str += char

    return new_str

# Map the list of ciphertext words to their decoded versions
decoded_words = map(decode, words_list)

# Join the decoded words back into a string
print(' '.join(decoded_words))


