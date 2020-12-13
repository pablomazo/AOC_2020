import difflib
def in_bags(rules, color):
    enters = []
    for rule in rules:
        bag = rule[0]
        colors = rule[1]
        #print(color, bag, colors)

        if color in colors:
            enters.append(bag)
            new = in_bags(rules, bag)
            enters += new
    return enters

with open('input', 'r') as f:
    lines = f.readlines()

def bags_in_bags(rules, color, number):
    nbags = 0
    for rule in rules:
        bag = rule[0]
        colors = rule[1]
        n_in = rule[2]

        if bag == color and 'end' not in colors:
            for [c, n] in zip(colors, n_in):
                nbags += number * n
                nbags += bags_in_bags(rules, c, number * n)

    return nbags


# Make list with all posible bags and what contain:
rules = []

for line in lines:
    line = line.strip()
    line = line.replace('.', '')
    line = line.replace(',', '')
    line = line.replace('bag ', 'bags')
    line = line.replace('\n', '')

    line = line.split('contain')
    bag = line[0].split('bags')[0].strip()
    contains = line[1].split('bags')
    inside = []
    number_inside = []
    for contain in contains:
        split = contain.split()
        lenght = len(split)
        if lenght == 2:
            inside.append('end')
        if lenght > 2:
            color = split[1] + ' ' + split[2]
            number = split[0]
            inside.append(color.strip())
            number_inside.append(int(number))

    rules.append([bag, inside, number_inside])


ini = 'shiny gold'
enters = []

# Part 1
#enters =  in_bags(rules, ini)
#print(len(set(enters)))


# Part 2
nbags = bags_in_bags(rules, ini, 1)
print(nbags)
