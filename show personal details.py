def personal_details():
# asking user input
    name = input("Enter your name: ")
#checking to see if the input is a digit number
    while name.isdigit():
        if name.isdigit():
            print("Sorry, no numbers allowed")
            name = input("Enter your name: ")
        else:
            print("Name accepted.")
# checking if the input is a symbol
    age = input("Enter your age: ")
    while age.isalpha():
        if age.isalpha():
            print("Sorry, did not understand.Try again")
            age = input("Enter your age: ")
        else:
            print("Age accepted.")
# checking if the input is a symbol
    height = input("Enter your height: ")
    while height.isalpha():
        if height.isalpha():
            print("Sorry, did not understand.Try again")
            height = input("Enter your height: ")
        else:
            print("Height accepted.")
    print("Hello ",name,". You are ",age," years old. Your height is ",height)
print(personal_details())