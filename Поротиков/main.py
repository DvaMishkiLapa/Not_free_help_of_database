import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import db

import ui
import edit_ship_loc

dbm = db.DBManager()

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ports_len = None
        self.ships_len = None
        self.free_ships_len = None
        self.data_len = None
        self.update_ports_table()

        self.selected_ship_in_seaport = []
        self.selected_port = []

        # buttons events
        self.tabWidget.currentChanged.connect(self.update_all_tables)
        
        self.ports_table.itemSelectionChanged.connect(self.ship_in_seaport_table_update)
        self.add_seaport.clicked.connect(self.add_seaport_click)
        self.del_seaport.clicked.connect(self.del_seaport_click)
        self.save_seaports.clicked.connect(self.save_seaports_click)

        self.ship_in_seaport_table.itemSelectionChanged.connect(self.save_selected_ship_in_seaport)
        self.change_seaport_for_ship.clicked.connect(self.change_seaport_for_ship_click)
        self.del_ship_in_seaport.clicked.connect(self.del_ship_in_seaport_click)

        self.save_ships.clicked.connect(self.save_ships_click)
        self.add_new_row_ship.clicked.connect(self.add_new_row_ship_click)
        self.del_ship.clicked.connect(self.del_ship_click)

        self.save_free_ships.clicked.connect(self.save_free_ships_click)
        self.del_free_ships.clicked.connect(self.del_free_ship_click)


    def update_all_tables(self):
        self.update_ships_table()
        self.update_ports_table()
        self.update_free_ships_table()


    def update_ports_table(self):
        self.ports_table.clearContents()  # Table cleaning
        self.ports_table.setRowCount(0)   #
        for port in dbm.get_all_ports():
            row_pos = self.ports_table.rowCount()
            self.ports_table.insertRow(row_pos)
            i = 0
            for x in port:
                self.ports_table.setItem(row_pos, i, QtWidgets.QTableWidgetItem(str(x)))
                i += 1
        self.ports_len = self.ports_table.rowCount()


    def update_ships_table(self):
        self.ships_table.clearContents()  # Table cleaning
        self.ships_table.setRowCount(0)   #
        data = {item[0]: item[1] for item in list(dbm.get_all_data())}
        self.data_len = len(data)
        for ship in dbm.get_all_ships():
            if data[ship[0]] != 0:
                row_pos = self.ships_table.rowCount()
                self.ships_table.insertRow(row_pos)
                self.ships_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(ship[0])))
                self.ships_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(data[ship[0]])))
                self.ships_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(ship[1]))
                self.ships_table.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(ship[2]))
        self.ships_len = self.ships_table.rowCount()


    def update_free_ships_table(self):
        self.free_ships_table.clearContents()  # Table cleaning
        self.free_ships_table.setRowCount(0)   #
        data = {item[0]: item[1] for item in list(dbm.get_all_data())}
        self.data_len = len(data)
        for ship in dbm.get_all_ships():
            if data[ship[0]] == 0:
                row_pos = self.free_ships_table.rowCount()
                self.free_ships_table.insertRow(row_pos)
                self.free_ships_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(ship[0])))
                self.free_ships_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(data[ship[0]])))
                self.free_ships_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(ship[1]))
                self.free_ships_table.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(ship[2]))
        self.free_ships_len = self.free_ships_table.rowCount()


    def ship_in_seaport_table_update(self):
        try:
            items = self.ports_table.selectedItems()
            if not items:
                return
            self.selected_port = [items[0].text(), items[1].text(), items[2].text(), items[3].text()]
        except IndexError:
            return
        self.ship_in_seaport_table.clearContents()  # Table cleaning
        self.ship_in_seaport_table.setRowCount(0)
        port_id = str(items[0].text())
        for ship in dbm.get_ships_in_port(port_id):
            row_pos = self.ship_in_seaport_table.rowCount()
            self.ship_in_seaport_table.insertRow(row_pos)
            i = 0
            for x in ship:
                self.ship_in_seaport_table.setItem(row_pos, i, QtWidgets.QTableWidgetItem(str(x)))
                i += 1

    # buttons near workers_table
    def add_seaport_click(self):
        self.ports_table.insertRow(self.ports_table.rowCount())


    def del_seaport_click(self):
        selected_rows = self.ports_table.selectionModel().selectedRows()
        list_index_rows = sorted([i.row() for i in selected_rows])
        for item in selected_rows:
            if item.sibling(item.row(), 0).data() != None:
                dbm.del_ports([int(item.sibling(item.row(), 0).data())])
                while len(list_index_rows): # Deleting rows from an employee's project table
                    self.ports_table.removeRow(list_index_rows[-1])
                    list_index_rows.pop()
            else:
                while len(list_index_rows): # Deleting rows from an employee's project table
                    self.ports_table.removeRow(list_index_rows[-1])
                    list_index_rows.pop()


    def save_seaports_click(self):
        row_pos = self.ports_table.rowCount()
        data = []
        for row in range(row_pos):
            data.append([])
            for col in range(4):
                try:
                    data[row].append(self.ports_table.item(row, col).text())
                except AttributeError:
                    pass
            if self.ports_len > row:
                dbm.update_ports(data[row])
            else:
                if dbm.insert_ports(data[row]):
                    self.ports_len = self.ports_table.rowCount()


    def save_selected_ship_in_seaport(self):
        items = self.ship_in_seaport_table.selectedItems()
        if items:
            self.selected_ship_in_seaport = [items[0].text(), items[1].text(), items[2].text()]


    def del_ship_in_seaport_click(self):
        if self.selected_port and self.selected_ship_in_seaport:
            dbm.update_data([self.selected_ship_in_seaport[0], 0])
            self.ship_in_seaport_table.removeRow(self.ship_in_seaport_table.selectionModel().selectedRows()[0].row())


    def change_seaport_for_ship_click(self):
        if self.selected_port and self.selected_ship_in_seaport:
            dialog = editShipLocDialog(self.selected_ship_in_seaport, self.selected_port)
            dialog.exec_()
            if dialog.answer:
                dbm.update_data([self.selected_ship_in_seaport[0], dialog.answer])
                self.ship_in_seaport_table_update()


    def save_ships_click(self):
        row_pos = self.ships_table.rowCount()
        data = []
        update_loc_list = []
        for row in range(row_pos):
            update_loc_list.append([])
            data.append([])
            update_loc_list[row].append(self.ships_table.item(row, 0).text())
            update_loc_list[row].append(self.ships_table.item(row, 1).text())
            for col in [0, 2, 3]:
                try:
                    data[row].append(self.ships_table.item(row, col).text())
                except AttributeError:
                    pass
            if self.ships_len > row:
                dbm.update_data(update_loc_list[row])
                dbm.update_ships(data[row])
            else:
                if dbm.insert_ships(data[row]):
                    self.ships_len = self.ships_table.rowCount()
                dbm.insert_data(update_loc_list[row])


    def del_ship_click(self):
        selected_rows = self.ships_table.selectionModel().selectedRows()
        list_index_rows = sorted([i.row() for i in selected_rows])
        for item in selected_rows:
            if item.sibling(item.row(), 0).data() != None:
                dbm.del_ships([int(item.sibling(item.row(), 0).data())])
                while len(list_index_rows): # Deleting rows from an employee's project table
                    self.ships_table.removeRow(list_index_rows[-1])
                    list_index_rows.pop()
            else:
                while len(list_index_rows): # Deleting rows from an employee's project table
                    self.ships_table.removeRow(list_index_rows[-1])
                    list_index_rows.pop()


    def add_new_row_ship_click(self):
        self.ships_table.insertRow(self.ships_table.rowCount())


    def save_free_ships_click(self):
        row_pos = self.free_ships_table.rowCount()
        data = []
        update_loc_list = []
        for row in range(row_pos):
            update_loc_list.append([])
            data.append([])
            update_loc_list[row].append(self.free_ships_table.item(row, 0).text())
            update_loc_list[row].append(self.free_ships_table.item(row, 1).text())
            for col in [0, 2, 3]:
                try:
                    data[row].append(self.free_ships_table.item(row, col).text())
                except AttributeError:
                    pass
            if self.free_ships_len > row:
                dbm.update_data(update_loc_list[row])
                dbm.update_ships(data[row])
            else:
                if dbm.insert_ships(data[row]):
                    self.free_ships_len = self.ships_table.rowCount()
                dbm.insert_data(update_loc_list[row])


    def del_free_ship_click(self):
        selected_rows = self.free_ships_table.selectionModel().selectedRows()
        list_index_rows = sorted([i.row() for i in selected_rows])
        for item in selected_rows:
            if item.sibling(item.row(), 0).data() != None:
                dbm.del_ships([int(item.sibling(item.row(), 0).data())])
                while len(list_index_rows): # Deleting rows from an employee's project table
                    self.free_ships_table.removeRow(list_index_rows[-1])
                    list_index_rows.pop()
            else:
                while len(list_index_rows): # Deleting rows from an employee's project table
                    self.free_ships_table.removeRow(list_index_rows[-1])
                    list_index_rows.pop()



class editShipLocDialog(QtWidgets.QDialog, edit_ship_loc.Ui_edit_ship_loc_dialog):
    def __init__(self, ship, port):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.answer = False
        self.ship_name = ship
        self.port_name = port
        self.current_ship.setText(self.ship_name[1] + ", " + self.ship_name[2])
        self.current_loc.setText(self.port_name[1] + ", " + self.port_name[2] + ", " + self.port_name[3])

        for port in dbm.get_all_ports():
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)
            i = 0
            for x in port:
                self.table.setItem(row_pos, i, QtWidgets.QTableWidgetItem(str(x)))
                i += 1

        self.add_button.clicked.connect(self.add_button_click)
        self.cancel_button.clicked.connect(self.cancel_button_click)

    def add_button_click(self):
        self.answer = self.table.selectedItems()[0].text()
        self.close()


    def cancel_button_click(self):
        self.close()


    def on_table_itemClicked(self, item):
        self.add_button.setEnabled(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()