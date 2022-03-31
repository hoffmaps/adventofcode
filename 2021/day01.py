import os
# getting the input for the problem
print(os.getcwd())
# change working directory for the input file
os.chdir(os.path.dirname(__file__))
file_in = open("day01input.txt", "r")
print(file_in)
content = file_in.readlines()
file_in.close()

# put all the numbers in a nice array
numbers = []
for x in content:
    numbers.append(int(x.rstrip()))

# Part 01
counter = 0
last_num = numbers[0]
for num in numbers:
    if num > last_num:
        counter+=1
    last_num = num

print("Number of increases:", counter)

# Part 02
counter = 0
first_sum = numbers[0] + numbers[1] + numbers[2]
i = 1
while i < len(numbers) - 1:
    second_sum = numbers[i-1] + numbers[i] + numbers[i+1]
    if second_sum > first_sum:
        counter += 1
    first_sum = second_sum
    i += 1

print("Number of group increases:", counter)
