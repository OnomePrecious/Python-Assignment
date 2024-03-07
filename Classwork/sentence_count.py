def accept_sentence(sample_string):
    count_letters = 0
    count_digits = 0
    for char in sample_string:
        if char.isalpha():
            count_letters += 1
        elif char.isnumeric():
            count_digits += 1
    return f'LETTERS{count_letters}, DIGITS{count_digits}'


sentence = "Hello world! 123"
print(accept_sentence(sentence))
