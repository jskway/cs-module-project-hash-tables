import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words

# Split the words into a list
words_list = words.split()

# Iterate through the words and build the dataset of which words follow
# particular words
dataset = {}

for i in range(len(words_list)):
    if words_list[i] not in dataset:
        dataset[words_list[i]] = []

    try:
        dataset[words_list[i]].append(words_list[i + 1])
    except IndexError:
        break


# TODO: construct 5 random sentences

suffixes = ('.', '?', '!', '."', '?"', '!"')

def print_random_sentence(word):
    print(word, end=" ")

    if word.endswith(suffixes):
        print('\n')
        return
    else:
        print_random_sentence(random.choice(dataset[word]))

print_random_sentence('Alice')
print_random_sentence('One')
print_random_sentence('King')
print_random_sentence('Queen')
print_random_sentence('Dinah')








