with open('input', 'r') as f:
    lines = f.readlines()

requiered_fields = [
    'byr',
    'ecl',
    'eyr',
    'hcl',
    'hgt',
    'iyr',
    'pid',
        ]

new = True
fields = []
nvalid = 0
for i, line in enumerate(lines):
    new = False

    if not new:
        for elem in line.split():
            field = elem.split(':')[0]
            fields.append(field)

    if line == '\n' or i == len(lines) - 1:
        new = True
        fields.sort()
        if 'cid' in fields: fields.remove('cid')

        if fields == requiered_fields: nvalid += 1

        fields = []

print('Valid passports:', nvalid)
