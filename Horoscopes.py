birthday = input("Enter your birthday (dd/mm/yy): ")  # inputs user birthday
day = int(birthday[0:2])  # slices day
month = int(birthday[3:5])  # slices month
year = int(birthday[6:])  # slices year
age = 0

if year < 25:  # calculates age based on today (16/02/24)
    if month < 3:
        if day < 17:
            age = 24 - year
        else:
            age = 23 - year
    else:
        age = 23 - year
else:
    if month < 3:
        if day < 17:
            age = (100 - year) + 24
        else:
            age = (100 - year) + 23
    else:
        age = (100 - year) + 23

print("You are", age, "years old!")

if month == 1:  # calculates zodiac sign based on day and month of birthday
    if day < 22:
        print("You are a Capricorn!")
    else:
        print("You are an Aquarius!")
elif month == 2:
    if day < 19:
        print("You are an Aquarius!")
    else:
        print("You are a Pisces!")
elif month == 3:
    if day < 21:
        print("You are a Pisces!")
    else:
        print("You are an Aries!")
elif month == 4:
    if day < 21:
        print("You are an Aries!")
    else:
        print("You are a Taurus!")
elif month == 5:
    if day < 21:
        print("You are a Taurus!")
    else:
        print("You are a Gemini!")
elif month == 6:
    if day < 22:
        print("You are a Gemini!")
    else:
        print("You are a Cancer!")
elif month == 7:
    if day < 23:
        print("You are a Cancer!")
    else:
        print("You are a Leo!")
elif month == 8:
    if day < 24:
        print("You are a Leo!")
    else:
        print("You are a Virgo!")
elif month == 9:
    if day < 24:
        print("You are a Virgo!")
    else:
        print("You are a Libra!")
elif month == 10:
    if day < 24:
        print("You are a Libra!")
    else:
        print("You are a Scorpio!")
elif month == 11:
    if day < 23:
        print("You are a Scorpio!")
    else:
        print("You are a Sagittarius!")
elif month == 12:
    if day < 22:
        print("You are a Sagittarius!")
    else:
        print("You are a Capricorn!")
