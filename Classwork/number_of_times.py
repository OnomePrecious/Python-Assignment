def count_number_of_times(number_list):
    count_numbers = 0
    for char in number_list:
        if char.t:
            count_numbers += 1
            return f"NUMBERS{count_numbers}"


number_list = [1, 2, 2, 3, 4, 2]
print(count_number_of_times(number_list))
