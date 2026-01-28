from random import random

values = [random() for i in range(20)]
x = random()
values.sort()
matching_indices = []

for i, val in enumerate(values):
    if val >= x:
        matching_indices.append(i)


if len(matching_indices)> 0:
    print(matching_indices[0])