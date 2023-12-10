if __name__ == '__main__':
    with open('advent_of_code_day_3.txt', 'r') as fd:
        y = 0
        sum = 0
        nums = []
        symbol_coordinates = {}
        star_coordinates = []
        gear_ratios = {}
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
                    if line[start_x] == '*':
                        star_coordinates.append((start_x, y))
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
                            sum += value
                            is_found = True
                            if (test_x, test_y) in star_coordinates:
                                if not gear_ratios.get((test_x, test_y)):
                                    gear_ratios[(test_x, test_y)] = []
                                gear_ratios[(test_x, test_y)].append(value)
                            break
                if is_found:
                    break
    gear_ratio_total = 0
    for coordinate, ratio in gear_ratios.items():
        if len(ratio) == 2:
            gear_ratio_total += (ratio[0] * ratio[1])
    print(gear_ratio_total)