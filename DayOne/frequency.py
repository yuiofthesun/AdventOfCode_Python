

def main():
    f = open('numbers', 'r')
    numbers = []
    result: int = 0
    frequencies = {result}

    for line in f:
        numbers.append(int(line))

    f.close()

    while True:
        for number in numbers:
            result = result + number

            if result in frequencies:
                print(result)
                return result

            frequencies.add(result)


if __name__ == '__main__':
    main()
