import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtCore import Qt, QPoint

class DraggableWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)
        self.setStyleSheet("background-color: red;")
        self.setMouseTracking(True)
        self.dragging = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
            self.dragging = True

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToParent(event.pos() - self.drag_start_position))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draggable Widgets")
        self.setGeometry(100, 100, 400, 300)

        self.lower_widget = QWidget(self)
        self.lower_widget.setGeometry(50, 150, 200, 100)
        self.lower_widget.setStyleSheet("background-color: blue;")
        self.lower_widget.setAcceptDrops(True)

    def create_red_widget(self, position):
        widget = DraggableWidget(self)
        widget.move(position)
        widget.show()
        print("[I] Red widget created")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.y() < self.height() / 2:
                self.create_red_widget(event.pos())

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-dnditemdata"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        position = event.pos()
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            widget = QLabel(event.mimeData().text(), self)
            widget.move(position)
            widget.show()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())

