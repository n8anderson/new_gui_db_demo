import gui
import sys
import sqlite3 as sql


def main():
    # Main database stuff here
    conn, curs = sql.connect('north_star_db.db')


    # get_info(cursor, id) # May want to consider including this in GUI
    app = gui.QApplication(sys.argv)
    ex = gui.Window(conn, curs)
    ex.isHidden()
    sys.exit(app.exec_())

main()