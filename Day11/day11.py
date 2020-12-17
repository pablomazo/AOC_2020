import copy
with open('input', 'r') as f:
    seats = f.read().splitlines()

for i, line in enumerate(seats):
    seats[i] = list(line)

def print_seats():
    for line in seats:
        l = ''
        for i in range(len(line)):
            l += line[i]
        print(l)

    print()

def update_state():
    new_seats = copy.deepcopy(seats)

    nocc = 0
    for i in range(len(new_seats)):
        for j in range(len(new_seats[0])):
            new_seats[i][j] = update_seat(i,j)

        nocc += new_seats[i].count('#')


    return new_seats, nocc

def update_seat1(i,j):
    seat = seats[i][j]
    if seat == '.':
        return '.'

    surround = [[i-1,j-1], [i-1,j], [i-1,j+1],
                [i  ,j-1],          [i,  j+1],
                [i+1,j-1], [i+1,j], [i+1,j+1]]

    nocc = 0
    for [a, b] in surround:
        if a>=0 and a<len(seats) and b>=0 and b<len(seats[0]):
            if seats[a][b] == '#': nocc +=1

    if seat == 'L' and nocc == 0:
        return '#'
    elif seat == '#' and nocc > 3:
        return 'L'
    else:
        return seat

def update_seat(i,j):
    seat = seats[i][j]
    if seat == '.':
        return '.'

    dirs = [[-1,-1], [-1,0], [-1,1],
            [ 0,-1],        [ 0,1],
            [+1,-1], [+1,0], [+1,1]]

    nocc = 0
    for [ix, iy] in dirs:
        a, b = i, j
        for r in range(len(seats)):
            a += ix
            b += iy

            if a>=0 and a<len(seats) and b>=0 and b<len(seats[0]):
                if seats[a][b] == '#':
                    nocc +=1
                    break
                elif seats[a][b] == 'L':
                    break
            else:
                break

    if seat == 'L' and nocc == 0:
        return '#'
    elif seat == '#' and nocc > 4:
        return 'L'
    else:
        return seat

nocc_p = 0
for i in range(10000):
    #print_seats()
    seats, nocc = update_state()
    if nocc == nocc_p:
        print(nocc)
        break

    nocc_p = nocc
