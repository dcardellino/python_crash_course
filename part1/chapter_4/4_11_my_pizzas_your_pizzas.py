my_pizzas = ['margharita', 'napoli', 'tonno', 'diavolo', 'hawaii']
friends_pizzas = my_pizzas[:]

my_pizzas.append('frutti di mare')
friends_pizzas.append('funghi')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)