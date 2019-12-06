
# getting the input for the problem
file_in = open("input01_01", "r")
print(file_in)
content = file_in.readlines()
print(content)
numbers = []
for x in content:
    numbers.append(int(x.rstrip()))


# go through every mass
total = 0

for m in numbers:
    fuel = (m//3) - 2
    total = total + fuel

print("Answer: ", total)