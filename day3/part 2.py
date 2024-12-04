import re

with open('input.txt', 'r') as file:
    data = file.read()

pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

enabled = True  
result_sum_part2 = 0
instructions = re.findall(pattern, data)

for instruction in instructions:
    if instruction[0].startswith("mul"):
        if enabled:
            result_sum_part2 += int(instruction[1]) * int(instruction[2])
    elif instruction[0] == "do()":
        enabled = True
    elif instruction[0] == "don't()":
        enabled = False

print(result_sum_part2)
