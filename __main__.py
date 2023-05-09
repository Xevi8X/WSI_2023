import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile
from stocker import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.trainButton.clicked.connect(lambda _ : print("Y"))
        self.ui.predictingChooseNNButton.clicked.connect(self.browseFiles)

    def browseFiles(self):
        fname=QFileDialog.getOpenFileName(self,'Open file', '.', '(*.h5)')
        self.ui.predictingChosenNNLineEdit.setText(fname[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()
    window.show()

    sys.exit(app.exec())