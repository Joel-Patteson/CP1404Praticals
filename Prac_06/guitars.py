from Prac_06.guitar import Guitars


def main():
    print("My guitars!")
    my_guitars = []
    input_name = input("Name: ")
    while input_name != "":
        input_year = int(input("Year: "))
        input_price = float(input("Price: "))
        new_guitar = Guitars(input_name, input_year, input_price)
        my_guitars.append(new_guitar)
        print(new_guitar, "Added")
        input_name = input("Name: ")

    my_guitars.append(Guitars("Gibson L-5 CES", 1922, 16035.40))
    my_guitars.append(Guitars("Line 6 JTV-59", 2010, 1512.9))

    if Guitars:
        Guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(Guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
             {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
