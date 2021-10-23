import re
import json
import os
from random import randint

card_types_path = os.path.join(os.path.dirname(__file__), 'static/card_types.json')

def card_sum(card_number):
    total_sum = 0
    if not re.search(r'^\d+$', card_number):
        raise ValueError('Invalid card number!')

    for i in range(len(card_number)):
        if i % 2 == 0:
            new_digit = int(card_number[i])*2

            if new_digit > 9:
                new_digit = new_digit - 9

            total_sum += new_digit
        else:
            total_sum += int(card_number[i])

    return total_sum

def get_card_props(card_type):
    with open(card_types_path) as card_data:
        card_types = json.load(card_data)
        card_flag = card_types[card_type]
        if not card_flag:
            raise ValueError('Card not supported')

        return {
            'niceType': card_flag['niceType'],
            'lengths': card_flag['lengths'],
            'patterns': card_flag['patterns']
        }

def generate_credit_card(card_type = ''):
    default_types = ['visa', 'mastercard', 'american-express']
    random_type = randint(0, 2)
    card_props = get_card_props(default_types[random_type])

    card_length = card_props['lengths'][0]
    start_pattern = card_props['patterns'][0]
    if isinstance(start_pattern, list):
        start_pattern = start_pattern[0]

    card_number = str(start_pattern)
    missing_numbers = card_length - len(card_number) - 1

    for i in range(missing_numbers):
        card_number += str(randint(0, 9))

    digits_sum = card_sum(card_number)

    if (len(card_number) % 2 == 0):
        new_digit = (10 - digits_sum % 10) % 10
        if new_digit % 2 == 0:
            card_number += str(int(new_digit/2))
        else:
            card_number += str(int((new_digit + 9) / 2))
    else:
        card_number += str((10 - digits_sum % 10) % 10)

    return {"type":card_props['niceType'],
            "cc":card_number,
            "date":str(randint(1,12))+"/"+str(randint(22,28)),
            "cvv":randint(100,999)}
