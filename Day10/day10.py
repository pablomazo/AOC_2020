from scipy.special import comb

with open('input', 'r') as f:
    lines = [int(l) for l in f.read().splitlines()]

# Sort adapters:
lines.append(0)
lines.append(max(lines) + 3)
lines.sort()

check_jolt = 0
diff_list = []

n1 = 0
n3 = 0
for jolt in lines:
    diff = jolt - check_jolt
    check_jolt = jolt
    if diff == 1:
        n1 += 1
    elif diff == 3:
        n3 += 1

print(n1 * n3)



D = {}
def get_narr(lines, i0):
    narr = 0
    if i0 == len(lines) - 1:
        return 1

    if i0 in D:
        return D[i0]

    for i in range(i0+1, len(lines)):
        if lines[i] - lines[i0] <= 3:
            narr += get_narr(lines, i)

    D[i0] = narr

    return narr

narr = get_narr(lines, 0)
print(narr)
