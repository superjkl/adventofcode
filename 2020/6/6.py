
def get_groups():
    ''' [ [set(), ...], ... ] '''
    with open('2020/6/6.input') as file:
        groups = file.read().strip().split('\n\n')
        groups = [[set([q for q in person]) for person in group.split('\n')] for group in groups]
        return groups

def group_answered_questions(group):
    s = set.union(*group)
    return len(s)

def group_common_questions(group):
    s = set.intersection(*group)
    return len(s)


groups = get_groups()

print(sum(map(group_answered_questions, groups)))
print(sum(map(group_common_questions, groups)))