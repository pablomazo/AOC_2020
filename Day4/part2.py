def validate_field(field, value):
    valid = False
    if field == 'byr':
        valid = 1920 <= int(value) <= 2002

    elif field == 'iyr':
        valid = 2010 <= int(value) <= 2020

    elif field == 'eyr':
        valid = 2020 <= int(value) <= 2030

    elif field == 'hgt':
        if value[-2:] == 'cm': valid = 150 <= int(value[:-2]) <= 193
        if value[-2:] == 'in': valid = 59 <= int(value[:-2]) <= 76

    elif field == 'hcl':
        valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'a', 'b', 'c', 'd', 'e', 'f']
        vals = list(value[1:])
        valid = len(vals) == 6 and all([val in valid_chars for val in vals])

    elif field == 'ecl':
        valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    elif field == 'pid':
        valid = len(list(value)) == 9

    elif field == 'cid':
        valid = True

    return valid

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
valid_fields = []
for i, line in enumerate(lines):
    new = False

    if not new:
        for elem in line.split():
            field = elem.split(':')[0]
            value = elem.split(':')[1]
            fields.append(field)
            valid_fields.append(validate_field(field, value))

    if line == '\n' or i == len(lines) - 1:
        new = True
        fields.sort()
        if 'cid' in fields: fields.remove('cid')

        if fields == requiered_fields and all(valid_fields): nvalid += 1

        fields = []
        valid_fields = []

print('Valid passports:', nvalid)
