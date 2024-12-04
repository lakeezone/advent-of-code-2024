import re

with open('/mnt/data/input.txt', 'r') as file:
    data = file.read()

pattern = r"mul\((\d+),(\d+)\)"

# Extract all matches
matches = re.findall(pattern, data)

result_sum = sum(int(x) * int(y) for x, y in matches)

result_sum
