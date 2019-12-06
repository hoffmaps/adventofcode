file_in = open("input02", "r")
print(file_in)

content = file_in.read()
print(content)
file_in.close()

string_code = content.split(',')

# list comprehension thing - so don't have x lying around
og_code = [int(x) for x in string_code]

def try_input(code, pos01, pos02):
    # setting up program
    code[1] = pos01
    code[2] = pos02
    i = 0
    opcode = code[i]
    # run through opcode
    while opcode != 99:
        if opcode == 1:
            num01 = code[i+1]
            num02 = code[i+2]
            storage = code[i+3]
            code[storage] = code[num01] + code[num02]
        elif opcode == 2:
            num01 = code[i+1]
            num02 = code[i+2]
            storage = code[i+3]
            code[storage] = code[num01] * code[num02]
        print(code)
        # moves on to next opcode
        i = i+4
        opcode = code[i]
    return code[0] == 19690720


x = 0
y = 0
c = og_code.copy()
# brute force going through a whooole bunch of options up to 50
while not try_input(c, x, y):
    c = og_code.copy()
    x = x + 1
    if x >= 50:
        x = 0
        y = y + 1

print("Noun:", x)
print("Verb:", y)
ans = 100*x + y
print("Answer:", ans)
# 1, 0 = 1258708
# 2, 1 = 1719509