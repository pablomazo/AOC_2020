with open('input', 'r') as f:
    lines = [int(l) for l in f.read().splitlines()]

PREAMBLE_LEN = 25

def check_is_sum(preamble, number):
    preamble.sort()

    is_sum = False
    if number < preamble[0] or number > 2*preamble[-1]:
        is_sum = False
    else:
        for i1 in range(len(preamble)):
            n1 = preamble[i1]
            for i2 in range(i1+1, len(preamble)):
                n2 = preamble[i2]
                if n1 + n2 == number:
                    is_sum = True
                    break

    return is_sum

def get_num(preamble, number):
    for i1 in range(len(preamble)):
        i2 = i1 + 1
        if i2 < len(preamble):
            n1 = preamble[i1]
            n2 = preamble[i2]
            suma = n1 + n2

            while suma < number and i2 < len(preamble):
                i2 += 1
                n2 = preamble[i2]
                suma += n2

                if suma == number:
                    ran = preamble[i1:i2+1]
                    ran.sort()
                    suma = 0
                    for elem in ran:
                        suma += elem

                    print('Sum: {}'.format(ran[0] + ran[-1]))
                    return

ini_num = PREAMBLE_LEN
ini_pre, fin_pre = 0, PREAMBLE_LEN
for i in range(ini_num, len(lines)):
    is_sum =  check_is_sum(lines[ini_pre:fin_pre], lines[i])
    if not is_sum:
        print('{} cannot be written as sum of previous {} numbers'.format(lines[i], PREAMBLE_LEN))
        break

    ini_pre += 1
    fin_pre += 1

get_num(lines, lines[i])
