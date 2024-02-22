import sys
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem, QVBoxLayout
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="1234.abcd",
    database="BANCO"
)
cursor = cx.cursor()

class ExibirClientes(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,300)
        self.setWindowTitle("Clientes cadastrados")

        tbclientes = QTableWidget(self)
        tbclientes.setColumnCount(4)
        tbclientes.setRowCount(10)

        headerLine=["Id","Nome","Email","Telefone"]

        tbclientes.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from CLIENTES")
        lintb = 0
        for linha in cursor:
            tbclientes.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbclientes.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbclientes.setItem(lintb,2,QTableWidgetItem(linha[2]))
            tbclientes.setItem(lintb,3,QTableWidgetItem(linha[3]))
            lintb+=1

        layout = QVBoxLayout()
        layout.addWidget(tbclientes)
        self.setLayout(layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = ExibirClientes()
    tela.show()
    sys.exit(app.exec_())