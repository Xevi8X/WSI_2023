import sys
from subprocess import Popen, PIPE
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile
from gui.stocker import Ui_MainWindow
from data_collector import collect_data2

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.trainButton.clicked.connect(self.trainNN)
        self.ui.predictingChooseNNButton.clicked.connect(self.browseFiles)

    def trainNN(self):
        stock_name = self.ui.trainingStockLineEdit.text()
        start = self.ui.trainingFromDateEdit.date().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        end = self.ui.trainingToDateEdit.date().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)
        epochNo = self.ui.trainEpochSpinBox.value()
        filename = collect_data2(stock_name, start, end, interval="1d")
        process = Popen(['python', 'train.py'], stdout=PIPE,bufsize=1, universal_newlines=True)
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
        

        
    def browseFiles(self):
        fname=QFileDialog.getOpenFileName(self,'Open file', '.', '(*.h5)')
        self.ui.predictingChosenNNLineEdit.setText(fname[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()
    window.show()

    sys.exit(app.exec())