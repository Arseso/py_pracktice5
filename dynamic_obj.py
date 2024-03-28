import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QPoint, QMimeData
from PySide6.QtGui import QDrag

class DragButton(QPushButton):
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            print("[I] DragEventSuccess")
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec(Qt.MoveAction)

class Window(QWidget):
     def __init__(self):
        super().__init__()
        self.setWindowTitle("Draggable Widgets")
        self.setGeometry(100, 100, 400, 300)

        self.lower_widget = QWidget(self)
        self.lower_widget.setGeometry(50, 150, 200, 100)
        self.lower_widget.setStyleSheet("background-color: blue;")
        self.lower_widget.setAcceptDrops(True)

     def create_red_widget(self, e):
        widget = DragButton(self)
        widget.setFixedSize(100, 100)
        widget.setStyleSheet("background-color: black;")
        widget.move(e)
        widget.show()
        print("[I] Red widget created")

     def mousePressEvent(self, e):
         if e.button() == Qt.RightButton:
             if e.y() < self.height() / 2:
                self.create_red_widget(e.pos())
     def dragEnterEvent(self, e):
         print("[I] DragEnter")
         e.accept()

     def dropEvent(self, e):
         print("[I] DropEvent before")
         pos = e.position()
         widget = e.source()
         for n in range(self.layout.count()):
             w = self.layout.itemAt(n).widget()
             if pos.x() < w.x() + w.size().width() // 2:
                 self.layout.insertWidget(n-1, widget)
                 break
         e.accept()
         print("[I] DropEvent after")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


