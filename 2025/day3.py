def main():
    lines = read_lines("input3.txt")
    joltage = joltage_sum(lines)
    print(f"Total joltage: {joltage}")

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines

def locate_max(line):
    max_joltage = 0
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            joltage = 10*int(line[i])+int(line[j])
            if joltage > max_joltage:
                max_joltage = joltage

    return max_joltage

def joltage_sum(lines):
    total_joltage = 0
    for line in lines:
        total_joltage += locate_max_v2(line, 12)
    return total_joltage

def locate_max_v2(line, n_digits):
    max_joltage = 0
    start_loc = 0
    for i in range(n_digits):
        end_loc = len(line) - n_digits + i + 1
        max_digit = 0
        start_inc = 0
        for j in range(start_loc, end_loc):
            if int(line[j]) > max_digit:
                max_digit = int(line[j])
                start_inc = j
        start_loc = start_inc + 1
        max_joltage = 10*max_joltage + max_digit
    # print(f"Max joltage for line {line} is {max_joltage}")
    return max_joltage

if __name__ == "__main__":
    main()