

def find_longest():
    longest_word = ''

    with open('C:\\local_new\\input.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

        for line in data:
            if len(line) > len(longest_word):
                longest_word=line

    return longest_word