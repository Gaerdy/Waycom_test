#!/bin/python3

def word_count(string):
    """
    Count word occurrences from main entry and print it
    :param string: string entry
    :return: None
    """
    entry_list = [element for element in string.split(" ")]
    count_list = []

    while len(entry_list) > 0:
        word = entry_list[0]
        counter = 0
        i = 0
        while i < len(entry_list):
            if entry_list[i] == word:
                counter += 1
                entry_list.pop(i)
            else:
                i += 1
        count_list.append((word, counter))

    count_list.sort(key=lambda x: x[1], reverse=True)

    for items in count_list:
        print(f'{items[1]} {items[0]}')


if __name__ == '__main__':
    word_count(input())
