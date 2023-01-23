#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for elem in dir(hidden_4):
        if elem[0:2] != "__":
            print(elem)
