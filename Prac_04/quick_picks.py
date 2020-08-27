import random

SMALLEST = 1
LARGEST = 45
error_check = True
quick_pick = 0
while error_check is True:
    try:
        quick_pick = int(input("How many quick picks? "))
        error_check = False

    except ValueError:
        print("Invalid input")
        error_check = True

number_list =[]
for i in range(0,quick_pick):
    for i in range(6):
        number = random.randrange(SMALLEST,LARGEST+1)
        error_check = number in number_list
        while error_check is True:
            number = random.randrange(SMALLEST,LARGEST+1)
            error_check = number in number_list

        number_list.append(number)
        print(number, end=" ")
    print()