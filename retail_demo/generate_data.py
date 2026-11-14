from pathlib import Path
import random
import csv

random.seed(42)
rows = []
for index in range(3000):
    category = random.choice(['Technology', 'Furniture', 'Office'])
    price = {'Technology': 220, 'Furniture': 150, 'Office': 25}[category]
    quantity = random.randint(1, 8)
    discount = random.choice([0, .05, .1, .2, .3, .4])
    base = price * random.uniform(.6, 1.4) * quantity
    sales = round(base * (1 - discount), 2)
    rows.append(dict(transaction_id=index + 1, month=random.randint(1, 12), region=random.choice(['North', 'South', 'East', 'West']), category=category, segment=random.choice(['Consumer', 'Corporate', 'Home office']), channel=random.choice(['Online', 'Store']), quantity=quantity, discount=discount, sales=sales, profit=round(sales - base * random.uniform(.55, .8), 2)))
with (Path(__file__).parent / 'data.csv').open('w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
