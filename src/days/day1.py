

def day1_part1():
    input_file: str = "./inputs/day1-part1-example.txt"
    with open(input_file) as file:
        lines = [line.rstrip() for line in file]
    
    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    running_total = 0

    for l in lines:
        x, y = 0, len(l)-1
        num = ''

        while x <= len(l)-1:
            if l[x].isdigit():
                num = l[x]
                break
            else:
                x += 1

        while y > 0 or y == x:
            if l[y].isdigit():
                num = num + l[y]
                break
            else:
                y -= 1

        running_total += int(num)
    
    return running_total

