from app import valid_user_input
from app import int_split_sum_combos
from app import is_kaprekar
from app import kaprekars_before


def user_choice():
    number = int(input("Enter a number: "))
    print(kaprekars_before(number))


if __name__ == '__main__':
    user_choice()
