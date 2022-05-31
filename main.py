a = 1
b = 2
c = 3
d = 4
e = 5
f = 8
g = 3
h = 5
i = 1
j = 1
k = 2
l = 3
m = 4
n = 5
o = 7
p = 8
q = 1
r = 2
s = 3
t = 4
u = 6
v = 6
w = 6
x = 5
y = 1
z = 7


def init_input(text):
    input_value = input(f'{text} : ').lower()
    return input_value


def init_compound(word):
    if word:
        letter_list = ''
        for letter in list(word):
            if letter_list:
                letter_list += ' + ' + letter
            else:
                letter_list = letter
        word_compound = eval(letter_list)
    else:
        word_compound = 0
    return word_compound


def init_singular(num):
    len_num = len(str(num))
    if len_num == 1 or num == 11 or num == 22:
        num = int(num)
    else:
        num = str(num)
        while len_num != 1:
            num_list = ''
            for letter in list(num):
                if num_list:
                    num_list += ' + ' + letter
                else:
                    num_list = letter
            num = eval(num_list)
            len_num = len(str(num))
    return num


if __name__ == '__main__':
    first_name = init_input('Enter Your First Name')

    need_mid = init_input('Do You Have Mid Name ( y or n )')
    if need_mid == 'y':
        mid_name = init_input('Enter Your Mid Name ')

        mid_name_num = init_compound(mid_name)
        mid_name_compound = mid_name_num

        mid_name_singular = init_singular(mid_name_compound)

    else:
        mid_name_num = mid_name_singular = mid_name_compound = 0

    last_name = init_input('Enter Your Last Name')

    first_name_num = init_compound(first_name)
    first_name_compound = first_name_num

    last_name_num = init_compound(last_name)
    last_name_compound = last_name_num

    first_name_singular = init_singular(first_name_compound)

    last_name_singular = init_singular(last_name_compound)

    compound_key = first_name_singular + mid_name_singular + last_name_singular
    singular_key = init_singular(compound_key)

    print('\n')
    print('Full Name : ', first_name + ' ' + last_name)
    print('first_name_singular : ', first_name_singular)
    print('mid_name_singular : ', mid_name_singular) if mid_name_singular != 0 else ''
    print('last_name_singular : ', last_name_singular)
    print('first_name_compound : ', first_name_compound)
    print('mid_name_compound : ', mid_name_compound) if mid_name_compound != 0 else ''
    print('last_name_compound : ', last_name_compound)
    print('compound_key : ', compound_key)
    print('singular_key : ', singular_key)
