rivers = {
    "nile": "egypt",
    "mississippi": "united states",
    "fraser": "canada",
    "kuskokwim": "alaska",
    "yangtze": "china",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers:
    print(river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(country.title())
