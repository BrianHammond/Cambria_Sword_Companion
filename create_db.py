import sys
from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery

def create_db():
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName("wonder_lifeforms.db")
    if not database.open():
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