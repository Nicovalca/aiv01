import sys
import json
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QComboBox, QHBoxLayout
from howdoi import howdoi

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    # set as property in case i need to do something with engine_combo before giving result
    @property
    def search_engine(self):
        return self.engine_combo.currentText()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HowDoI - App")
        self.setFixedSize(480,480)

        self.input = QLineEdit()

        self.engine_combo = QComboBox()
        self.engine_combo.addItems(howdoi.SUPPORTED_SEARCH_ENGINES) 

        search_row = QHBoxLayout()
        search_row.addWidget(QLabel("Search engine: "))
        search_row.addWidget(self.engine_combo)

        self.lbl_answer = QTextEdit()        

        self.lbl_info = QLabel()
        self.lbl_info.setWordWrap(True)

        button = QPushButton("Ask")
        button.clicked.connect(self.on_button_ask_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addItem(search_row)
        layout.addWidget(self.lbl_answer)
        layout.addWidget(self.lbl_info)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        
        # Set the central widget of the window
        self.setCentralWidget(container)


    def on_button_ask_clicked(self):                
        question = self.input.text()
        params = " -j -e "
        engine = self.search_engine

        # how do I use this method in async way, so i can show a "loading" animation while waiting for the answer?
        ans = howdoi.howdoi(''.join([question, params, engine]))
        data = json.loads(ans)
        
        if not "error" in data:
            for answer in data:
                self.lbl_answer.setHtml(answer['answer'])
                self.lbl_info.setText(answer['link'])
        else:
            self.lbl_answer.setHtml(answer['error'])
       
            
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

# to ask: why if don't use this, when i call howdoi.howdoi, new instances of QWindow appears until the howdoi script return the answer
# is that becuase howdoi is a web request and due to the nature of qt this script is executed each tick while the process is busy?
if __name__ == "__main__":
    main()
    
