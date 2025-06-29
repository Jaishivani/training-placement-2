from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
all_combinations = list(combinations(range(n), k))
favorable = 0
for comb in all_combinations:
    if 'a' in [letters[i] for i in comb]:
        favorable += 1
probability = favorable / len(all_combinations)
print(f"{probability:.4f}")
