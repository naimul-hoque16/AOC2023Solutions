if __name__ == '__main__':
    with open('advent_of_code_day_3.txt', 'r') as fd:
        y = 0
        sum = 0
        nums = []
        symbol_coordinates = {}
        while True:
            line = fd.readline()
            if not line:
                break
            line = line.strip()
            start_x = 0
            while start_x < len(line):
                tmp = []
                num_starts = 0
                num_ends = 0
                if line[start_x].isnumeric():
                    num_starts = start_x
                    while start_x < len(line) and line[start_x].isnumeric():
                        tmp.append(line[start_x])
                        start_x += 1
                    num_ends = start_x - 1
                    nums.append((int(''.join(tmp)), [num_starts, num_ends], y))
                elif line[start_x] != '.':
                    if not symbol_coordinates.get(y):
                        symbol_coordinates[y] = []
                    symbol_coordinates[y].append(start_x)
                    start_x += 1
                else:
                    start_x += 1
            y += 1
        for item in nums:
            value, x_coord, y_coord = item
            for x in range(x_coord[0], x_coord[1] + 1):
                is_found = False
                for coordinate in [(x, y_coord + 1), (x, y_coord - 1), (x + 1, y_coord), (x - 1, y_coord), (x + 1, y_coord - 1), (x + 1, y_coord + 1), (x - 1, y_coord + 1), (x - 1, y_coord - 1)]:
                    test_x, test_y = coordinate
                    if symbol_coordinates.get(test_y):
                        if test_x in symbol_coordinates.get(test_y):
                            print(f'Value {value} is adjacent to {(test_x, test_y)}')
                            sum += value
                            is_found = True
                            break
                if is_found:
                    break
