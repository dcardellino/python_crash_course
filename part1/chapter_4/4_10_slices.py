from random import randint

numbers = [randint(0, 9) for i in range(99)]

print(f"The first three items are: {str(numbers[:3])}")
print(f"Three items from the middle of the list are: {str(numbers[49:52])}")
print(f"The last three items from the list are: {str(numbers[-3:])}")