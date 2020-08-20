name = input("Enter your name ")
OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
print("Your name is", name, file=out_file)

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()
