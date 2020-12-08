'''
out of all given colors how many can contain a gold bag

so this is a grammar, assumed that all grammars are finitely terminal
just need to use each rewriting rule

can memoize
want to find if terminal is gold
for each color save if gold, otherwise compute it
'''


def memoize_single_arg(func):
    args_seen = {}

    def wrapper(arg):
        if arg not in args_seen:
            result = func(arg)
            args_seen[arg] = result
        return args_seen[arg]

    return wrapper


def get_bags(path):
    with open(path) as file:
        def bag_with_contents(bag_str):
            def process_bag_str(string):
                bag_w_count = string.rstrip('.').rstrip('bag').rstrip('bags').rstrip().lstrip()
                tokens = bag_w_count.split()
                count = tokens[0]
                color = ' '.join(tokens[1:])
                return { 'color': color, 'count': int(count) }

            bag_str = bag_str.rstrip('.')
            if "bags contain no other bags" in bag_str:
                color = bag_str.split('bags contain no other bags')[0].strip()
                return { 'color': color, 'contents': {} }
            else:
                color, bag_list_str = bag_str.split(' bags contain ')
                bag_list_str = bag_list_str.split(', ')
                bag_dict = { bag['color']: bag for bag in list(map(process_bag_str, bag_list_str))}
                return { 'color': color, 'contents': bag_dict }

        bags = file.read().strip().split('\n')
        return { bag['color']: bag for bag in list(map(bag_with_contents, bags))}
 
bag_rules = get_bags('2020/7/7.input')

@memoize_single_arg
def bag_contains_shiny_gold(color):
    bag_contents = bag_rules[color]['contents']
    for color in bag_contents:
        if bag_contains_shiny_gold(color) or (color == 'shiny gold'):
            return True
    return False

@memoize_single_arg
def bags_contained_count(color):
    bag_contents = bag_rules[color]['contents']
    bags_count = 0
    for color, bag in bag_contents.items():
        bags_count += bag['count']
        bags_count += bag['count'] * bags_contained_count(color)
    return bags_count


print(sum(map(int, map(bag_contains_shiny_gold, bag_rules.keys()))))

print(bags_contained_count('shiny gold'))