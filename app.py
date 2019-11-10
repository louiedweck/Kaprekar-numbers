def int_split_sum_combos(number: int) -> [int]:
    sums = []
    number_str = str(number)
    for i in range(len(str(number))-1):
        prefix = int(number_str[:i+1])
        suffix = int(number_str[i+1:])
        sums.append(prefix + suffix)
    return sums


def is_kaprekar(n: int) -> bool:
    return n in int_split_sum_combos(n*n)


def kaprekars_before(n: int) -> [int]:
    kaprekars = []
    for i in range(1, n+1):
        if is_kaprekar(i) and i % 10 != 0:
            kaprekars.append(i)
    return kaprekars


def valid_user_input(prompt, options):
    '''Ensures user input is within valid options. '''
    user_input = input(prompt)
    while user_input not in options:
        print("Invalid option")
        user_input = input(prompt)
    return user_input
