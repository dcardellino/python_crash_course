favorite_places = {
    'dominic': ['gallipoli', 'new york', 'orlando'],
    'lisa': ['disney land', 'new york', 'miami'],
    'robyn': ['berlin', 'stuttgart', 'paris']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")