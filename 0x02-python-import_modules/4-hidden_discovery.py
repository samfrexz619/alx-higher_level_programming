#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    for title in dir(hidden_4):
        if title[0] != '_' and title[1] != '_':
            print(title)
