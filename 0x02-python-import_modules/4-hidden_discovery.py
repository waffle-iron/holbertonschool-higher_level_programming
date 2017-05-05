#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4  # import modules from Python cache file
    names = dir(hidden_4)
    for n in names:
        if n[0] != '_':
            print('{}'.format(n))
