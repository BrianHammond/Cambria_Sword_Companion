# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 738)
        icon = QIcon()
        icon.addFile(u":/images/cs_ac.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_dark_mode = QAction(MainWindow)
        self.action_dark_mode.setObjectName(u"action_dark_mode")
        self.action_dark_mode.setCheckable(True)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.group_wonderful = QGroupBox(self.centralwidget)
        self.group_wonderful.setObjectName(u"group_wonderful")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_wonderful.sizePolicy().hasHeightForWidth())
        self.group_wonderful.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.group_wonderful)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(self.group_wonderful)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_0 = QWidget()
        self.tab_0.setObjectName(u"tab_0")
        self.verticalLayout_2 = QVBoxLayout(self.tab_0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_0 = QGridLayout()
        self.gridLayout_0.setObjectName(u"gridLayout_0")
        self.gridLayout_0.setHorizontalSpacing(10)
        self.gridLayout_0.setVerticalSpacing(20)
        self.gridLayout_0.setContentsMargins(10, 10, 10, 10)
        self.label_sp_weapon_0 = QLabel(self.tab_0)
        self.label_sp_weapon_0.setObjectName(u"label_sp_weapon_0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_sp_weapon_0.sizePolicy().hasHeightForWidth())
        self.label_sp_weapon_0.setSizePolicy(sizePolicy1)
        self.label_sp_weapon_0.setMinimumSize(QSize(100, 0))

        self.gridLayout_0.addWidget(self.label_sp_weapon_0, 1, 0, 1, 1)

        self.label_eyes_0 = QLabel(self.tab_0)
        self.label_eyes_0.setObjectName(u"label_eyes_0")
        sizePolicy1.setHeightForWidth(self.label_eyes_0.sizePolicy().hasHeightForWidth())
        self.label_eyes_0.setSizePolicy(sizePolicy1)

        self.gridLayout_0.addWidget(self.label_eyes_0, 0, 0, 1, 1)

        self.box_eyes_0 = QComboBox(self.tab_0)
        self.box_eyes_0.addItem("")
        self.box_eyes_0.addItem("")
        self.box_eyes_0.addItem("")
        self.box_eyes_0.addItem("")
        self.box_eyes_0.addItem("")
        self.box_eyes_0.addItem("")
        self.box_eyes_0.setObjectName(u"box_eyes_0")

        self.gridLayout_0.addWidget(self.box_eyes_0, 0, 1, 1, 1)

        self.box_sp_weapon_0 = QComboBox(self.tab_0)
        self.box_sp_weapon_0.addItem("")
        self.box_sp_weapon_0.addItem("")
        self.box_sp_weapon_0.addItem("")
        self.box_sp_weapon_0.addItem("")
        self.box_sp_weapon_0.addItem("")
        self.box_sp_weapon_0.addItem("")
        self.box_sp_weapon_0.setObjectName(u"box_sp_weapon_0")

        self.gridLayout_0.addWidget(self.box_sp_weapon_0, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_0)

        self.tabWidget.addTab(self.tab_0, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_4 = QVBoxLayout(self.tab_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.gridLayout_1.setHorizontalSpacing(10)
        self.gridLayout_1.setVerticalSpacing(20)
        self.gridLayout_1.setContentsMargins(10, 10, 10, 10)
        self.label_sp_weapon_1 = QLabel(self.tab_1)
        self.label_sp_weapon_1.setObjectName(u"label_sp_weapon_1")
        sizePolicy1.setHeightForWidth(self.label_sp_weapon_1.sizePolicy().hasHeightForWidth())
        self.label_sp_weapon_1.setSizePolicy(sizePolicy1)
        self.label_sp_weapon_1.setMinimumSize(QSize(100, 0))

        self.gridLayout_1.addWidget(self.label_sp_weapon_1, 1, 0, 1, 1)

        self.label_eyes_1 = QLabel(self.tab_1)
        self.label_eyes_1.setObjectName(u"label_eyes_1")
        sizePolicy1.setHeightForWidth(self.label_eyes_1.sizePolicy().hasHeightForWidth())
        self.label_eyes_1.setSizePolicy(sizePolicy1)

        self.gridLayout_1.addWidget(self.label_eyes_1, 0, 0, 1, 1)

        self.box_eyes_1 = QComboBox(self.tab_1)
        self.box_eyes_1.addItem("")
        self.box_eyes_1.addItem("")
        self.box_eyes_1.addItem("")
        self.box_eyes_1.addItem("")
        self.box_eyes_1.addItem("")
        self.box_eyes_1.addItem("")
        self.box_eyes_1.setObjectName(u"box_eyes_1")

        self.gridLayout_1.addWidget(self.box_eyes_1, 0, 1, 1, 1)

        self.box_sp_weapon_1 = QComboBox(self.tab_1)
        self.box_sp_weapon_1.addItem("")
        self.box_sp_weapon_1.addItem("")
        self.box_sp_weapon_1.addItem("")
        self.box_sp_weapon_1.addItem("")
        self.box_sp_weapon_1.addItem("")
        self.box_sp_weapon_1.addItem("")
        self.box_sp_weapon_1.setObjectName(u"box_sp_weapon_1")

        self.gridLayout_1.addWidget(self.box_sp_weapon_1, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_sp_weapon_2 = QLabel(self.tab_2)
        self.label_sp_weapon_2.setObjectName(u"label_sp_weapon_2")
        sizePolicy1.setHeightForWidth(self.label_sp_weapon_2.sizePolicy().hasHeightForWidth())
        self.label_sp_weapon_2.setSizePolicy(sizePolicy1)
        self.label_sp_weapon_2.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.label_sp_weapon_2, 1, 0, 1, 1)

        self.label_eyes_2 = QLabel(self.tab_2)
        self.label_eyes_2.setObjectName(u"label_eyes_2")
        sizePolicy1.setHeightForWidth(self.label_eyes_2.sizePolicy().hasHeightForWidth())
        self.label_eyes_2.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_eyes_2, 0, 0, 1, 1)

        self.box_eyes_2 = QComboBox(self.tab_2)
        self.box_eyes_2.addItem("")
        self.box_eyes_2.addItem("")
        self.box_eyes_2.addItem("")
        self.box_eyes_2.addItem("")
        self.box_eyes_2.addItem("")
        self.box_eyes_2.addItem("")
        self.box_eyes_2.setObjectName(u"box_eyes_2")

        self.gridLayout_2.addWidget(self.box_eyes_2, 0, 1, 1, 1)

        self.box_sp_weapon_2 = QComboBox(self.tab_2)
        self.box_sp_weapon_2.addItem("")
        self.box_sp_weapon_2.addItem("")
        self.box_sp_weapon_2.addItem("")
        self.box_sp_weapon_2.addItem("")
        self.box_sp_weapon_2.addItem("")
        self.box_sp_weapon_2.addItem("")
        self.box_sp_weapon_2.setObjectName(u"box_sp_weapon_2")

        self.gridLayout_2.addWidget(self.box_sp_weapon_2, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_sp_weapon_3 = QLabel(self.tab_3)
        self.label_sp_weapon_3.setObjectName(u"label_sp_weapon_3")
        sizePolicy1.setHeightForWidth(self.label_sp_weapon_3.sizePolicy().hasHeightForWidth())
        self.label_sp_weapon_3.setSizePolicy(sizePolicy1)
        self.label_sp_weapon_3.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.label_sp_weapon_3, 1, 0, 1, 1)

        self.label_eyes_3 = QLabel(self.tab_3)
        self.label_eyes_3.setObjectName(u"label_eyes_3")
        sizePolicy1.setHeightForWidth(self.label_eyes_3.sizePolicy().hasHeightForWidth())
        self.label_eyes_3.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.label_eyes_3, 0, 0, 1, 1)

        self.box_eyes_3 = QComboBox(self.tab_3)
        self.box_eyes_3.addItem("")
        self.box_eyes_3.addItem("")
        self.box_eyes_3.addItem("")
        self.box_eyes_3.addItem("")
        self.box_eyes_3.addItem("")
        self.box_eyes_3.addItem("")
        self.box_eyes_3.setObjectName(u"box_eyes_3")

        self.gridLayout_3.addWidget(self.box_eyes_3, 0, 1, 1, 1)

        self.box_sp_weapon_3 = QComboBox(self.tab_3)
        self.box_sp_weapon_3.addItem("")
        self.box_sp_weapon_3.addItem("")
        self.box_sp_weapon_3.addItem("")
        self.box_sp_weapon_3.addItem("")
        self.box_sp_weapon_3.addItem("")
        self.box_sp_weapon_3.addItem("")
        self.box_sp_weapon_3.setObjectName(u"box_sp_weapon_3")

        self.gridLayout_3.addWidget(self.box_sp_weapon_3, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_7 = QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_sp_weapon_4 = QLabel(self.tab_4)
        self.label_sp_weapon_4.setObjectName(u"label_sp_weapon_4")
        sizePolicy1.setHeightForWidth(self.label_sp_weapon_4.sizePolicy().hasHeightForWidth())
        self.label_sp_weapon_4.setSizePolicy(sizePolicy1)
        self.label_sp_weapon_4.setMinimumSize(QSize(100, 0))

        self.gridLayout_4.addWidget(self.label_sp_weapon_4, 1, 0, 1, 1)

        self.label_eyes_4 = QLabel(self.tab_4)
        self.label_eyes_4.setObjectName(u"label_eyes_4")
        sizePolicy1.setHeightForWidth(self.label_eyes_4.sizePolicy().hasHeightForWidth())
        self.label_eyes_4.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.label_eyes_4, 0, 0, 1, 1)

        self.box_eyes_4 = QComboBox(self.tab_4)
        self.box_eyes_4.addItem("")
        self.box_eyes_4.addItem("")
        self.box_eyes_4.addItem("")
        self.box_eyes_4.addItem("")
        self.box_eyes_4.addItem("")
        self.box_eyes_4.addItem("")
        self.box_eyes_4.setObjectName(u"box_eyes_4")

        self.gridLayout_4.addWidget(self.box_eyes_4, 0, 1, 1, 1)

        self.box_sp_weapon_4 = QComboBox(self.tab_4)
        self.box_sp_weapon_4.addItem("")
        self.box_sp_weapon_4.addItem("")
        self.box_sp_weapon_4.addItem("")
        self.box_sp_weapon_4.addItem("")
        self.box_sp_weapon_4.addItem("")
        self.box_sp_weapon_4.addItem("")
        self.box_sp_weapon_4.setObjectName(u"box_sp_weapon_4")

        self.gridLayout_4.addWidget(self.box_sp_weapon_4, 1, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_4)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_8 = QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_sp_weapon_5 = QLabel(self.tab_5)
        self.label_sp_weapon_5.setObjectName(u"label_sp_weapon_5")
        sizePolicy1.setHeightForWidth(self.label_sp_weapon_5.sizePolicy().hasHeightForWidth())
        self.label_sp_weapon_5.setSizePolicy(sizePolicy1)
        self.label_sp_weapon_5.setMinimumSize(QSize(100, 0))

        self.gridLayout_5.addWidget(self.label_sp_weapon_5, 1, 0, 1, 1)

        self.label_eyes_5 = QLabel(self.tab_5)
        self.label_eyes_5.setObjectName(u"label_eyes_5")
        sizePolicy1.setHeightForWidth(self.label_eyes_5.sizePolicy().hasHeightForWidth())
        self.label_eyes_5.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_eyes_5, 0, 0, 1, 1)

        self.box_eyes_5 = QComboBox(self.tab_5)
        self.box_eyes_5.addItem("")
        self.box_eyes_5.addItem("")
        self.box_eyes_5.addItem("")
        self.box_eyes_5.addItem("")
        self.box_eyes_5.addItem("")
        self.box_eyes_5.addItem("")
        self.box_eyes_5.setObjectName(u"box_eyes_5")

        self.gridLayout_5.addWidget(self.box_eyes_5, 0, 1, 1, 1)

        self.box_sp_weapon_5 = QComboBox(self.tab_5)
        self.box_sp_weapon_5.addItem("")
        self.box_sp_weapon_5.addItem("")
        self.box_sp_weapon_5.addItem("")
        self.box_sp_weapon_5.addItem("")
        self.box_sp_weapon_5.addItem("")
        self.box_sp_weapon_5.addItem("")
        self.box_sp_weapon_5.setObjectName(u"box_sp_weapon_5")

        self.gridLayout_5.addWidget(self.box_sp_weapon_5, 1, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_5)

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.grid_main = QGridLayout()
        self.grid_main.setObjectName(u"grid_main")
        self.grid_main.setHorizontalSpacing(10)
        self.grid_main.setVerticalSpacing(20)
        self.grid_main.setContentsMargins(10, 10, 10, 10)
        self.box_option_shot = QComboBox(self.group_wonderful)
        self.box_option_shot.addItem("")
        self.box_option_shot.addItem("")
        self.box_option_shot.addItem("")
        self.box_option_shot.addItem("")
        self.box_option_shot.setObjectName(u"box_option_shot")

        self.grid_main.addWidget(self.box_option_shot, 1, 1, 1, 1)

        self.label_main_shot = QLabel(self.group_wonderful)
        self.label_main_shot.setObjectName(u"label_main_shot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_main_shot.sizePolicy().hasHeightForWidth())
        self.label_main_shot.setSizePolicy(sizePolicy2)

        self.grid_main.addWidget(self.label_main_shot, 0, 0, 1, 1)

        self.box_rating = QComboBox(self.group_wonderful)
        self.box_rating.addItem("")
        self.box_rating.addItem("")
        self.box_rating.addItem("")
        self.box_rating.setObjectName(u"box_rating")

        self.grid_main.addWidget(self.box_rating, 2, 1, 1, 1)

        self.label_option_shot = QLabel(self.group_wonderful)
        self.label_option_shot.setObjectName(u"label_option_shot")
        sizePolicy2.setHeightForWidth(self.label_option_shot.sizePolicy().hasHeightForWidth())
        self.label_option_shot.setSizePolicy(sizePolicy2)
        self.label_option_shot.setMinimumSize(QSize(0, 0))

        self.grid_main.addWidget(self.label_option_shot, 1, 0, 1, 1)

        self.label_rating = QLabel(self.group_wonderful)
        self.label_rating.setObjectName(u"label_rating")
        sizePolicy2.setHeightForWidth(self.label_rating.sizePolicy().hasHeightForWidth())
        self.label_rating.setSizePolicy(sizePolicy2)
        self.label_rating.setMinimumSize(QSize(110, 0))

        self.grid_main.addWidget(self.label_rating, 2, 0, 1, 1)

        self.box_main_shot = QComboBox(self.group_wonderful)
        self.box_main_shot.addItem("")
        self.box_main_shot.addItem("")
        self.box_main_shot.addItem("")
        self.box_main_shot.addItem("")
        self.box_main_shot.setObjectName(u"box_main_shot")

        self.grid_main.addWidget(self.box_main_shot, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_main)

        self.line_notes = QLineEdit(self.group_wonderful)
        self.line_notes.setObjectName(u"line_notes")

        self.verticalLayout.addWidget(self.line_notes)

        self.hb_buttons = QHBoxLayout()
        self.hb_buttons.setObjectName(u"hb_buttons")
        self.hb_buttons.setContentsMargins(10, 10, 10, 10)
        self.button_add = QPushButton(self.group_wonderful)
        self.button_add.setObjectName(u"button_add")
        font = QFont()
        font.setPointSize(8)
        self.button_add.setFont(font)

        self.hb_buttons.addWidget(self.button_add)

        self.button_update = QPushButton(self.group_wonderful)
        self.button_update.setObjectName(u"button_update")
        font1 = QFont()
        font1.setPointSize(9)
        self.button_update.setFont(font1)

        self.hb_buttons.addWidget(self.button_update)

        self.button_remove = QPushButton(self.group_wonderful)
        self.button_remove.setObjectName(u"button_remove")
        self.button_remove.setFont(font1)

        self.hb_buttons.addWidget(self.button_remove)

        self.button_remove_all = QPushButton(self.group_wonderful)
        self.button_remove_all.setObjectName(u"button_remove_all")
        self.button_remove_all.setFont(font1)

        self.hb_buttons.addWidget(self.button_remove_all)


        self.verticalLayout.addLayout(self.hb_buttons)


        self.verticalLayout_9.addWidget(self.group_wonderful)

        self.group_search = QGroupBox(self.centralwidget)
        self.group_search.setObjectName(u"group_search")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.group_search.sizePolicy().hasHeightForWidth())
        self.group_search.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.group_search)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.grid_database = QGridLayout()
        self.grid_database.setObjectName(u"grid_database")
        self.grid_database.setHorizontalSpacing(10)
        self.grid_database.setVerticalSpacing(5)
        self.grid_database.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.group_search)
        self.label_4.setObjectName(u"label_4")

        self.grid_database.addWidget(self.label_4, 0, 1, 1, 1)

        self.button_search = QPushButton(self.group_search)
        self.button_search.setObjectName(u"button_search")
        sizePolicy1.setHeightForWidth(self.button_search.sizePolicy().hasHeightForWidth())
        self.button_search.setSizePolicy(sizePolicy1)
        self.button_search.setMinimumSize(QSize(100, 0))

        self.grid_database.addWidget(self.button_search, 3, 0, 1, 1)

        self.label = QLabel(self.group_search)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(113, 0))

        self.grid_database.addWidget(self.label, 0, 0, 1, 1)

        self.box_search_life_forms = QComboBox(self.group_search)
        self.box_search_life_forms.addItem("")
        self.box_search_life_forms.addItem("")
        self.box_search_life_forms.addItem("")
        self.box_search_life_forms.addItem("")
        self.box_search_life_forms.addItem("")
        self.box_search_life_forms.addItem("")
        self.box_search_life_forms.addItem("")
        self.box_search_life_forms.setObjectName(u"box_search_life_forms")

        self.grid_database.addWidget(self.box_search_life_forms, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.grid_database.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.grid_database.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.box_search_rating = QComboBox(self.group_search)
        self.box_search_rating.addItem("")
        self.box_search_rating.addItem("")
        self.box_search_rating.addItem("")
        self.box_search_rating.addItem("")
        self.box_search_rating.setObjectName(u"box_search_rating")
        sizePolicy1.setHeightForWidth(self.box_search_rating.sizePolicy().hasHeightForWidth())
        self.box_search_rating.setSizePolicy(sizePolicy1)
        self.box_search_rating.setMinimumSize(QSize(115, 0))

        self.grid_database.addWidget(self.box_search_rating, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.grid_database)

        self.table = QTableWidget(self.group_search)
        if (self.table.columnCount() < 8):
            self.table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table.setObjectName(u"table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy4)
        self.table.setMinimumSize(QSize(867, 50))
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setMinimumSectionSize(20)
        self.table.horizontalHeader().setDefaultSectionSize(130)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_3.addWidget(self.table)


        self.verticalLayout_9.addWidget(self.group_search)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 958, 22))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_sp_weapon_0.setBuddy(self.box_sp_weapon_0)
        self.label_eyes_0.setBuddy(self.box_eyes_0)
        self.label_sp_weapon_1.setBuddy(self.box_sp_weapon_0)
        self.label_eyes_1.setBuddy(self.box_eyes_0)
        self.label_sp_weapon_2.setBuddy(self.box_sp_weapon_0)
        self.label_eyes_2.setBuddy(self.box_eyes_0)
        self.label_sp_weapon_3.setBuddy(self.box_sp_weapon_0)
        self.label_eyes_3.setBuddy(self.box_eyes_0)
        self.label_sp_weapon_4.setBuddy(self.box_sp_weapon_0)
        self.label_eyes_4.setBuddy(self.box_eyes_0)
        self.label_sp_weapon_5.setBuddy(self.box_sp_weapon_0)
        self.label_eyes_5.setBuddy(self.box_eyes_0)
        self.label_main_shot.setBuddy(self.box_main_shot)
        self.label_option_shot.setBuddy(self.box_option_shot)
        self.label_rating.setBuddy(self.box_rating)
        self.label_4.setBuddy(self.box_search_rating)
        self.label.setBuddy(self.box_search_life_forms)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabWidget, self.box_main_shot)
        QWidget.setTabOrder(self.box_main_shot, self.box_option_shot)
        QWidget.setTabOrder(self.box_option_shot, self.box_rating)
        QWidget.setTabOrder(self.box_rating, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_update)
        QWidget.setTabOrder(self.button_update, self.button_remove)
        QWidget.setTabOrder(self.button_remove, self.button_remove_all)
        QWidget.setTabOrder(self.button_remove_all, self.table)
        QWidget.setTabOrder(self.table, self.box_sp_weapon_0)
        QWidget.setTabOrder(self.box_sp_weapon_0, self.box_eyes_0)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings.addAction(self.action_dark_mode)
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_about_qt)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cambria Sword Companion", None))
        self.action_dark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.group_wonderful.setTitle(QCoreApplication.translate("MainWindow", u"Wonderful Life Forms", None))
        self.label_sp_weapon_0.setText(QCoreApplication.translate("MainWindow", u"Special Weapon", None))
        self.label_eyes_0.setText(QCoreApplication.translate("MainWindow", u"Clone Eyes", None))
        self.box_eyes_0.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Normal", None))
        self.box_eyes_0.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Energy", None))
        self.box_eyes_0.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Blade", None))
        self.box_eyes_0.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Missile", None))
        self.box_eyes_0.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Power", None))
        self.box_eyes_0.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Force", None))

        self.box_sp_weapon_0.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Clustar", None))
        self.box_sp_weapon_0.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Hyper-Ray", None))
        self.box_sp_weapon_0.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Search", None))
        self.box_sp_weapon_0.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Burst", None))
        self.box_sp_weapon_0.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Verteblade", None))
        self.box_sp_weapon_0.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Thunder", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), QCoreApplication.translate("MainWindow", u"Cyclopyge Unbonata", None))
        self.label_sp_weapon_1.setText(QCoreApplication.translate("MainWindow", u"Special Weapon", None))
        self.label_eyes_1.setText(QCoreApplication.translate("MainWindow", u"Clone Eyes", None))
        self.box_eyes_1.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Normal", None))
        self.box_eyes_1.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Energy", None))
        self.box_eyes_1.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Blade", None))
        self.box_eyes_1.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Missile", None))
        self.box_eyes_1.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Power", None))
        self.box_eyes_1.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Force", None))

        self.box_sp_weapon_1.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Clustar", None))
        self.box_sp_weapon_1.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Hyper-Ray", None))
        self.box_sp_weapon_1.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Search", None))
        self.box_sp_weapon_1.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Burst", None))
        self.box_sp_weapon_1.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Verteblade", None))
        self.box_sp_weapon_1.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Thunder", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Marrella Splendens", None))
        self.label_sp_weapon_2.setText(QCoreApplication.translate("MainWindow", u"Special Weapon", None))
        self.label_eyes_2.setText(QCoreApplication.translate("MainWindow", u"Clone Eyes", None))
        self.box_eyes_2.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Normal", None))
        self.box_eyes_2.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Energy", None))
        self.box_eyes_2.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Blade", None))
        self.box_eyes_2.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Missile", None))
        self.box_eyes_2.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Power", None))
        self.box_eyes_2.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Force", None))

        self.box_sp_weapon_2.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Clustar", None))
        self.box_sp_weapon_2.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Hyper-Ray", None))
        self.box_sp_weapon_2.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Search", None))
        self.box_sp_weapon_2.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Burst", None))
        self.box_sp_weapon_2.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Verteblade", None))
        self.box_sp_weapon_2.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Thunder", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hallucigenia Sparsa", None))
        self.label_sp_weapon_3.setText(QCoreApplication.translate("MainWindow", u"Special Weapon", None))
        self.label_eyes_3.setText(QCoreApplication.translate("MainWindow", u"Clone Eyes", None))
        self.box_eyes_3.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Normal", None))
        self.box_eyes_3.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Energy", None))
        self.box_eyes_3.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Blade", None))
        self.box_eyes_3.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Missile", None))
        self.box_eyes_3.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Power", None))
        self.box_eyes_3.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Force", None))

        self.box_sp_weapon_3.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Clustar", None))
        self.box_sp_weapon_3.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Hyper-Ray", None))
        self.box_sp_weapon_3.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Search", None))
        self.box_sp_weapon_3.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Burst", None))
        self.box_sp_weapon_3.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Verteblade", None))
        self.box_sp_weapon_3.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Thunder", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Sarotrocercus Oblita", None))
        self.label_sp_weapon_4.setText(QCoreApplication.translate("MainWindow", u"Special Weapon", None))
        self.label_eyes_4.setText(QCoreApplication.translate("MainWindow", u"Clone Eyes", None))
        self.box_eyes_4.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Normal", None))
        self.box_eyes_4.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Energy", None))
        self.box_eyes_4.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Blade", None))
        self.box_eyes_4.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Missile", None))
        self.box_eyes_4.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Power", None))
        self.box_eyes_4.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Force", None))

        self.box_sp_weapon_4.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Clustar", None))
        self.box_sp_weapon_4.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Hyper-Ray", None))
        self.box_sp_weapon_4.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Search", None))
        self.box_sp_weapon_4.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Burst", None))
        self.box_sp_weapon_4.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Verteblade", None))
        self.box_sp_weapon_4.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Thunder", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Burgessia Bella", None))
        self.label_sp_weapon_5.setText(QCoreApplication.translate("MainWindow", u"Special Weapon", None))
        self.label_eyes_5.setText(QCoreApplication.translate("MainWindow", u"Clone Eyes", None))
        self.box_eyes_5.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Normal", None))
        self.box_eyes_5.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Energy", None))
        self.box_eyes_5.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Blade", None))
        self.box_eyes_5.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Missile", None))
        self.box_eyes_5.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Power", None))
        self.box_eyes_5.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Force", None))

        self.box_sp_weapon_5.setItemText(0, QCoreApplication.translate("MainWindow", u"A: Clustar", None))
        self.box_sp_weapon_5.setItemText(1, QCoreApplication.translate("MainWindow", u"B: Hyper-Ray", None))
        self.box_sp_weapon_5.setItemText(2, QCoreApplication.translate("MainWindow", u"C: Search", None))
        self.box_sp_weapon_5.setItemText(3, QCoreApplication.translate("MainWindow", u"D: Burst", None))
        self.box_sp_weapon_5.setItemText(4, QCoreApplication.translate("MainWindow", u"E: Verteblade", None))
        self.box_sp_weapon_5.setItemText(5, QCoreApplication.translate("MainWindow", u"F: Thunder", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Redlichia Rex", None))
        self.box_option_shot.setItemText(0, QCoreApplication.translate("MainWindow", u"Blue: Vulcan", None))
        self.box_option_shot.setItemText(1, QCoreApplication.translate("MainWindow", u"Green: Wide", None))
        self.box_option_shot.setItemText(2, QCoreApplication.translate("MainWindow", u"Red: Power", None))
        self.box_option_shot.setItemText(3, QCoreApplication.translate("MainWindow", u"Purple: Multiway", None))

        self.label_main_shot.setText(QCoreApplication.translate("MainWindow", u"Main Shot", None))
        self.box_rating.setItemText(0, QCoreApplication.translate("MainWindow", u"1: Bad", None))
        self.box_rating.setItemText(1, QCoreApplication.translate("MainWindow", u"2: Good", None))
        self.box_rating.setItemText(2, QCoreApplication.translate("MainWindow", u"3: Great", None))

        self.label_option_shot.setText(QCoreApplication.translate("MainWindow", u"Option Shot", None))
        self.label_rating.setText(QCoreApplication.translate("MainWindow", u"Overall Rating", None))
        self.box_main_shot.setItemText(0, QCoreApplication.translate("MainWindow", u"Blue: Vulcan", None))
        self.box_main_shot.setItemText(1, QCoreApplication.translate("MainWindow", u"Green: Wide", None))
        self.box_main_shot.setItemText(2, QCoreApplication.translate("MainWindow", u"Red: Power", None))
        self.box_main_shot.setItemText(3, QCoreApplication.translate("MainWindow", u"Purple: Multiway", None))

        self.line_notes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Add Life Form", None))
        self.button_update.setText(QCoreApplication.translate("MainWindow", u"Update Life Form", None))
        self.button_remove.setText(QCoreApplication.translate("MainWindow", u"Remove Life Form", None))
        self.button_remove_all.setText(QCoreApplication.translate("MainWindow", u"Remove All", None))
        self.group_search.setTitle(QCoreApplication.translate("MainWindow", u"Wonderful Life Form Database", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Overall Rating", None))
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wonder Life Forms", None))
        self.box_search_life_forms.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.box_search_life_forms.setItemText(1, QCoreApplication.translate("MainWindow", u"Cyclopyge Unbonata", None))
        self.box_search_life_forms.setItemText(2, QCoreApplication.translate("MainWindow", u"Marrella Splendense", None))
        self.box_search_life_forms.setItemText(3, QCoreApplication.translate("MainWindow", u"Hallucigenia Sparsa", None))
        self.box_search_life_forms.setItemText(4, QCoreApplication.translate("MainWindow", u"Sarotrocercus Oblita", None))
        self.box_search_life_forms.setItemText(5, QCoreApplication.translate("MainWindow", u"Burgessia Bella", None))
        self.box_search_life_forms.setItemText(6, QCoreApplication.translate("MainWindow", u"Redlichia Rex", None))

        self.box_search_life_forms.setPlaceholderText("")
        self.box_search_rating.setItemText(0, QCoreApplication.translate("MainWindow", u"Any", None))
        self.box_search_rating.setItemText(1, QCoreApplication.translate("MainWindow", u"1: Bad", None))
        self.box_search_rating.setItemText(2, QCoreApplication.translate("MainWindow", u"2: Good", None))
        self.box_search_rating.setItemText(3, QCoreApplication.translate("MainWindow", u"3: Great", None))

        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Wonderful Life Form", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Main Shot", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Option Shot", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Clone Eyes", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Special Weapon", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Overall Rating", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Notes", None));
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

