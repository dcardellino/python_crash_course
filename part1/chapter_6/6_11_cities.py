cities = {
    'stuttgart': {
        'country': 'germany',
        'population': 500000,
        'attractions': 'canstatter wasen'
    },
    'orlando': {
        'country': 'america',
        'population': 280000,
        'attractions': 'disney world'
    },
    'new york': {
        'country': 'america',
        'population': 8400000,
        'attractions': 'central park'
    }
}

for city, fact in cities.items():
    print(f"The city {city} is located in {fact['country'].title()}")
    print(f"It has a population of {str(fact['population'])} and it's most famous attraction is {fact['attractions'].title()}")