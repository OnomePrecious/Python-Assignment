from Account.exception.invalid_input_error import InvalidInputError


def dispatch_rider(successful_delivery):
    amount_pay = 0
    base_pay = 5000

    if successful_delivery <= 0:
        raise InvalidInputError("Invalid input")

    if 50 > successful_delivery >= 1:
        amount_pay = 160
    if 59 <= successful_delivery > 50:
        amount_pay = 200
    if 69 <= successful_delivery > 59:
        amount_pay = 250
    if successful_delivery >= 70:
        amount_pay = 500

    return successful_delivery * amount_pay + base_pay


