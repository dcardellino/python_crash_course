prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"  I will add {topping} to your pizza.")
    else:
        break
