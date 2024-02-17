countries = ["afghanistan", "albania", "algeria", "andorra", "angola", "antigua and barbuda", "argentina", "armenia",
             "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium",
             "belize", "benin", "bhutan", "bolivia", "bosnia and herzegovina", "botswana", "brazil", "brunei",
             "bulgaria", "burkina faso", "burundi", "cabo verde", "cambodia", "cameroon", "canada",
             "central african republic", "chad", "chile", "china", "colombia", "comoros",
             "democratic republic of the congo", "republic of the congo", "costa rica", "côte d’ivoire", "croatia",
             "cuba", "cyprus", "czech republic", "denmark", "djibouti", "dominica", "dominican republic", "timor-leste",
             "ecuador", "egypt", "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia",
             "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada",
             "guatemala", "guinea", "guinea bissau", "guyana", "haiti", "honduras", "hungary", "iceland", "india",
             "indonesia", "iran", "iraq", "ireland", "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan",
             "kenya", "kiribati", "north korea", "south korea", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia",
             "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "madagascar",
             "malawi", "malaysia", "maldives", "mali", "malta", "marshall islands", "mauritania", "mauritius", "mexico",
             "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia",
             "nauru", "nepal", "netherlands", "new zealand", "nicaragua", "niger", "nigeria", "north macedonia",
             "norway", "oman", "pakistan", "palau", "panama", "papua new guinea", "paraguay", "peru", "philippines",
             "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis", "saint lucia",
             "saint vincent and the grenadines", "samoa", "san marino", "sao tome and principe", "saudi arabia",
             "senegal", "serbia", "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon islands",
             "somalia", "south africa", "spain", "sri lanka", "sudan", "south sudan", "suriname", "sweden",
             "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "togo", "tonga",
             "trinidad and tobago", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine",
             "united arab emirates", "united kingdom", "united states", "uruguay", "uzbekistan", "vanuatu",
             "vatican city", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"]  # 196 countries
correct = []
guess = ""
number_correct = 0

while number_correct < len(countries):  # while all countries haven't been guessed
    guess = input("Guess a country: ").lower()  # take guess
    if guess in countries:
        if guess not in correct:  # if not already guessed
            correct.append(guess)  # add guess to list
            number_correct = number_correct + 1  # increase number of correct guesses
            print("Correct!")
        else:
            print("Already guessed...")
    elif guess == "give up":
        print("Too bad")
        number_correct = 400  # ends while
    else:
        print("Incorrect.")
    print(len(correct), "/", len(countries), "guessed correctly.")  # running score

if number_correct == len(countries):
    print("You guessed all the countries correctly!")  # winner!!
