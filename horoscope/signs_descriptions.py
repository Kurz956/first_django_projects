signs = {
    'aries': ['Fire', "♈", '1', "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
              [i for i in range(80,111)]],
    'taurus': ['Earth', "♉", '2', "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
               [i for i in range(111,141)]],
    'gemini': ['Air', "♊", '3', "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
               [i for i in range(141,172)]],
    'cancer': ['Water', "♋", '4', "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
               [i for i in range(172,202)]],
    'leo': ['Fire', "♌", '5', "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
            [i for i in range(202,234)]],
    'virgo': ['Earth', "♍", '6', "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
              [i for i in range(234,267)]],
    'libra': ['Air', "♎", '7', "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
              [i for i in range(267,297)]],
    'scorpio': ['Water', "♏", '8', "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
                [i for i in range(297,324)]],
    'sagittarius': ['Fire', "♐", '9', "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
                    [i for i in range(324, 357)]],
    'capricorn': ['Earth', "♑", '10', "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
                  [i for i in range(357,366)] + [i for i in range(1,21)]],
    'aquarius': ['Air', "♒", '11', "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
                 [i for i in range(21,51)]],
    'pisces': ['Water', "♓", '12', "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
               [i for i in range(51,80)]],
}

class Sign:
    def __init__(self, name:str, type:str, picture:str, description:str, index:str, date:list):
        self._name = name
        self._type = type
        self._picture = picture
        self._description = description
        self._index = index
        self._date = date
    def __repr__(self):
        return str(self._name)
    def get_sign(self):
        return self.__dict__


zodiac_signs = {}
for sign, desc in signs.items():
    zodiac_signs[sign] = Sign(name=sign, type=desc[0], picture=desc[1], index=desc[2], description=desc[3], date=desc[4])