import modules.DbConnection as DBCon
import modules.FillingLib as FillLib

passw = '3228'


def createQuerryProduct(p_name, p_cost, weight, date_produced, manufacturer):
    return f"INSERT INTO Product (p_name, p_cost, weight, date_produced, manufacturer)" \
           f"VALUES ('{p_name}', '{p_cost}', '{weight}', '{date_produced}', '{manufacturer}')"


def insertingProduct(db):
    p_name = input('p_name=')
    p_cost = input('p_cost=')
    weight = input('weight=')
    date_produced = input('date=')
    manufacturer = input('manufacturer=')
    querry = createQuerryProduct(p_name, p_cost, weight, date_produced, manufacturer)
    db.execInsertQuerry(querry)


def createQuerrySupply(address, s_date, amount, cost):
    return f"INSERT INTO Supply (address, s_date, amount, cost)" \
           f"VALUES ('{address}', '{s_date}', '{amount}', '{cost}')"


def insertingSupply(db):
    address = input('address=')
    s_date = input('s_date=')
    amount = input('amount=')
    cost = input('cost=')
    querry = createQuerrySupply(address, s_date, amount, cost)
    db.execInsertQuerry(querry)


def main():
    # con = DBCon.AccessConnection(r"C:\Users\Nikesh\Documents\langs.accdb")
    con = DBCon.PostgreConnection('Prak1', passw)
    while True:
        insertingProduct(con)
    # filler = FillLib.Filler()
    # print(filler.getCarNumber())
    # print(con.execSelectQuerry('SELECT * FROM clients'))


if __name__ == '__main__':
    main()
