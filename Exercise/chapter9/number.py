print("Enter one number, and I'll display it.")
print("Enter 'q' to quit")
while True:
    number = input("Enter number: ")
    if number == 'q':
        break
    try:
        print("Number you just enter: ", int(number))
    except ValueError:
        print("You entered is not a number!")