favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite programming language is {language.title()}")

coders = ["phil", "josh", "david", "becca", "sarah", "matt", "danielle"]

for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")
