from random import *


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
        return self.names[randint(0, len(self.names) - 1)]

    # Возвращает случайную мужскую фамилию
    def getMaleFamily(self):
        return self.families[randint(0, len(self.families) - 1)]

    # Возвращает случайное мужское отчество
    def getMalePatronimy(self):
        return self.otches[randint(0, len(self.otches) - 1)]

    # Возвращает случайное женское имя
    def getFemaleName(self):
        return self.names_female[randint(0, len(self.names_female) - 1)]

    # Возвращает случайную женскую фамилию
    def getFemaleFamily(self):
        return self.families_female[randint(0, len(self.families_female) - 1)]

    # Возвращает случайное женское отчество
    def getFemalePatronimy(self):
        return self.otches_female[randint(0, len(self.otches_female) - 1)]

    # Возвращает случайные пасспортные данные вида 0#########
    def getPassportData(self):
        return "0" + str(randint(1, 9)) + str(randint(10, 20)) + str(randint(100000, 999999))

    # Возвращает случайный номер телефона вида +7##########
    def getPhoneNumber(self):
        return "+7" + str(randint(100, 999)) + str(randint(1000000, 9999999))

    # Возвращает случайный адрес вида #Город#, #Улица#, #Номер дома#
    def getAddress(self):
        return f"{self.cities[randint(0, len(self.cities) - 1)]}, {self.street[randint(0, len(self.street) - 1)]}, " \
               f"{randint(1, 800)}"

    # Возвращает случайную бувку русского алфавита
    def getRusLetter(self):
        return self.rus_alphabet[randint(0, len(self.rus_alphabet) - 1)]

    # Возвращает случайную букву английского алфавита
    def getEngLetter(self):
        return self.eng_alphabet[randint(0, len(self.eng_alphabet) - 1)]

    # Возвращает случайный гос номер автомобиля без региона
    def getCarNumber(self):
        return self.getRusLetter() + self.getRusLetter() + str(randint(100, 999)) + self.getRusLetter()


def main():
    f = Filler()
    print(f"{f.getMaleFamily()} {f.getMaleName()} {f.getMalePatronimy()}, {f.getAddress()}, {f.getPhoneNumber()}, "
          f"{f.getPassportData()}, {f.getCarNumber()}")


if __name__ == "__main__":
    main()
