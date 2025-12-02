def main():
    lines = read_lines("input2a.txt")
    # lines = read_lines("test2a.txt")
    # lines = read_lines("2025/test2a.txt")
    line = lines[0]
    ranges = split_ranges(line)
    invalid = count_invalid_ids_v1(ranges)
    invalid = count_invalid_ids_v2(ranges)
    print(invalid)

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines

def split_ranges(line):
    ranges = []
    parts = line.split(",")
    for part in parts:
        range = tuple(map(int, part.split("-")))
        ranges.append(range)
    return ranges

def count_invalid_ids_v1(ranges):
    invalid_sum = 0
    for r in ranges:
        start = r[0]
        end = r[1]
        for id_num in range(start, end + 1):
            id_str = str(id_num)
            if len(id_str) % 2 == 1:
                continue
            if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
                invalid_sum += id_num
    return invalid_sum

def count_invalid_ids_v2(ranges):
    invalids = set()
    for r in ranges:
        start = r[0]
        end = r[1]
        repeat = len(str(end))
        for rep in range(2, repeat+1):
            for id_num in range(start, end + 1):
                id_str = str(id_num)
                if len(id_str) % rep != 0:
                    continue
                does_repeat = False
                for i in range(1, rep):
                    if id_str[:len(id_str)//rep] != id_str[i*(len(id_str)//rep):(i+1)*(len(id_str)//rep)]:
                        does_repeat = False
                        break
                    does_repeat = True
                if does_repeat:
                    invalids.add(id_num)
                    # print(f"Found invalid ID: {id_num} in range {r} with repeat {rep}")

    invalid_sum = sum(invalids)
    return invalid_sum

if __name__ == "__main__":
    main()