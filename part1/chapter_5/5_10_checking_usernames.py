current_users = [
    "dcardellino",
    "fbreckle",
    "fpeters",
    "mfrese",
    "jyb"
]

new_users = [
    "benleb",
    "aakyuez",
    "fbreckle",
    "mfrese",
    "hherbst"
]

for user in new_users:
    if user in current_users:
        print(f"The username {user} is already in use. Please choose another username.")
    else:
        print(f"{user} is available.")