import os
# getting the input for the problem
print(os.getcwd())
# change working directory for the input file
os.chdir(os.path.dirname(__file__))
file_in = open("day02input.txt", "r")
print(file_in)
content = file_in.readlines()
file_in.close()

seq = []
for x in content:
    seq.append(x.rstrip())

hor_pos = 0
depth = 0

# Part 1
for x in seq:
    apart = x.split()
    instruction = apart[0]
    num = int(apart[1])
    if instruction == "up":
        depth = depth - num
    elif instruction == "down":
        depth = depth + num
    elif instruction == "forward":
        hor_pos = hor_pos + num

print("Multiplying at the end", hor_pos*depth)

depth = 0
hor_pos = 0
aim = 0

# Part 2
for x in seq:
    apart = x.split()
    instruction = apart[0]
    num = int(apart[1])
    if instruction == "up":
        aim = aim - num
    elif instruction == "down":
        aim = aim + num
    elif instruction == "forward":
        hor_pos = hor_pos + num
        depth = depth + aim * num

print("Multiplying at the end", hor_pos*depth)