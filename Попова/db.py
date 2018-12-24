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
        return self._query("SELECT * FROM students")

    def get_all_ports(self):
        return self._query("SELECT * FROM hostels")

    def get_ships_in_port(self, hostel_id):
        return self._query("SELECT * FROM students WHERE id IN (SELECT student_id FROM data WHERE data.hostel_id='{}')".format(hostel_id))

    def get_all_data(self):
        return self._query("SELECT * FROM data")

    def update_ports(self, hostels_data):
        return self._query("UPDATE hostels SET address='{1}', area='{2}' WHERE id='{0}'".format(*hostels_data))

    def insert_ports(self, hostels_data):
        try:
            return self._query("INSERT INTO hostels VALUES ('{}', '{}', '{}')".format(*hostels_data))
        except:
            return []

    def del_ports(self, hostels):
        for student in list(self._query("SELECT student_id FROM data WHERE hostel_id='{}'".format(*hostels))):
            self.update_data([student[0], 0])
        return self._query("DELETE FROM hostels WHERE id = '{}'".format(*hostels))

    def update_ships(self, students_data):
        return self._query("UPDATE students SET name='{1}', course='{2}', fac='{3}' WHERE id='{0}'".format(*students_data))

    def insert_ships(self, students_data):
        try:
            return self._query("INSERT INTO students VALUES ('{}', '{}', '{}', '{}')".format(*students_data))
        except:
            return []

    def del_ships(self, students):
        self.del_ship_in_port(students[0])
        return self._query("DELETE FROM students WHERE id = '{}'".format(*students))

    def insert_data(self, data):
        if not list(self._query("SELECT * FROM data WHERE hostel_id='{}' AND student_id='{}'".format(*data))):
            return self._query("INSERT INTO data VALUES ('{}', '{}')".format(*data))

    def update_data(self, data):
        return self._query("UPDATE data SET hostel_id='{1}' WHERE student_id='{0}'".format(*data))

    def del_ship_in_port(self, student_id):
        return self._query("DELETE FROM data WHERE student_id='{}'".format(student_id))

    def __del__(self):
        self.connect.close()
