def int_split_sum_combos(number: int) -> [int]:
    sums = []
    number_str = str(number)
    for i in range(len(str(number))-1):
        prefix = int(number_str[:i+1])
        suffix = int(number_str[i+1:])
        sums.append(prefix + suffix)
    return sums
