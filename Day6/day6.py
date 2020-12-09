with open('input', 'r') as f:
    lines = f.readlines()

yes = 0
letters = []
npeople = 0
for line in lines:
    if line == '\n':
        print(letters, npeople)
        for elem in set(letters):
            if letters.count(elem) == npeople: yes += 1
        print(yes)
        letters = []
        npeople = 0

    else:
        let = list(line[:-1])
        letters += let
        npeople += 1

print('Number of yes:', yes)
