
fruits = [
    ('apple', 280),
    ('orange', 90),
    ('watermelon', 75),
    ('gauva', 105),
    ('grapes', 140),
    ('pineapple', 80),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 40)

price = (["fruits" for fruit in fruits])
print(f"price :{price}")

print("-" * 40)
price = [fruit for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[0] for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] * 0.9 for fruit in fruits]                # disc of 10%
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] * 0.75 for fruit in fruits]                # disc of 10%
print(f"price :{price}")

print("-" * 40)
price = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits
                            if fruit[1] > 100]
print(f"price :{price}")

