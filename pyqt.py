from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
pyqt = uic.loadUi("pyqt.ui")


pyqt.show()
app.exec()
