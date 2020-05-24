from functions import sigmoid, approximate, approximate2

def main():
    E = approximate2(3, 1.1, 0.25, 0.5, breakpoint= 1)
    print(E)
    E = approximate2(1, 2.9, E, 0.5, breakpoint = 1)
    print(E)
    pass


if __name__ == "__main__":
    main()
    pass