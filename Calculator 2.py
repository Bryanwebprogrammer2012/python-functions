def calculator():
    question = float(input("\nEnter a number to calculate: "))
    question2 = float(input("\nEnter the second number to calculate: "))
    print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
    htc = int(input("\nHow do you want to calculate (Enter by the number of calculation): "))
    if htc is 1:
        add = question + question2
        print("The answer is",add)
    if htc is 2:
        sub = question - question2
        print("The answer is",sub)
    if htc is 3:
        mul = question * question2
        print("The answer is",mul)
    if htc is 4:
        div = question/question2
        print("The answer is",div)
    return calculator()
calculator()