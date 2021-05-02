user_names = ["dcardellino", "fpeters", "mfrese", "fbreckle", "admin"]

for user in user_names:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")