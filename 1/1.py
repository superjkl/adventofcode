# sums are a strict subset of the cartesian product
# so need to compute  (a,b), a ∈ A, b ∈ (A \ a)
# instead just iterate over the list
from pprint import pprint

def get_list():
    with open('1/1.input') as file:
        return list(map(lambda x : int(x), file.read().split()))

sum_target = 2020
nums = get_list()
indexed_entries = list(zip(range(len(nums)), nums))
answers = [
    a * b 
    for i1, a in indexed_entries
    for i2, b in indexed_entries
    if (i1 != i2) and (a + b == sum_target)
    ]
print(list(answers))
answers = [
    a * b * c
    for i1, a in indexed_entries
    for i2, b in indexed_entries
    for i3, c in indexed_entries
    if len(set([i1,i2,i3])) == 3 and (a + b + c == sum_target)
    ]
print(list(answers))


