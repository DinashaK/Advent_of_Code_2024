from collections import Counter

with open('input.txt') as file:
    left_list, right_list = [], []

    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

def calculate_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return sum(abs(l - r) for l, r in zip(left_list, right_list))

distance = calculate_distance(left_list, right_list)
print(distance)

right_counter = Counter(right_list)
similar = sum(left * right_counter[left] for left in set(left_list))

print(similar)