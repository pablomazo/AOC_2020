
line = True
nvalid, nincorrect = 0, 0
with open('input', 'r') as f:
    while line:
        # Read each line in input file:
        line = f.readline().split()

        if line:
            # Split line into minimum and maximum occurrence of a letter and password.
            min_occ, max_occ = int(line[0].split('-')[0]), int(line[0].split('-')[1])
            letter = line[1].split(':')[0]
            passwd = list(line[2])

            # Count occurrences of letter in passwd.
            occ = passwd.count(letter)

            # If the number of occurrences in password is between min_occ and max_occ
            # it is valid.
            if (min_occ <= occ <= max_occ):
                nvalid += 1
            else:
                nincorrect += 1

print('Number of valid passwords:', nvalid)
print('Number of incorrect passwords:', nincorrect)
