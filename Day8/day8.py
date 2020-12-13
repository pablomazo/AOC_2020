with open('input', 'r') as f:
    lines = f.read().splitlines()



def eval_acumulator(lines):
    ind = 0
    history = [ind]
    op_list = []

    acc_val = 0

    cont = True
    while cont:
        [op, arg] = lines[ind].split()
        arg = int(arg)

        new_ind = ind + 1
        acc = 0
        if op == 'acc':
            acc += arg

        elif op == 'jmp':
            new_ind += arg - 1

        if new_ind not in history and new_ind < len(lines):
            history.append(new_ind)
            acc_val += acc
            ind = new_ind
        else:
            cont = False
    return acc_val, history

# Part 1
acc_val, _ = eval_acumulator(lines)
print('Accumulator:', acc_val)


# Part 2
for i, line in enumerate(lines):
    [op, arg] = line.split()
    if op == 'jmp':
        new_line = 'nop {}'.format(arg)
        lines_cp = lines.copy()
        lines_cp[i] = new_line
        acc_val, hist = eval_acumulator(lines_cp)
        if len(lines_cp) - 1 in hist:
            print('Operation {} {} with index {} changed'.format(op, arg, i))
            print('Accumulator:', acc_val)
    elif op == 'nop':
        new_line = 'jmp {}'.format(arg)
        lines_cp = lines.copy()
        lines_cp[i] = new_line
        acc_val, hist = eval_acumulator(lines_cp)
        if len(lines_cp) - 1 in hist:
            print('Operation {} with index {} changed'.format(op, i))
            print('Accumulator:', acc_val)


