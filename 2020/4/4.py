def get_passports():
    with open('2020/4/4.input') as file:
        passports = file.read().strip().split('\n\n')
        dicts = []
        for p in passports:
            fields = p.replace('\n', ' ').split()
            passport = {}
            for f in fields:
                key, val = f.split(':')
                passport[key] = val
            dicts.append(passport)
        return dicts


def is_valid(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid
    return int(all(map(lambda f : f in passport, req_fields)))

def validation(passport):
    def hgt(s):
        unit = s[-2:]
        if unit not in ['cm', 'in']:
            return False
        if unit == 'cm':
            return 150 <= int(s[0:-2]) <= 193
        else:
            return 59 <= int(s[0:-2]) <= 76
    
    def hcl(s):
        sym = s[0:1]
        num = s[1:]
        if sym != '#':
            return False
        return len(num) == 6 and all(map(lambda c : c.isdigit() or c in ['a', 'b', 'c', 'd', 'e', 'f'], num))
    
    def ecl(s):
        return s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def pid(s):
        return len(s) == 9 and s.isdigit()

    rules = [
        ('byr', lambda x : 1920 <= int(x) <= 2002),
        ('iyr', lambda x : 2010 <= int(x) <= 2020),
        ('hgt', hgt),
        ('eyr', lambda x : 2020 <= int(x) <= 2030),
        ('hcl', hcl),
        ('ecl', ecl),
        ('pid', pid)
    ]

    return all(map(lambda p : p[1](passport[p[0]]), rules))


print(sum(list(map(is_valid, get_passports()))))


print(sum(list(map(lambda p : is_valid(p) and validation(p), get_passports()))))
