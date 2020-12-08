'''
7 - {F,B} front/back paritioning 0-127 rows
3 - {L,R} left/right partitioning 0-7 rows

FBFBFBFLLR
decode to (row, col)
seat id is (row * 8) + col

'''

def binary_search(partitions, nums):
    if len(nums) == 1:
        return nums[0]
    elif len(partitions) == 0:
        return -1

    nums_smaller = nums[:int(len(nums)/2)]
    nums_larger = nums[int(len(nums)/2):]
    direction = partitions[0]
    partitions = partitions[1:]
    return binary_search(partitions, nums_smaller if direction == 'S' else nums_larger)


def get_passes():
    with open('2020/5/5.input') as file:
        passports = [ (bpass[0:7], bpass[7:10]) for bpass in file.read().strip().split('\n')]
        return passports

def decode_pass(bpass):
    row_part, col_part = bpass

    def partitions(parts):
        part_map = { # map to smaller or larger partition
            'F': 'S',
            'B': 'L',
            'L': 'S',
            'R': 'L',
        }
        return list(map(lambda p : part_map[p], parts))

    # binary search through nums 2^^7 row and 2^^3 for col
    row = binary_search(partitions(row_part), range(128))
    col = binary_search(partitions(col_part), range(8))
    return (row, col)

def seat_id(decoded):
    row, col = decoded
    return (row * 8) + col

passes = get_passes()
decoded = list(map(decode_pass, passes))
print(max(list(map(seat_id, decoded))))


# all seats are contiguous in seat ids

seat_ids = list(map(seat_id, decoded))
seat_ids.sort()
for i, seat_id in enumerate(seat_ids):
    if seat_ids[i+1] != (seat_id + 1):
        print(seat_id + 1)
        break