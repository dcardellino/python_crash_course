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