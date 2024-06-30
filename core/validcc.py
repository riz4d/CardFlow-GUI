import random
from core.isvalid import is_valid_credit_card

def generate_valid_cc(bin_number):
    bin_number = str(bin_number)
    bin_length = len(bin_number)
    total_length = 16
    remaining_length = total_length - bin_length - 1
    
    while True:
        if remaining_length > 0:
            generated_num = ''.join([str(random.randint(0, 9)) for _ in range(remaining_length)])
        else:
            generated_num = ""
        
        incomplete_card_number = bin_number + generated_num
        for check_digit in range(10):
            card_number = incomplete_card_number + str(check_digit)
            if is_valid_credit_card(card_number):
                return card_number
