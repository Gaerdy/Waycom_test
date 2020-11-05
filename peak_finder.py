#!/bin/python3

def read_lines():
    """
    Read lines from main entry

    :return : (list) split lines
    """
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line.split(":"))
    return [[int(time) for time in call] for call in content]


def call_peak(call_list):
    """
    Find the maximum number of simultaneous calls and print the answer

    :param call_list: (list) list of integer list
    :return: None
    """
    max_count = 0
    count = 0
    start = call_list[0][0]
    end = call_list[0][1]

    # Find last call end
    for call in call_list:
        if call[1] > end:
            end = call[1]

    # Count simultaneous calls for each second between first and last call
    for i in range(start, end):
        for call in call_list:
            if call[0] <= i < call[1]:
                count += 1
        if count > max_count:
            max_count = count
        count = 0

    print(max_count)


if __name__ == '__main__':
    call_peak(read_lines())
