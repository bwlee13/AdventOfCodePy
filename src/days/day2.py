import re

def day2_part1():
    """
    12 red, 13 green, 14 blue 
    """
    input_file: str = "./inputs/day2-part1-example.txt"
    with open(input_file) as file:
        lines = [l.rstrip() for l in file]
    
    comp_dict = {"red": 12, "green": 13, "blue": 14}
    
    matches = 0
    for l in lines:
        pattern = r'(\d+) (\w+)'
        color_dict = {}

        for number, color in re.findall(pattern, l):
            if color not in color_dict or color_dict[color] < int(number):
                color_dict[color] = int(number)
        
        possible = False
        for k, v in color_dict.items():
            if v > comp_dict[k]:
                possible = False
                break
            else:
                possible = True

        if possible:
            game_num_pattern = r'Game (\d+):'
            game_num = re.search(game_num_pattern, l)

            if game_num:
                game_num = int(game_num.group(1))
                matches += game_num
            else:
                raise ValueError("Game num not found")
            

    return matches


def gen_lines():
    input_file: str = "./inputs/day2-part1-input.txt"
    with open(input_file) as file:
        for line in file:
            yield line.rstrip()


def day2_part2():
    line = gen_lines()
    running_total = 0

    try:
        while True:
            color_dict = {}
            l = next(line)
            print(l)
            pattern = r'(\d+) (\w+)'

            for number, color in re.findall(pattern, l):
                if color not in color_dict:
                    color_dict[color] = int(number) 
                else:
                    color_dict[color] = max(int(number), color_dict[color])
            print(color_dict)

            pwr = None
            for k, v in color_dict.items():
                if not pwr:
                    pwr = v
                else:
                    pwr *= v
            
            running_total += pwr

    except StopIteration:
        print("Done")

    return running_total
    