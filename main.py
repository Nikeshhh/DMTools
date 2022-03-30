import modules.DbConnection as DBCon
import modules.FillingLib as FillLib


def main():
    con = DBCon.Connection(r"C:\Users\Nikesh\Documents\langs.accdb")
    filler = FillLib.Filler()
    print(filler.getCarNumber())
    print(con.execSelectQuerry('SELECT * FROM clients'))


if __name__ == '__main__':
    main()
