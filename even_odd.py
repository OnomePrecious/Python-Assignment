even_total = 0
odd_total = 0
try:
    number = int(input("Enter a number: "))
except ValueError("Invalid input"):

    for numbers in range(1, number):
        if numbers % 2 == 0:
            even_total += numbers
        else:
            odd_total += numbers

            print("The sum of even number is:", even_total)
            print("The sum of odd number is:", odd_total)



