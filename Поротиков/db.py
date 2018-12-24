import sqlite3

class DBManager():
    def __init__(self):
        try:
            self.connect = sqlite3.connect('db.sqlite')
        except sqlite3.Error as e:
            print(e)
        self.cursor = self.connect.cursor()

    def _query(self, arg):
        self.cursor.execute(arg)
        self.connect.commit()
        return self.cursor

    def get_all_ships(self):
        return self._query("SELECT * FROM ships")

    def get_all_ports(self):
        return self._query("SELECT * FROM ports")

    def get_ships_in_port(self, port_id):
        return self._query("SELECT * FROM ships WHERE id IN (SELECT ship_id FROM data WHERE data.port_id='{}')".format(port_id))

    def get_all_data(self):
        return self._query("SELECT * FROM data")

    def update_ports(self, ports_data):
        return self._query("UPDATE ports SET name='{1}', city='{2}', country='{3}' WHERE id='{0}'".format(*ports_data))

    def insert_ports(self, ports_data):
        try:
            return self._query("INSERT INTO ports VALUES ('{}', '{}', '{}', '{}')".format(*ports_data))
        except:
            return []

    def del_ports(self, ports):
        for ship in list(self._query("SELECT ship_id FROM data WHERE port_id='{}'".format(*ports))):
            print(ship[0])
            self.update_data([ship[0], 0])
        return self._query("DELETE FROM ports WHERE id = '{}'".format(*ports))

    def update_ships(self, ships_data):
        return self._query("UPDATE ships SET name='{1}', index_name='{2}' WHERE id='{0}'".format(*ships_data))

    def insert_ships(self, ships_data):
        try:
            return self._query("INSERT INTO ships VALUES ('{}', '{}', '{}')".format(*ships_data))
        except:
            return []

    def del_ships(self, ships):
        self.del_ship_in_port(ships[0])
        return self._query("DELETE FROM ships WHERE id = '{}'".format(*ships))

    def insert_data(self, data):
        if not list(self._query("SELECT * FROM data WHERE port_id='{}' AND ship_id='{}'".format(*data))):
            return self._query("INSERT INTO data VALUES ('{}', '{}')".format(*data))

    def update_data(self, data):
        return self._query("UPDATE data SET port_id='{1}' WHERE ship_id='{0}'".format(*data))

    def del_ship_in_port(self, ship_id):
        return self._query("DELETE FROM data WHERE ship_id='{}'".format(ship_id))

    def __del__(self):
        self.connect.close()
