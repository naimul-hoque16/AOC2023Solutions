MAX_GREEN = 13
MAX_RED = 12
MAX_BLUE = 14

max_color_values = {
    "green": MAX_GREEN,
    "red": MAX_RED,
    "blue": MAX_BLUE
}

if __name__ == '__main__':
    with open('advent_of_code_day_2.txt', 'r') as fd:
        valid_game_sum = 0
        while True:
            line = fd.readline()
            if not line:
                break
            line = line.strip()
            splitted_text = line.split(':')
            game_id = int(splitted_text[0].split('Game ')[-1])
            hands = splitted_text[-1].strip().split(';')
            is_valid_hand = True
            for hand in hands:
                individual_color_set = hand.strip().split(',')
                for color_set in individual_color_set:
                    color_details = color_set.strip().split(' ')
                    color_value = color_details[0]
                    color = color_details[1]
                    if int(color_value) > max_color_values[color]:
                        is_valid_hand = False
                        break
            if is_valid_hand:
                valid_game_sum += game_id
    print(valid_game_sum)




