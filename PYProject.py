# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PYProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from mplotwidget import MplotWidget
import pandas as pd
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)


# main window class
class Ui_MainWindow(object):

    # constructor that builds the gui
    def setupUi(self, MainWindow, file):


        self.df = pd.read_csv(file)

        # MainWindow.__init__(self)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")


        # settings for the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ------------------- Title ---------------------------------

        # settings for the tittle label
        self.Tittle = QtWidgets.QLabel(self.centralwidget)
        self.Tittle.setGeometry(QtCore.QRect(10, 0, 331, 41))
        font2 = QtGui.QFont()
        font2.setFamily("Times New Roman")
        font2.setPointSize(24)
        self.Tittle.setFont(font2)
        self.Tittle.setObjectName("Tittle")


        # ------------------- Grid Layout  ---------------------------------

        # grid for menu widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 270, 671))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # ------------------- Radio Buttons ---------------------------------

        # Radio BTN HORIZONATAL
        self.horizontal_radioBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.horizontal_radioBtn.setFont(font)
        self.horizontal_radioBtn.setObjectName("horizontal_radioBtn")
        self.gridLayout.addWidget(self.horizontal_radioBtn, 1, 0, 1, 1)
        self.horizontal_radioBtn.setChecked(True)

        # Radio BTN for VERTICAL view
        self.vertical_radioBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.vertical_radioBtn.setFont(font)
        self.vertical_radioBtn.setObjectName("vertical_radioBtn")
        self.gridLayout.addWidget(self.vertical_radioBtn, 2, 0, 1, 1)  # adding the btn to the grid layout


        # Change Lay out BTN

        self.change_layOut_BTN = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.change_layOut_BTN.setObjectName("change_layOut_btn")
        self.gridLayout.addWidget(self.change_layOut_BTN, 3, 1, 1, 1)

        # ------------------ X axis settings --------------------------------

        # x axis LABEL
        self.x_axis_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.x_axis_label.setFont(font)
        self.x_axis_label.setObjectName("x_axis_label")
        self.gridLayout.addWidget(self.x_axis_label, 3, 0, 1, 1)  # adding the label to the grid layout

        # X axis COMBO BOX
        self.x_axis_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.x_axis_comboBox.setFont(font)
        self.x_axis_comboBox.setObjectName("x_axis_comboBox")
        self.x_axis_comboBox.addItem("")
        self.x_axis_comboBox.addItem("")
        self.x_axis_comboBox.addItem("")
        self.gridLayout.addWidget(self.x_axis_comboBox, 4, 0, 1, 1)

        # ------------------ Y axis Settings --------------------------------

        # Y axis Label
        self.y_axis_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.y_axis_label.setFont(font)
        self.y_axis_label.setObjectName("y_axis_label")
        self.gridLayout.addWidget(self.y_axis_label, 5, 0, 1, 1)

        # Y axis COMOBO BOX
        self.y_axis_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.y_axis_comboBox.setFont(font)
        self.y_axis_comboBox.setObjectName("y_axis_comboBox")
        self.y_axis_comboBox.addItem("")
        self.y_axis_comboBox.addItem("")
        self.y_axis_comboBox.addItem("")
        self.gridLayout.addWidget(self.y_axis_comboBox, 6, 0, 1, 1)

        # ------------------ Sliders --------------------------------

        # Revenue LABEL
        self.revenu_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.revenu_Label.setFont(font)
        self.revenu_Label.setObjectName("revenu_Label")
        self.gridLayout.addWidget(self.revenu_Label, 8, 0, 1, 1)

        # Revenue SLIDER
        self.revenueSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.revenueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.revenueSlider.setObjectName("revenueSlider")
        self.gridLayout.addWidget(self.revenueSlider, 9, 0, 1, 1)

        # revenue BTN
        self.revenue_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.revenue_btn.setObjectName("revenue_btn")
        self.gridLayout.addWidget(self.revenue_btn,  9, 1, 1, 1)



        # Runtime LABEL
        self.runtime_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.runtime_label.setObjectName("runtime_label")
        self.gridLayout.addWidget(self.runtime_label, 10, 0, 1, 1)

        # Runtime SLIDER
        self.run_time_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.run_time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.run_time_slider.setObjectName("run_time_slider")
        self.gridLayout.addWidget(self.run_time_slider, 11, 0, 1, 1)

        # revenue BTN
        self.runtime_BTN = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.runtime_BTN.setObjectName("runtime_BTN")
        self.gridLayout.addWidget(self.runtime_BTN, 11, 1, 1, 1)


        # ------------------ genre Combo Box --------------------------------

        # Gnere LABEL
        self.genre_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.genre_label.setObjectName("genre_label")
        self.gridLayout.addWidget(self.genre_label, 12, 0, 1, 1)  # adding the label to the grid layout


        # Genre Combo box
        self.genre_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.genre_comboBox.setFont(font)
        self.genre_comboBox.setObjectName("genre_comboBox")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.gridLayout.addWidget(self.genre_comboBox, 13, 0, 1, 1)

        # revenue BTN
        self.genre_BTN = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.genre_BTN.setObjectName("runtime_BTN")
        self.gridLayout.addWidget(self.genre_BTN,  13, 1, 1, 1)



        # ------------------ Search Boxes --------------------------------


        # DIRECTOR LABEL
        self.srch_Director_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.srch_Director_label.setObjectName("srch_Director_label")
        self.gridLayout.addWidget(self.srch_Director_label, 15, 0, 1, 1)

        # DIRECTOR SEARCH BOX
        self.director_searchbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.director_searchbox.setObjectName("director_searchbox")
        self.gridLayout.addWidget(self.director_searchbox, 16, 0, 1, 1)

        # DIRECTOR BTN
        self.search_director_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search_director_btn.setObjectName("search_director_btn")
        self.gridLayout.addWidget(self.search_director_btn, 16, 1, 1, 1)



        # search by ACTOR LABEL
        self.srch_actor_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.srch_actor_label.setObjectName("srch_actor_label")
        self.gridLayout.addWidget(self.srch_actor_label, 17, 0, 1, 1)

        # ACTOR SEARCH BOX
        self.actor_searchbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.actor_searchbox.setObjectName("actor_searchbox")
        self.gridLayout.addWidget(self.actor_searchbox, 18, 0, 1, 1)

        # Search Actor BTN
        self.search_actor_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search_actor_btn.setObjectName("search_actor_btn")
        self.gridLayout.addWidget(self.search_actor_btn, 18, 1, 1, 1)



        # Rank Label
        self.srch_rank_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.srch_rank_label.setObjectName("srch_rank_label")
        self.gridLayout.addWidget(self.srch_rank_label, 19, 0, 1, 1)

        # RANK REACH BOX
        self.rank_searchbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.rank_searchbox.setObjectName("rank_searchbox")
        self.gridLayout.addWidget(self.rank_searchbox, 20, 0, 1, 1)

        # Search by RANK BTN
        self.srch_rank_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.srch_rank_btn.setObjectName("srch_rank_btn")
        self.gridLayout.addWidget(self.srch_rank_btn, 20, 1, 1, 1)


        # Search Movie

        self.srch_4movies_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.srch_4movies_label.setObjectName("srch_4movie_label")
        self.gridLayout.addWidget(self.srch_4movies_label, 21,0,1,1)

        self.srch_4movies_searchBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.srch_4movies_searchBox.setObjectName("srch_4movie_searchBox")
        self.gridLayout.addWidget(self.srch_4movies_searchBox, 22,0,1,1)

        self.srch_4movies_BTN = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.srch_4movies_BTN.setObjectName("srch_4movie_BTN")
        self.gridLayout.addWidget(self.srch_4movies_BTN, 22,1,1,1)

        # ------------------ Min and Max Combo Box --------------------------------

        # max and min LABEL
        self.ma_min_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ma_min_label.setObjectName("ma_min_label")
        self.gridLayout.addWidget(self.ma_min_label, 23, 0, 1, 1)  # adding the label to the grid layout

        # Min Max Combo Box
        self.max_min_combobox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.max_min_combobox.setObjectName("max_min_combobox")
        self.max_min_combobox.addItem("")
        self.max_min_combobox.addItem("")
        self.max_min_combobox.addItem("")
        self.gridLayout.addWidget(self.max_min_combobox, 24, 0, 1, 1)

        # Max min search BTN
        self.max_min_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.max_min_btn.setObjectName("max_min_btn")
        self.gridLayout.addWidget(self.max_min_btn, 24, 1, 1, 1)


        # ------------------ Spacers --------------------------------

        # spacer item
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)

        # spacer item
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 25, 0, 1, 1)

        # Spacer item
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)

        #Spacer Item
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 22, 0, 1, 1)

        # spacer Item
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 14, 0, 1, 1)

        # ---------------------------------------------------------------

        # Centering everything
        MainWindow.setCentralWidget(self.centralwidget)

        # Top menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # bottom status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ------------------- GRAPH Layout  ---------------------------------

        # graph widget
        self.MplotWidget = MplotWidget(self.centralwidget)

        # MainWindow.addToolBar(NavigationToolbar(self.MplotWidget.canvas, self))

        self.MplotWidget.setGeometry(QtCore.QRect(309, 49, 731, 651))
        self.MplotWidget.setObjectName("MplotWidget")

        # self.MplotWidget.canvas.axes.scatter(self.df['Rank'], self.df['Revenue (Millions)'])
        # self.MplotWidget.canvas.axes.set_xlabel('Rank')
        # self.MplotWidget.canvas.axes.set_ylabel('Rating')



        # ------------------ Info Label ----------------------------------

        self.movie_info_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.movie_info_scroll.setGeometry(QtCore.QRect(1070, 40, 350, 700))
        self.movie_info_scroll.setFont(font)
        self.movie_info_scroll.setObjectName("movie_info_scroll")
        self.movie_info_scroll.setWidgetResizable(True)

        self.movie_info_label = QtWidgets.QLabel()
        self.movie_info_label.setObjectName("movie_info_label")

        self.movie_info_scroll.setWidget(self.movie_info_label)




        # adding the main window to the UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # method to rename all the buttons and labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tittle.setText(_translate("MainWindow", "IMBD Data Base Interactive GUI"))
        self.ma_min_label.setText(_translate("MainWindow", "Max"))
        self.x_axis_label.setText(_translate("MainWindow", "X-Axis"))
        self.vertical_radioBtn.setText(_translate("MainWindow", "Vertical"))
        self.genre_label.setText(_translate("MainWindow", "Genre"))
        self.max_min_btn.setText(_translate("MainWindow", "Get Value"))
        self.runtime_label.setText(_translate("MainWindow", "Runtime: "))
        self.srch_rank_btn.setText(_translate("MainWindow", "Search Rank"))
        self.srch_actor_label.setText(_translate("MainWindow", "Search by Actors"))
        self.search_director_btn.setText(_translate("MainWindow", "Search Director"))
        self.srch_Director_label.setText(_translate("MainWindow", "Search by Director"))
        self.horizontal_radioBtn.setText(_translate("MainWindow", "Horizontal"))
        self.revenu_Label.setText(_translate("MainWindow", "Revenue: "))
        self.y_axis_comboBox.setItemText(0, _translate("MainWindow", "Rating"))
        self.y_axis_comboBox.setItemText(1, _translate("MainWindow", "Revenue (Millions)"))
        self.y_axis_comboBox.setItemText(2, _translate("MainWindow", "Votes"))
        self.x_axis_comboBox.setItemText(0, _translate("MainWindow", "Rank"))
        self.x_axis_comboBox.setItemText(1, _translate("MainWindow", "Year"))
        self.x_axis_comboBox.setItemText(2, _translate("MainWindow", "Metascore"))
        self.max_min_combobox.setItemText(0, _translate("MainWindow", "Max"))
        self.max_min_combobox.setItemText(1, _translate("MainWindow", "Min"))
        self.max_min_combobox.setItemText(2, _translate("MainWindow", "Mean"))
        self.y_axis_label.setText(_translate("MainWindow", "Y-Axis"))
        self.search_actor_btn.setText(_translate("MainWindow", "Search Actor"))
        self.srch_rank_label.setText(_translate("MainWindow", "Search by Top Rank"))
        self.change_layOut_BTN.setText(_translate("MainWindow", "Change Layout"))
        self.genre_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.genre_comboBox.setItemText(1, _translate("MainWindow", "Adventure"))
        self.genre_comboBox.setItemText(2, _translate("MainWindow", "Action"))
        self.genre_comboBox.setItemText(3, _translate("MainWindow", "Animation"))
        self.genre_comboBox.setItemText(4, _translate("MainWindow", "Biography"))
        self.genre_comboBox.setItemText(5, _translate("MainWindow", "Comedy"))
        self.genre_comboBox.setItemText(6, _translate("MainWindow", "Crime"))
        self.genre_comboBox.setItemText(7, _translate("MainWindow", "Drama"))
        self.genre_comboBox.setItemText(8, _translate("MainWindow", "Fantasy"))
        self.genre_comboBox.setItemText(9, _translate("MainWindow", "Horror"))
        self.genre_comboBox.setItemText(10, _translate("MainWindow", "Mystery"))
        self.genre_comboBox.setItemText(11, _translate("MainWindow", "Romance"))
        self.genre_comboBox.setItemText(12, _translate("MainWindow", "Sci-Fi"))
        self.genre_comboBox.setItemText(13, _translate("MainWindow", "Thriller"))
        self.revenue_btn.setText(_translate("MainWindow", "Search Revenue"))
        self.runtime_BTN.setText(_translate("MainWindow", "Search Runtime"))
        self.genre_BTN.setText(_translate("MainWindow", "Search Genre"))
        self.srch_4movies_label.setText(_translate("MainWindow", "Search Movie Name"))
        self.srch_4movies_BTN.setText(_translate("MainWindow", "Search Movie"))
        self.movie_info_label.setText(_translate("MainWindow","All Movies: \nRank               "
                                                              "                             Ttitle\n"+
                                                            self.df["Title"].to_string()))



if __name__ == "__main__":
    import sys

    file = "/Users/ervinlara/PycharmProjects/FinalProject/IMDB-Movie-Data.csv"

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,file)
    MainWindow.show()
    sys.exit(app.exec_())
