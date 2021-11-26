import gui
import sys

def main():
    # Main database stuff here
    name = 'taco_tower.db'

    # get_info(cursor, id) # May want to consider including this in GUI
    app = gui.QApplication(sys.argv)
    ex = gui.Window(conn, curs)
    ex.isHidden()
    sys.exit(app.exec_())

main()