# ///
# Напишите программу, которая определяет, бьёт ли одна карта другую.
# Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
# Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
# Если карты разных мастей и нет козырных, то никто не побеждает.
# C, D, H, S (clubs, diamonds, hearts, or spades ) булав, алмазов, сердец или пиков
# 6, 7, 8, 9, 10, J, Q, K, A
# Формат ввода:
# На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке указывается козырная масть.
# Формат вывода:
# Программа должна вывести слово
# First, если первая карта бьёт вторую,
# Second, если вторая карта бьёт первую,
# Error, если ни одна из карт не может побить другую.
# Sample Input 1:
# AH JH
# D
#
def get_who_covers_card(default_value, value_fc, value_sc):
    """Получить порядок карты которая кроет.

    Args:
        default_value: Значения карт(6, .., король, туз)
        value_fc: Знасение первой карты.
        value_sc: Значение второй карты.

    Returns:
        str
    """
    if default_value.index(value_fc) > default_value.index(value_sc):
        return "First"
    elif default_value.index(value_fc) == default_value.index(value_sc):
        return "Error"
    elif default_value.index(value_fc) < default_value.index(value_sc):
        return "Second"

string_input = input()
mast_kozir = input()
string_input = string_input.split(' ')
first_card, second_card = string_input[0], string_input[1]
first_card, second_card = list(first_card), list(second_card)
default_value = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# TODO: Исправить. Не учел, что может быть 10А, пришлось городить костыль.
if len(first_card) == 3:
    value_fc, mast_fc = '{0}{1}'.format(first_card[0], first_card[1]), first_card[2]
else:
    value_fc, mast_fc = first_card[0], first_card[1]
if len(second_card) == 3:
    value_sc, mast_sc = '{0}{1}'.format(second_card[0], second_card[1]), second_card[2]
else:
    value_sc, mast_sc = second_card[0], second_card[1]

if mast_kozir == mast_fc and mast_kozir != mast_sc:
    print("First")
elif mast_kozir == mast_fc and mast_kozir == mast_sc:
    print(get_who_covers_card(default_value, value_fc, value_sc))
elif mast_kozir != mast_fc and mast_kozir == mast_sc:
    print("Second")
elif mast_kozir != mast_fc and mast_kozir != mast_sc:
    if mast_fc == mast_sc:
        print(get_who_covers_card(default_value, value_fc, value_sc))
    else:
        print("Error")
