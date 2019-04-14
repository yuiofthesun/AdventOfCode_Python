
def main():
    f = open('numbers', 'r')
    numbers = []

    for line in f:
        numbers.append(int(line))

    print(type(numbers))
    print(len(numbers))


if __name__ == '__main__':
    main()