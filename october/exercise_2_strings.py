# задание 2
"""
Придумайте такую строку (на любом знакомом Вам языке),чтобы она состояла из трех других (повторы строки разрешены).
Напишите код. Если вы можете сделать это более, чем одним способом, напишите все способы
"""

str_1 = 'Посмотрев на нее, он сказал'
str_2 = 'Просто процитирую тебе фразу из рассказа Борхеса'
str_3 = 'Авэрроэс желал представить себе, что такое драма, не подозревая при этом, что есть театр...'

final_str = str_1 + ': ' + str_2 + ' - ' + '\"' + str_3 + '\"'
print(final_str)

################
# version 2
################


str_list = [str_1, str_2, str_3]
signs = [': ', ' - ', '\"']

final_str = str_list[0] + signs[0] + str_list[1] + signs[1] + signs[2] + str_list[2] + signs[2]

print()
print('version 2:')
print(final_str)

