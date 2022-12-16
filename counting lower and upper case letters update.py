# counting lower and upper case letters

def count(letters):
    upper = 0
    lower = 0
    for char in letters:   
        
        
        if char.isupper():
            upper = upper +1
        if char.islower():
            lower = lower +1
        if char.isdigit():
            print("You are not allowed to put numbers")
    print("The number of lower letters is", lower)
    print("The number of upper letters is", upper)
    # returning the function    
    return count


add = input("Enter a sentence: ")

print(count(add))