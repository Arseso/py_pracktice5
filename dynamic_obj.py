from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QMainWindow


class interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lab4.2")
        self.setFixedSize(500, 500)

        self.drag = DragLabel("", self)
        self.drag.setGeometry(0, 0, 500, 250)
        self.drag.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.drag.setStyleSheet("padding: 10px;")

        self.destination = QLabel("", self)
        self.destination.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.destination.setGeometry(0, 250, 500, 250)
        self.destination.setStyleSheet("background-color: blue")


class DragLabel(QLabel):
    eventHappened = Signal(str)

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.parent = parent
        self.setStyleSheet("border: 2px solid black; padding: 10px;")
        self.count = 0

    def mousePressEvent(self, event):
        newL = Dragable(self.parent, event.x(), event.y())


class Dragable(QLabel):
    evenHappened = Signal(str)

    def __init__(self, parent=None, x=0, y=0):
        super().__init__(parent)
        self.parent = parent
        self.setStyleSheet("background-color: red;")
        self.setGeometry(x - 25, y - 25, 50, 50)
        self.flag = False
        self.show()

    def mousePressEvent(self, event):
        self.flag = True

    def mouseReleaseEvent(self, event):
        self.flag = False;

    def mouseMoveEvent(self, event):
        if (self.flag == True):
            global_pos = event.globalPos()
            parent_pos = self.parent.mapFromGlobal(global_pos)
            self.move(parent_pos - self.rect().center())
