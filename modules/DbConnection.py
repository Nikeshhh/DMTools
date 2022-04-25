import pyodbc
import psycopg2
from modules.FillingLib import Filler


passw = '3228'


class AccessConnection:

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


class PostgreConnection:

    # Устанавливает соединение с PostgreSQL
    def __init__(self, dbname, password, dbuser='postgres', host='localhost'):
        self.connection = psycopg2.connect(dbname=dbname, user=dbuser, password=password, host=host)
        self.cursor = self.connection.cursor()

    def execInsertQuerry(self, querrystr):
        try:
            self.cursor.execute(querrystr)
            self.connection.commit()
        except BaseException as e:
            print(e)


def main():
    c = AccessConnection(r"C:\Users\Nikesh\Documents\langs.accdb")
    querry = "SELECT * FROM CLients"
    c.execSelectQuerry(querry)
    cp = PostgreConnection('Prak1', passw)


if __name__ == "__main__":
    main()
