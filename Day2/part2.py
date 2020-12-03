
line = True
nvalid, nincorrect = 0, 0
with open('input', 'r') as f:
    while line:
        # Read each line in input file:
        line = f.readline().split()

        if line:
            # Split line into minimum and maximum occurrence of a letter and password.
            ind1, ind2 = int(line[0].split('-')[0]), int(line[0].split('-')[1])
            letter = line[1].split(':')[0]
            passwd = list(line[2])

            # Get the items in possitions ind1 and ind2 (indexes in passwd start 
            # with index 1).
            items = [passwd[ind1-1], passwd[ind2-1]]
            occ = items.count(letter)

            # The password is valid if only one occurrence is counted.
            if (occ == 1):
                nvalid += 1
            else:
                nincorrect += 1

print('Number of valid passwords:', nvalid)
print('Number of incorrect passwords:', nincorrect)
