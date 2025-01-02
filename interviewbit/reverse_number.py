def reverse_number(number: int) -> int:
    new_number = 0

    while number:
        new_number = new_number * 10 + number % 10
        number = number // 10

    return new_number


if __name__ == '__main__':
    print(reverse_number(int(input())))
