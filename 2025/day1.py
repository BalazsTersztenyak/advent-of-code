def main():
    lines = read_lines("input1a.txt")

    count = count_zeros_v1(lines)
    count = count_zeros_v2(lines)
    print(count)

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
    
def count_zeros_v1(lines):
    zero_count = 0
    dial = 50
    for line in lines:
        if line.startswith("L"):
            dial -= int(line[1:])
        elif line.startswith("R"):
            dial += int(line[1:])
        dial %= 100
        if dial == 0:
            zero_count += 1
    return zero_count

def count_zeros_v2(lines):
    zero_count = 0
    dial = 50
    for line in lines:
        direction = True if line.startswith("R") else False
        amount = int(line[1:])
        if direction:
            for _ in range(amount):
                dial += 1
                dial %= 100
                if dial == 0:
                    zero_count += 1
        else:
            for _ in range(amount):
                dial -= 1
                dial %= 100
                if dial == 0:
                    zero_count += 1
    return zero_count

if __name__ == "__main__":
    main()