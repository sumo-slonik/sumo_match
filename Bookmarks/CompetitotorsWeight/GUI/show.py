import sys

from Bookmarks.CompetitotorsWeight.GUI.CompetitorsWeight import MainWindow
from Bookmarks.CompetitotorsWeight.GUI.main_window import Ui_MainWindow
from Bookmarks.CompetitotorsWeight.GUI.ui_competitiorsWeight import *





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
