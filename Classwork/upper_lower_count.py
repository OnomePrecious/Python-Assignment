def accept_sentence(sample_string: str) -> str:
    count_alpha = 0
    count_lower = 0
    for char in sample_string:
        if char.isupper():
            count_alpha += 1
        elif char.islower():
            count_lower += 1
    return f'UPPERCASE{count_alpha}, LOWERCASE{count_lower}'


sentence = "Hello world!"
print(accept_sentence(sentence))
