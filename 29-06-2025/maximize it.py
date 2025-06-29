from itertools import product
K, M = map(int, input().split())
lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    # Skip the first number (count), store the rest
    lists.append(data[1:])
all_combinations = product(*lists)
max_value = 0
for combo in all_combinations:
    value = sum(x**2 for x in combo) % M
    if value > max_value:
        max_value = value
print(max_value)
