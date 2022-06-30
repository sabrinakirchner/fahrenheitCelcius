def fahcel():
    fahrenheit = float(input("What temperature (in fahrenheit) would you like converted to celcius? "))
    celsius =  (fahrenheit -32)* 5/9
    print(fahrenheit, "F is", round(celsius, 2), "C" )


    keepPlay = input("Do you want to ask another one? ").lower().strip()

    while keepPlay == "yes":
        fahcel()

    if keepPlay == "no":
        print("Thanks for play. ")
        quit()


fahcel()


