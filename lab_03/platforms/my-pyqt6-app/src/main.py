import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from ceasar_view import CeasarView
from rsa_view import RSAView

class MainWindow(QMainWindow):  # Change QStackedWidget to QMainWindow
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/ui/main_window.ui', self)
        
        # Initialize views
        self.ceasar_view = CeasarView()
        self.rsa_view = RSAView()

        # Add views to the stacked widget
        self.stackedWidget.addWidget(self.ceasar_view)
        self.stackedWidget.addWidget(self.rsa_view)

        # Connect buttons to switch views
        self.btn_ceasar.clicked.connect(self.show_ceasar)
        self.btn_rsa.clicked.connect(self.show_rsa)

    def show_ceasar(self):
        self.stackedWidget.setCurrentWidget(self.ceasar_view)

    def show_rsa(self):
        self.stackedWidget.setCurrentWidget(self.rsa_view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())