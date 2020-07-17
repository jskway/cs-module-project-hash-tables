# Read in all the words
with open("robin.txt") as f:
    words = f.read()

# characters to ignore
to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'

histogram = {}

# Split the words into a list
words_list = words.split()
longest = 0


for word in words_list:
    # Convert the word to lowercase and strip out invalid chars
    word = word.lower().strip(to_ignore)

    # Keep track of the longest word
    if len(word) > longest:
        longest = len(word)

    if word not in histogram:
        # Skip to next word if string is empty
        if word == "":
            continue
        # Initialize to empty string
        histogram[word] = ""

    # Increment hash
    histogram[word] += "#"

histogram_items = list(histogram.items())
# Sort the (word, hash) tuples by:
# - Length of hash string in reverse (so greatest is at the top)
# - Then by alphabetical order, for hash strings that are equal length
histogram_items.sort(key = lambda pair: (-len(pair[1]), pair[0]))

for item in histogram_items:
    # https://stackoverflow.com/a/54969247
    # :<{longest + 2} is saying the first column is {longest + 2} chars long
    # and left justified
    print(f"{item[0] :<{longest + 2}}{item[1]}")



