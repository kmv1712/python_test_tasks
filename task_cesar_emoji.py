position_shift, input_emoji  = int(input()), input()
list_input_emoji = [input_emoji[i: i+1] for i in range(0, len(input_emoji), 1)]
start, end, offset = 128512, 128591, position_shift
# Получим список со сдвигом.
result = [(chr( start + (ord(emoji) - start + offset) % (end - start + 1))) for emoji in list_input_emoji]
print('Result: \"{}\"'.format(''.join(result)))
