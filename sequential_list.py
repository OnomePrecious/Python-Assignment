my_list = [number for number in range(1, 16)]
print(my_list)

my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14,14, 15, 15]
print(my_list)

my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14,14, 15, 15]
print(set(my_list))


def add_third_elements(this_list):
    total = 0
    for i in range(2, len(this_list), 3):
        total += this_list[i]
    return total


#def sum_first_middle_last_elements(this_list):
 #   my_list1 = [this_list[0],this_list[len(this_list)-1],this_list[len(this_list)//2]]
  #  return my_list1

#def sums(the_list):
 #       total = 0
  #      for i in range([len(the_list)-1],the_list[len(the_list)//2]]:
   #         total+=the_list[i]
    #        return total

inputs = []
for number in range(10):
    collection = input("Enter numbers: ")
    inputs.append(collection)
    print(set(inputs))

def sum_collection(numbers):
    total = 0
    for i in numbers:
        total+= i
    return total

def remove_item(removed_element):
   if removed_element in set():
    return removed_element
   else:
    return none
