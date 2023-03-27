# library imports
import sys


# custom imports


def greet(fname: str) -> str:
    print(f'Hello {fname}, and welcome to the code snippet section')
    return fname


if __name__ == '__main__':
    name = sys.argv[1]
    greet(name)
