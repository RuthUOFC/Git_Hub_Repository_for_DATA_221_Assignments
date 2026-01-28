pairs = [[5,2], [3,-1], [4,3], [2,0]]

result = []
def variable_computed_to_the_power_of(x,y):
    return x**y

for p in pairs:
    if p[1] < 0:
        continue
    else:
        result.append(variable_computed_to_the_power_of(*p))



print(result)