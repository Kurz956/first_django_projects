signs = {
    'aries': ['Fire', "♈", '1', "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)."],
    'taurus': ['Earth', "♉", '2', "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)."],
    'gemini': ['Air', "♊", '3', "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)."],
    'cancer': ['Water', "♋", '4', "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)."],
    'leo': ['Fire', "♌", '5', "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)."],
    'virgo': ['Earth', "♍", '6', "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)."],
    'libra': ['Air', "♎", '7', "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)."],
    'scorpio': ['Water', "♏", '8', "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)."],
    'sagittarius': ['Fire', "♐", '9', "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)."],
    'capricorn': ['Earth', "♑", '10', "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)."],
    'aquarius': ['Air', "♒", '11', "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)."],
    'pisces': ['Water', "♓", '12', "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."]
}

class Sign:
    def __init__(self, name:str, type:str, picture:str, description:str, index:str):
        self._name = name
        self._type = type
        self._picture = picture
        self._description = description
        self._index = index

    def __repr__(self):
        return str(self._name)
    def get_sign(self):
        return self.__dict__

zodiac_signs = {}
for sign, desc in signs.items():
    zodiac_signs[sign] = Sign(name=sign, type=desc[0], picture=desc[1], index=desc[2], description=desc[3])

print(zodiac_signs)
print(zodiac_signs['leo'].get_sign())

year = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
m = 2
print(year[m])
# raw = f'{zodiac_signs["leo"]._description}'
# print(raw)
# for sign, index in zodiac_signs.items():
#     if index._index == '1':
#         a = sign
#         print(a)
# #types = set()
# #for type in zodiac_signs.values():
# #    types.add(type._type)
# types = sorted({type._type for type in zodiac_signs.values()})
# print(types)
# element = 'Air'
# zodiacs = list(zodiac_signs.keys())
# response = '<ol>'
# for sign in zodiacs:
#     redirect_path = 'redirect_path'
#     if zodiac_signs[sign]._type == element:
#         response += f'<li><a href=\'{redirect_path}\'>{sign.title()}</a></li>'
# response += '</ol>'
# print()

# signs1 = {
#     'aries': ['Fire', "♈", 1, "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)."],
#     'taurus': ['Earth', "♉", 2, "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)."],
#     'gemini': ['Air', "♊", 3, "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)."],
#     'cancer': ['Water', "♋", 4, "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)."],
#     'leo': ['Fire', "♌", 5, "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)."],
#     'virgo': ['Earth', "♍", 6, "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)."],
#     'libra': ['Air', "♎", 7, "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)."],
#     'scorpio': ['Water', "♏", 8, "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)."],
#     'sagittarius': ['Fire', "♐", 9, "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)."],
#     'capricorn': ['Earth', "♑", 10, "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)."],
#     'aquarius': ['Air', "♒", 11, "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)."],
#     'pisces': ['Water', "♓", 12, "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."]
# }
