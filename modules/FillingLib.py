from random import choice, randint


class Filler:

    def __init__(self):
        self.rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщыэюя"  # русский алфавит без ьъ
        self.eng_alphabet = "abcdefghijklmnopqrstuvwxyz"  # английский алфавит
        self.cities = ["Краснодар", "Кропоткин", "Сыктывкар", "Бердянск", "Тихорецк"]  # список городов для генератора
        self.street = ["Калинина", "Трубилина", "Марса", "Пасито", "Нефтяников"]  # список улиц для генератора
        self.names = ["Дмитрий", "Василий", "Никита", "Артем", "Антон", "Борис", "Григорий", "Владислав", "Николай",
                      "Егор", "Анатолий",
                      "Степан", "Тимофей", "Ярослав", "Павел", "Федор", "Константин", "Максим"]  # список мужских имен
        self.names_female = ["Екатерина", "Алина", "Марина", "Ангелина", "Анна", "Анастасия", "Елена", "Дарья",
                             "Светлана",
                             "Агафья",
                             "Аделина", "Карина", "Вера",
                             "Валерия", "Наталья", "Александра", "Кира", "Алла"]  # список женских имен
        self.families_female = ["Петрова", "Иванова", "Сидорова", "Пивоварова", "Сергеева", "Болотинская", "Павленко",
                                "Петренко",
                                "Хомухина", "Смирнова", "Фешина", "Попова", "Соколова", "Михайлова", "Кашка",
                                "Мелихова",
                                "Царицынская"]  # список женских фамилий
        self.families = ["Петров", "Иванов", "Сидоров", "Пивоваров", "Сергеев", "Болотинский", "Павленко", "Петренко",
                         "Хомухин"]  # список мужских фамилий
        self.otches = ["Петрович", "Дмитриевич", "Владимирович", "Павлович", "Сергеевич", "Григорьевич", "Николаевич",
                       "Егорович", "Васильевич"]  # список мужских отчеств
        self.otches_female = ["Петровна", "Дмитриевна", "Владимировна", "Павловна", "Сергеевна", "Григорьевна",
                              "Николаевна",
                              "Егоровна", "Васильевна", "Тимофеевна", "Федоровна", "Александровна", "Максимовна",
                              "Степановна"]  # список женских отчеств

    # Возвращает случайное мужское имя
    def getMaleName(self):
        return choice(self.names)

    # Возвращает случайную мужскую фамилию
    def getMaleFamily(self):
        return choice(self.families)

    # Возвращает случайное мужское отчество
    def getMalePatronimy(self):
        return choice(self.otches)

    # Возвращает случайное женское имя
    def getFemaleName(self):
        return choice(self.names_female)

    # Возвращает случайную женскую фамилию
    def getFemaleFamily(self):
        return choice(self.families_female)

    # Возвращает случайное женское отчество
    def getFemalePatronimy(self):
        return choice(self.otches_female)

    # Возвращает случайные пасспортные данные вида 0#########
    def getPassportData(self):
        return "0" + str(randint(1, 9)) + str(randint(10, 20)) + str(randint(100000, 999999))

    # Возвращает случайный номер телефона вида +7##########
    def getPhoneNumber(self):
        return "+7" + str(randint(100, 999)) + str(randint(1000000, 9999999))

    # Возвращает случайный адрес вида #Город#, #Улица#, #Номер дома#
    def getAddress(self):
        return f"{choice(self.cities)}, {choice(self.street)}, " \
               f"{randint(1, 800)}"

    # Возвращает случайную бувку русского алфавита
    def getRusLetter(self):
        return choice(self.rus_alphabet)

    # Возвращает случайную букву английского алфавита
    def getEngLetter(self):
        return choice(self.eng_alphabet)

    # Возвращает случайный гос номер автомобиля без региона
    def getCarNumber(self):
        return self.getRusLetter() + self.getRusLetter() + str(randint(100, 999)) + self.getRusLetter()


def main():
    f = Filler()
    print(f"{f.getMaleFamily()} {f.getMaleName()} {f.getMalePatronimy()}, {f.getAddress()}, {f.getPhoneNumber()}, "
          f"{f.getPassportData()}, {f.getCarNumber()}")


if __name__ == "__main__":
    main()
