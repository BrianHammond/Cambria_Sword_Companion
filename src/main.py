import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QSettings
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui
import qdarkstyle

class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.create_db()
        self.setupUi(self)
        self.settings_manager = SettingsManager(self)  # Initialize the SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts

        # Push Buttons
        self.button_add.clicked.connect(self.add_lifeform)
        self.button_update.clicked.connect(self.update_lifeform)
        self.button_remove.clicked.connect(self.remove_lifeform)
        self.button_remove_all.clicked.connect(self.remove_all)
        self.button_search.clicked.connect(self.search_lifeform)
        
        # Menu Bar
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.show_about_qt)
        self.action_dark_mode.toggled.connect(self.dark_mode)

        self.query_db()

    def add_lifeform(self):
        wonderful_group_index = self.tabWidget.currentIndex() # get the index number for each tab
        life_form = self.tabWidget.tabText(wonderful_group_index) # get tab names (e.g. each Wonderful Life Form)
        
        clone_eyes_index = f"box_eyes_{wonderful_group_index}" # add the wonderful_group_index suffix to the combobox name (e.g. cb_eyes_0)
        clone_eyes_get = getattr(self, clone_eyes_index) # clone_eyes_get = cb_eyes_0 - 5 (depending on which tab you're on)
        clone_eyes = clone_eyes_get.currentText() # grab the text in the clone eyes combo box

        sp_weapon_index = f"box_sp_weapon_{wonderful_group_index}" # add the wonderful_group_index suffix to the sp_weapon name (e.g. cb_sp_weapon_0)
        sp_weapon_get = getattr(self, sp_weapon_index) # sp_weapon_get = cb_sp_weapon_0 - 5 (depending on which tab you're on)
        sp_weapon = sp_weapon_get.currentText() # grab the text in the special weapon combo box
        
        main_shot = self.box_main_shot.currentText()
        option_shot = self.box_option_shot.currentText()
        rating = self.box_rating.currentText()

        notes = self.line_notes.text()
       
        query = QSqlQuery()
        query.prepare("""
                    INSERT INTO lifeforms (life_form, main_shot, option_shot, clone_eyes, sp_weapon, rating, notes)
                    VALUES(?, ?, ?, ?, ?, ?, ?)
                    """)
        query.addBindValue(life_form)
        query.addBindValue(main_shot)
        query.addBindValue(option_shot)
        query.addBindValue(clone_eyes)
        query.addBindValue(sp_weapon)
        query.addBindValue(rating)
        query.addBindValue(notes)

        query.exec()

        self.query_db() # this will load the database back into the table with the updated information

        self.line_notes.clear()  # Clear the notes input field after adding the lifeform
       
    def update_lifeform(self):
        notes = self.line_notes.text()
        selected_row = self.table.currentRow()
 
        if selected_row == -1:
            QMessageBox.warning(self, "no life form chosen", "please choose a wonderful life form to update")
            return

        id = int(self.table.item(selected_row, 0).text())
        life_form = self.table.item(selected_row, 1).text()
        main_shot = self.table.item(selected_row, 2).text()
        option_shot = self.table.item(selected_row, 3).text()
        clone_eyes = self.table.item(selected_row, 4).text()
        sp_weapon = self.table.item(selected_row, 5).text()
        rating = self.table.item(selected_row, 6).text()
        notes = self.table.item(selected_row, 7).text()

        confirm = QMessageBox.question(self, "Are you sure?", "Update life form Information?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.No:
            return

        query = QSqlQuery()
        
        query.prepare("""
                      UPDATE lifeforms SET life_form = ?, main_shot = ?, option_shot = ?, clone_eyes = ?, sp_weapon = ?, rating = ?, notes = ? WHERE id = ?
                      """)
        
        query.addBindValue(life_form)
        query.addBindValue(main_shot)
        query.addBindValue(option_shot)
        query.addBindValue(clone_eyes)
        query.addBindValue(sp_weapon)
        query.addBindValue(rating)
        query.addBindValue(notes)
        query.addBindValue(id)

        query.exec()

        self.query_db()

        self.line_notes.clear()  # Clear the notes input field

    def remove_lifeform(self):
        self.line_notes.clear()  # Clear the notes input field
        
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Wonderful Life Form chosen", "Please choose a Wonderful Life Form to remove")
            return

        id = int(self.table.item(selected_row, 0).text())

        confirm = QMessageBox.question(self, "Are you sure?", "Remove Wonderful Life Form?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM lifeforms WHERE id = ?")
        query.addBindValue(id)

        query.exec()

        self.query_db()

    def remove_all(self):
        self.line_notes.clear()  # Clear the notes input field

        confirm = QMessageBox.question(self, "Are you sure?", "Are you sure you want to delete?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        match confirm:
            case QMessageBox.StandardButton.No:
                return
            case QMessageBox.StandardButton.Yes:
                confirm2  = QMessageBox.question(self, "Are you sure?", "Dude, are you like really sure you want to delete?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                match confirm2:
                    case QMessageBox.StandardButton.No:
                        return

        query = QSqlQuery()
        query.prepare("DELETE FROM lifeforms")

        query.exec()

        self.query_db()

    def search_lifeform (self):
        self.table.setRowCount(0)
        
        search_life_forms = self.box_search_life_forms.currentText()
        if search_life_forms == 'All':
            search_life_forms = '%'
        else:
            search_life_forms = self.box_search_life_forms.currentText()

        search_rating = self.box_search_rating.currentText()
        if search_rating == 'Any':
            search_rating = '%'
        else:
            search_rating = self.box_search_rating.currentText()

        query = QSqlQuery("""
                          SELECT * FROM lifeforms where 
                          (life_form like ?) and
                          (rating like ?) 
                          """)
        
        query.addBindValue(search_life_forms)
        query.addBindValue(search_rating)

        query.exec()
        
        row = 0
        while query.next(): # while loop to query all the rows in the database and add them to the table
            self.populate_table(query, row)
            row += 1

    def query_db(self): # queries the database and updates the table
        self.table.setRowCount(0)

        query = QSqlQuery("SELECT * FROM lifeforms")

        row = 0
        while query.next(): # while loop to query all the rows in the database and add them to the table
            self.populate_table(query, row)
            row += 1

    def populate_table(self, query, row):
        # these query the database to get each values
        id = query.value(0)
        life_form = query.value(1)
        main_shot = query.value(2)
        option_shot = query.value(3)
        clone_eyes = query.value(4)
        sp_weapon = query.value(5)
        rating = query.value(6)
        notes = query.value(7)

        # the queried values are then populated to the table
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(['ID','Life Form','Main Shot','Option Shot','Clone Eyes','Special Weapon','Rating','Notes'])
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem('  '+str(id)+'  '))
        self.table.setItem(row, 1, QTableWidgetItem('  '+life_form+'  '))
        self.table.setItem(row, 2, QTableWidgetItem('  '+main_shot+'  '))
        self.table.setItem(row, 3, QTableWidgetItem('  '+option_shot+'  '))
        self.table.setItem(row, 4, QTableWidgetItem('  '+clone_eyes+'  '))
        self.table.setItem(row, 5, QTableWidgetItem('  '+sp_weapon+'  '))
        self.table.setItem(row, 6, QTableWidgetItem('  '+rating+'  '))
        self.table.setItem(row, 7, QTableWidgetItem('  '+notes+'  '))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
    def create_db(self): # creates a database if none is found
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("wonder_lifeforms.db")
        if not self.database.open():
            QMessageBox.critical(None, "Error","Could not open your database")
            sys.exit(1)

        query = QSqlQuery()
        query.exec("""
                    CREATE TABLE IF NOT EXISTS lifeforms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        life_form TEXT,
                        main_shot TEXT,
                        option_shot TEXT,
                        clone_eyes TEXT,
                        sp_weapon TEXT,
                        rating TEXT,
                        notes TEXT
                    )
                    """)

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self): # loads the About window
        self.about_window = AboutWindow(dark_mode=self.action_dark_mode.isChecked())
        self.about_window.show()

    def show_about_qt(self):
        QApplication.aboutQt()

    def closeEvent(self, event): #settings will save when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()

class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.action_dark_mode.isChecked())

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
