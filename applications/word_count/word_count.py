def word_count(s):
    counts = {}
    to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'

    # convert to lower case
    s = s.lower()

    # split words into list
    string_list = s.split()

    # iterate through the words
    for word in string_list:
        # strip out invalid chars
        word = word.strip(to_ignore)

        # If there are no valid chars, skip to the next word
        if word == '': continue

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('" : ; , . - + = / \ | [ ] { } ( ) * ^ &'))

