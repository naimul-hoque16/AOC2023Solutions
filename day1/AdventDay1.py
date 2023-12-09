"""
There are two parts to this problem. This first goal is to find the first and last digit in a string, concatenate,
and take the sum to come up with the solution. For the second part, numbers spelled out need to be considered in 
the calculation.
"""
if __name__ == '__main__':
    string_representation_of_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    nums = []
    with open('advent_day_1_input.txt', 'r') as fd:
        while True:
            line = fd.readline()
            index_value_pairs = []
            if not line:
                break
            else:
                line = line.strip()
                left_ptr, right_ptr = 0, len(line) - 1
                left_value, right_value = None, None
                while not left_value or not right_value:
                    if line[left_ptr].isnumeric():
                        left_value = int(line[left_ptr])

                    if line[right_ptr].isnumeric():
                        right_value = int(line[right_ptr])
                    
                    if not left_value:
                        left_ptr += 1
                    if not right_value:
                        right_ptr -= 1
                index_value_pairs.append((left_ptr, left_value))
                index_value_pairs.append((right_ptr, right_value))
                leftmost_index, leftmost_value = len(line) - 1, 0
                rightmost_index, rightmost_value = 0, 0
                for item, value in string_representation_of_digits.items():
                    substring_index = line.find(item)
                    reverse_substring_index = line.rfind(item)
                    if substring_index != -1:
                        if substring_index < leftmost_index:
                            leftmost_index = substring_index
                            leftmost_value = value
                    if reverse_substring_index != -1:
                        if reverse_substring_index > rightmost_index:
                            rightmost_index = reverse_substring_index
                            rightmost_value = value
                if leftmost_value != 0:
                    index_value_pairs.append((leftmost_index, leftmost_value))
                if rightmost_value != 0:
                    index_value_pairs.append((rightmost_index, rightmost_value))
                index_value_pairs.sort()
                num = index_value_pairs[0][1] * 10 + index_value_pairs[-1][1]
                nums.append(num)
    print(sum(nums))