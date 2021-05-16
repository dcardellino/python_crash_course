prompt = "\n How old are you?"
prompt += "\nEnter 'quit' to leave the program.\n"

while True:
    age = input(prompt)
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("\nThe movie ticket is free!")
    elif age >= 3 and age < 12:
        print("\nThe price for the ticket is 10$!")
    else:
        print("\nThe price for the ticket is 15$!")
