from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
import sys


class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow,self).__init__()
    self.initUI()

  def initUI(self):
    self.setGeometry(400, 400, 500, 500)
    self.setWindowTitle("Mass YouTube Downloader")
    grid_layout = QGridLayout()

    self.label = QtWidgets.QLabel(self)
    self.label.setText("my first label!")
    grid_layout.addWidget(self.label, 1, 1)

    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("click me!")
    self.b1.clicked.connect(self.button_clicked)

  def button_clicked(self):
    self.label.setText("you pressed the button")
    self.update()


  def update(self):
    self.label.adjustSize()


def window():
  app = QApplication(sys.argv)
  win = MyWindow()
  win.show()
  sys.exit(app.exec_())

window()