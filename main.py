import sys
import time
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication
from main_status_layout import Ui_MainWindow
from home_page import Ui_HomePage

class Page1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Page1, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


######### test button page dummy ref
#class Page2(QtWidgets.QMainWindow):
#    def __init__(self):
#        super(Page2, self).__init__()
#        self.ui = Ui_Page2()
#        self.ui.setupUi(self)
#        self.ui.anotherButton.clicked.connect(self.another_function)  # Example button
#
#    def another_function(self):
#        # Functionality for Page 2
#        print("Button on Page 2 clicked!")
######### till here


class HomePage(QtWidgets.QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        self.ui = Ui_HomePage()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Connect buttons on the home page
        self.ui.freespace_btn.clicked.connect(self.open_page1)  # Button to open Page 1
        self.ui.wired_btn.clicked.connect(self.open_page2)  # Button to open Page 2

    def open_page1(self):
        try:
            time.sleep(1)
            self.page1 = Page1()
            self.page1.show()
            self.close()
        except Exception as e:
            print(e)

    def open_page2(self):
        self.page2 = Page1()
        self.page2.show()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    home = HomePage()
    home.show()
    sys.exit(app.exec())
