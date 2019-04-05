age = input("how old are you?")

if age:
    age = int(age)    
    if age >= 21: 
        print("you are good to enter and can drink!")
    elif age >= 18:
        print("you can enter, but need a wristband!")
    else:
        print("you can't come in, little one!")
else:
    print("please enter an age!")