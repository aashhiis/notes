from PyQt5.QtWidgets import *
from notes_data import load_notes, save_notes

app = QApplication([])

window = QWidget()
window.setWindowTitle("Умные заметки")
window.resize(700, 500)

notes = load_notes()

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()

list_notes = QListWidget()
text_note = QTextEdit()

button_create = QPushButton("Создать")
button_save = QPushButton("Сохранить")
button_delete = QPushButton("Удалить")

left_layout.addWidget(QLabel("Список заметок"))
left_layout.addWidget(list_notes)
left_layout.addWidget(button_create)
left_layout.addWidget(button_delete)

right_layout.addWidget(QLabel("Текст заметки"))
right_layout.addWidget(text_note)
right_layout.addWidget(button_save)

main_layout.addLayout(left_layout, 2)
main_layout.addLayout(right_layout, 5)

window.setLayout(main_layout)


def show_notes():
    list_notes.clear()
    for name in notes:
        list_notes.addItem(name)


def open_note():
    item = list_notes.currentItem()

    if item:
        name = item.text()
        text_note.setText(notes[name])


def create_note():
    name, ok = QInputDialog.getText(window, "Создать", "Название заметки:")

    if ok:
        if name == "":
            QMessageBox.warning(window, "Ошибка", "Пустое название")
        elif name in notes:
            QMessageBox.warning(window, "Ошибка", "Уже есть")
        else:
            notes[name] = ""
            save_notes(notes)
            show_notes()


def save_note():
    item = list_notes.currentItem()

    if not item:
        QMessageBox.warning(window, "Ошибка", "Выберите заметку")
    else:
        name = item.text()
        notes[name] = text_note.toPlainText()
        save_notes(notes)
        QMessageBox.information(window, "Ок", "Сохранено")


def delete_note():
    item = list_notes.currentItem()

    if not item:
        QMessageBox.warning(window, "Ошибка", "Выберите заметку")
    else:
        name = item.text()
        del notes[name]
        text_note.clear()
        save_notes(notes)
        show_notes()


list_notes.itemClicked.connect(open_note)
button_create.clicked.connect(create_note)
button_save.clicked.connect(save_note)
button_delete.clicked.connect(delete_note)

show_notes()

window.show()
app.exec_()