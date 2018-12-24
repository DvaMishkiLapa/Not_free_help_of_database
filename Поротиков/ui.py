# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Windows/System32/@AppHelpToast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.change_seaport_for_ship = QtWidgets.QPushButton(self.tab)
        self.change_seaport_for_ship.setObjectName("change_seaport_for_ship")
        self.gridLayout_2.addWidget(self.change_seaport_for_ship, 5, 4, 1, 1)
        self.del_ship_in_seaport = QtWidgets.QPushButton(self.tab)
        self.del_ship_in_seaport.setObjectName("del_ship_in_seaport")
        self.gridLayout_2.addWidget(self.del_ship_in_seaport, 5, 3, 1, 1)
        self.del_seaport = QtWidgets.QPushButton(self.tab)
        self.del_seaport.setObjectName("del_seaport")
        self.gridLayout_2.addWidget(self.del_seaport, 3, 4, 1, 1)
        self.add_seaport = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_seaport.sizePolicy().hasHeightForWidth())
        self.add_seaport.setSizePolicy(sizePolicy)
        self.add_seaport.setObjectName("add_seaport")
        self.gridLayout_2.addWidget(self.add_seaport, 3, 3, 1, 1)
        self.save_seaports = QtWidgets.QPushButton(self.tab)
        self.save_seaports.setMinimumSize(QtCore.QSize(0, 0))
        self.save_seaports.setSizeIncrement(QtCore.QSize(0, 0))
        self.save_seaports.setBaseSize(QtCore.QSize(0, 0))
        self.save_seaports.setObjectName("save_seaports")
        self.gridLayout_2.addWidget(self.save_seaports, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ship_in_seaport_table = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ship_in_seaport_table.sizePolicy().hasHeightForWidth())
        self.ship_in_seaport_table.setSizePolicy(sizePolicy)
        self.ship_in_seaport_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ship_in_seaport_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ship_in_seaport_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ship_in_seaport_table.setGridStyle(QtCore.Qt.SolidLine)
        self.ship_in_seaport_table.setObjectName("ship_in_seaport_table")
        self.ship_in_seaport_table.setColumnCount(3)
        self.ship_in_seaport_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ship_in_seaport_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ship_in_seaport_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ship_in_seaport_table.setHorizontalHeaderItem(2, item)
        self.ship_in_seaport_table.horizontalHeader().setDefaultSectionSize(160)
        self.gridLayout_4.addWidget(self.ship_in_seaport_table, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 4, 0, 1, 5)
        self.ports_table = QtWidgets.QTableWidget(self.tab)
        self.ports_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ports_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ports_table.setGridStyle(QtCore.Qt.SolidLine)
        self.ports_table.setObjectName("ports_table")
        self.ports_table.setColumnCount(4)
        self.ports_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ports_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ports_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ports_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ports_table.setHorizontalHeaderItem(3, item)
        self.ports_table.horizontalHeader().setDefaultSectionSize(140)
        self.gridLayout_2.addWidget(self.ports_table, 0, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.add_new_row_ship = QtWidgets.QPushButton(self.tab_2)
        self.add_new_row_ship.setObjectName("add_new_row_ship")
        self.gridLayout_3.addWidget(self.add_new_row_ship, 2, 3, 1, 1)
        self.del_ship = QtWidgets.QPushButton(self.tab_2)
        self.del_ship.setObjectName("del_ship")
        self.gridLayout_3.addWidget(self.del_ship, 2, 4, 1, 1)
        self.save_ships = QtWidgets.QPushButton(self.tab_2)
        self.save_ships.setObjectName("save_ships")
        self.gridLayout_3.addWidget(self.save_ships, 2, 0, 1, 1)
        self.ships_table = QtWidgets.QTableWidget(self.tab_2)
        self.ships_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ships_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ships_table.setObjectName("ships_table")
        self.ships_table.setColumnCount(4)
        self.ships_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ships_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ships_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ships_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ships_table.setHorizontalHeaderItem(3, item)
        self.ships_table.horizontalHeader().setDefaultSectionSize(160)
        self.gridLayout_3.addWidget(self.ships_table, 0, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.free_ships_table = QtWidgets.QTableWidget(self.tab_3)
        self.free_ships_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.free_ships_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.free_ships_table.setObjectName("free_ships_table")
        self.free_ships_table.setColumnCount(4)
        self.free_ships_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.free_ships_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.free_ships_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.free_ships_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.free_ships_table.setHorizontalHeaderItem(3, item)
        self.free_ships_table.horizontalHeader().setDefaultSectionSize(160)
        self.gridLayout_5.addWidget(self.free_ships_table, 0, 0, 1, 3)
        self.save_free_ships = QtWidgets.QPushButton(self.tab_3)
        self.save_free_ships.setObjectName("save_free_ships")
        self.gridLayout_5.addWidget(self.save_free_ships, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(563, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 1, 1, 1)
        self.del_free_ships = QtWidgets.QPushButton(self.tab_3)
        self.del_free_ships.setObjectName("del_free_ships")
        self.gridLayout_5.addWidget(self.del_free_ships, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Управление дислокацией кораблей"))
        self.change_seaport_for_ship.setText(_translate("MainWindow", "Изменить порт"))
        self.del_ship_in_seaport.setText(_translate("MainWindow", "Отвязать"))
        self.del_seaport.setText(_translate("MainWindow", "Удалить"))
        self.add_seaport.setText(_translate("MainWindow", "Добавить"))
        self.save_seaports.setText(_translate("MainWindow", "Сохранить изменения"))
        self.groupBox.setTitle(_translate("MainWindow", "Корабли, находящиеся в порту"))
        item = self.ship_in_seaport_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.ship_in_seaport_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.ship_in_seaport_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Класс корабля"))
        item = self.ports_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.ports_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.ports_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Город"))
        item = self.ports_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Страна"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Порты"))
        self.add_new_row_ship.setText(_translate("MainWindow", "Добавить"))
        self.del_ship.setText(_translate("MainWindow", "Удалить"))
        self.save_ships.setText(_translate("MainWindow", "Сохранить изменения"))
        item = self.ships_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.ships_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID порта дислокации"))
        item = self.ships_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.ships_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Класс корабля"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Корабли"))
        item = self.free_ships_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.free_ships_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID порта дислокации"))
        item = self.free_ships_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.free_ships_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Класс корабля"))
        self.save_free_ships.setText(_translate("MainWindow", "Сохранить изменения"))
        self.del_free_ships.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Корабли без назначенного порта"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

