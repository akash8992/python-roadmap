print("Legal age of marrage in India")

gender = input("Enter male (m) or Female (f): ")
age = int(input("Enter age: "))

if gender == "m":
    if age >= 21:
        print("Legal age of marrage")
    else:
        print("child marrage")
elif gender == "f":
    if age >= 18:
        print("legal age of marrage")
    else:
        print("child marrage")

else:
    print("Enter m for male and f for female")
