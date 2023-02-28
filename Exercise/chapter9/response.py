flag= True
prompt = "Why do you like programming? Please enter your question: \n"
while(flag):
    res = input(prompt)
    if res == "":
        flag = False
    else:
        with open("responses.txt", "a") as file_object:
            file_object.write(f"{res}\n")