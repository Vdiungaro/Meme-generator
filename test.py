import random

with open('quotes.txt', 'r') as f:
    lines = f.read().splitlines()
f.close()

selected = random.choice(lines)

print(selected)