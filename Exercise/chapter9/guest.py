# Bai 1
flag= True
while(flag):
    name = input("Please enter your name: ")
    if name == "quit":
        flag = False
    else:
        print(f"Hello, ", name)
        with open("guest.txt", "a") as file_object:
            file_object.write(f"{name}\n")