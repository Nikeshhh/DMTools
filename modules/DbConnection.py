import pyodbc


class Connection:

    # Устанавливает соединение с базой данных Access
    def __init__(self, path, driver="Microsoft Access Driver (*.mdb, *.accdb)"):
        self.connection = pyodbc.connect("Driver={" + driver + "};DBQ=" + path + ";")
        self.cursor = self.connection.cursor()

    # Выполняет запрос типа INSERT
    def execInsertQuerry(self, querrystr):
        try:
            self.cursor.execute(querrystr)
            self.cursor.commit()
        except BaseException as e:
            print(e)

    # Выполняет запрос типа SELECT и возвращает список кортежей
    def execSelectQuerry(self, querrystr):
        try:
            self.cursor.execute(querrystr)
            return self.cursor.fetchall()
        except BaseException as e:
            print(e)


def main():
    c = Connection(r"C:\Users\Nikesh\Documents\langs.accdb")
    querry = "SELECT * FROM CLients"
    c.execSelectQuerry(querry)


if __name__ == "__main__":
    main()
