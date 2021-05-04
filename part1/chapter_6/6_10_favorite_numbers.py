favorite_numbers = {
    'Dominic': [9,8],
    'Lisa': [12,8,4],
    'Robyn': [22,14],
    'Sabine': [13,10],
    'Luigi': [7,9]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"\t- {str(number)}")