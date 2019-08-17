import sys, os
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
import time

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        #img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        #img.save('capture.png')
        #img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        from PyQt5.QtWidgets import QMessageBox, QInputDialog
        reply = QMessageBox.question(self, 'Continue?', 
                 'Do you want to reselect ?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            restart(self)
        else:
            n, okPressed = QInputDialog.getInt(self, " ","Enter total number of pages, you will get 5 seconds to go fullscreen in kindle pc", 0, 0, 100000000, 1)
            if okPressed:
                time.sleep(5)
                print(n)
                for i in range(n):
                    time.sleep(0.4)
                    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
                    im.save(str(i)+".jpg")
                    time.sleep(0.15)
                    action("right")

            cv2.imshow('Captured Image', img)
            cv2.waitKey(0)
            #cv2.destroyAllWindows()


def restart(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

def action(key):
    pyautogui.press(key)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
