#from flask import Flask
#application = Flask(__name__)

#@application.route('/')
#def hello_world():
#    return "Hola, Tepic! iwuser02 > Victor \r\n", 200, { 'Content-Type': 'text/plain' }



#if __name__ == '__main__':
#  application.run(debug = True)


import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Ventana PyQT-5')
    w.setWindowIcon(QIcon('icon.ico'))

    btn = QPushButton('Este es un Button', w)
    btn.setToolTip('This is a <b>QPushButton</b> widget')
    btn.move(150, 50)

    btn.setIcon(QIcon('icon.ico'))
    btn.clicked.connect(QCoreApplication.instance().quit)

    w.resize(1280, 720)
    w.show()

    sys.exit(app.exec_())

