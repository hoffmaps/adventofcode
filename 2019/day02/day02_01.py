file_in = open("input02", "r")
print(file_in)

content = file_in.read()
print(content)
file_in.close()

string_code = content.split(',')

# list comprehension thing - so don't have x lying around
code = [int(x) for x in string_code]


# setting up program
code[1] = 12
code[2] = 2
print(code)

# for each opcode
i = 0
opcode = code[i]
while opcode != 99:
    if opcode == 1:
        num01 = code[i+1]
        num02 = code[i+2]
        storage = code[i+3]
        code[storage] = code[num01] + code[num02]
        print(code)
    elif opcode == 2:
        num01 = code[i+1]
        num02 = code[i+2]
        storage = code[i+3]
        code[storage] = code[num01] * code[num02]

    # moves on to next opcode
    i = i+4
    opcode = code[i]

print(code)