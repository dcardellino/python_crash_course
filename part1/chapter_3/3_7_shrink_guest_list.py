guest_list = ["Lisa", "Luigi", "Sabine", "Andy", "Andi", "Didi", "Conny", "Roby"]

for guest in guest_list:
    print(f"You're invited to my dinner party, {guest}")

print(f"{guest_list[3]} can't make it to the party")

guest_list[3] = "Andreas"

for guest in guest_list:
    print(f"You're invited to my dinner party, {guest}")

guest_list.insert(0, "Leo")
guest_list.insert(5, "Tim")
guest_list.append("Sam")

for guest in guest_list:
    print(f"You're invited to my dinner party, {guest}")

print("I only can invite 2 people for dinner!")



while len(guest_list) > 2:
    name = guest_list.pop()
    print(f"Sorry, {name}")

print(len(guest_list))
print(guest_list)