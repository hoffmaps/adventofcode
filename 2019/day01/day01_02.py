

# recursion to continue calculating fuel for additional fuel that comes in
def calculate_fuel(mass):
    new_fuel = mass//3 - 2
    if new_fuel <= 0:
        return 0
    else:
        return new_fuel + calculate_fuel(new_fuel)


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
    total = total + calculate_fuel(m)

print("Answer: ", total)