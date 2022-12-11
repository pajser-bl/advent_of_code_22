instructions = """noop
noop
addx 5
addx 21
addx -16
noop
addx 1
noop
noop
addx 4
addx 1
addx 4
addx 1
noop
addx 4
addx -9
noop
addx 19
addx -5
noop
noop
addx 5
addx 1
addx -38
addx 5
addx -2
addx 2
noop
noop
addx 7
addx 9
addx 20
addx -3
addx -18
addx 2
addx 5
noop
noop
addx -2
noop
noop
addx 7
addx 3
addx -2
addx 2
addx -28
addx -7
addx 5
noop
addx 2
addx 32
addx -27
noop
noop
noop
noop
noop
addx 7
noop
addx 22
addx -19
noop
addx 5
noop
addx -7
addx 17
addx -7
noop
addx -20
addx 27
noop
addx -16
addx -20
addx 1
noop
addx 3
addx 15
addx -8
addx -2
addx -6
addx 14
addx 4
noop
noop
addx -17
addx 22
noop
addx 5
noop
noop
noop
addx 2
noop
addx 3
addx -32
addx -5
noop
addx 4
addx 3
addx -2
addx 34
addx -27
addx 5
addx 16
addx -18
addx 7
noop
addx -2
addx -1
addx 8
addx 14
addx -9
noop
addx -15
addx 16
addx 2
addx -35
noop
noop
noop
noop
addx 3
addx 4
noop
addx 1
addx 4
addx 1
noop
addx 4
addx 2
addx 3
addx -5
addx 19
addx -9
addx 2
addx 4
noop
noop
noop
noop
addx 3
addx 2
noop
noop
noop"""

_instructions = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

x = 1
c = 0
it = [20, 60, 100, 140, 180, 220]
s = 0
crt = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]
for instruction in instructions.split('\n'):
    if instruction.startswith('noop'):
        if c % 40 in [x - 1, x, x + 1]:
            crt[c // 40][c % 40] = '#'
        c += 1
        if c in it:
            s += c * x
    else:
        if c % 40 in [x - 1, x, x + 1]:
            crt[c // 40][c % 40] = '#'
        c += 1
        if c in it:
            s += c * x
        if c % 40 in [x - 1, x, x + 1]:
            crt[c // 40][c % 40] = '#'
        c += 1
        if c in it:
            s += c * x

        x += int(instruction.split()[1])

print(s)
for row in crt:
    print("".join(row))
