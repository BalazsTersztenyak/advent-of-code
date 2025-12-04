def main():
    lines = read_lines("input4.txt")
    matrix = create_matrix(lines)
    result = locate_free_rolls_v2(matrix)
    print(result)

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines

def create_matrix(lines):
    matrix = []
    for line in lines:
        row = []
        for cell in line:
            row.append(1 if cell == '@' else 0)
        matrix.append(row)
    return matrix

def locate_free_rolls(matrix):
    num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                if check_neighbours(matrix, i, j):
                    num += 1
    return num

def locate_free_rolls_v2(matrix):
    num = 0
    num_round = -1
    while num_round != 0:
        num_round = 0
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    if check_neighbours(matrix, i, j):
                        num_round += 1
                        matrix[i][j] = 0
        num += num_round
    return num

def check_neighbours(matrix, i, j):
    xmin = 0
    xmax = len(matrix) - 1
    ymin = 0
    ymax = len(matrix[0]) - 1

    xmin = max(xmin, i - 1)
    xmax = min(xmax, i + 1)
    ymin = max(ymin, j - 1)
    ymax = min(ymax, j + 1)

    count = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if x == i and y == j:
                continue
            if matrix[x][y] == 1:
                count += 1
    return count < 4

if __name__ == "__main__":
    main()