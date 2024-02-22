import sys
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem,QLabel,QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="1234.abcd",
    database="BANCO"
)
cursor = cx.cursor()

class AtualizarClientes(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("Clientes cadastrados")
      
        labelId = QLabel("Id cliente:")
        self.editId = QLineEdit()

        labelNome = QLabel("Nome Completo:")
        self.editNome = QLineEdit()

        labelEmail = QLabel("E-Mail:")
        self.editEmail = QLineEdit()

        labelTelefone = QLabel("Telefone:")
        self.editTelefone = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")
        
        layout.addWidget(labelId)
        layout.addWidget(self.editId)

        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)

        layout.addWidget(labelEmail)
        layout.addWidget(self.editEmail)

        layout.addWidget(labelTelefone)
        layout.addWidget(self.editTelefone)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCli)

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

       
        layout.addWidget(tbclientes)
        self.setLayout(layout)
    
    def upCli(self):
        if(self.editId.text()==""):
            print("Não é possível atualizar sem o id do cliente")
        elif(self.editNome.text()!="" and self.editEmail.text()=="" and self.editTelefone.text()==""):
            print("Não é possível atualizar se não houver dados")
       
        elif(self.editNome.text()!="" and self.editEmail.text()=="" and self.editTelefone.text()==""):
            cursor.execute("update CLIENTES set NOMEcliente=%s where CLIENTESid=%s",
                           (self.editNome.text(), self.editId.text()))
       
        elif(self.editNome.text()=="" and self.editEmail.text()!="" and self.editTelefone.text()==""):
            cursor.execute("update CLIENTES set EMAILcliente=%s where CLIENTESid=%s",
                           (self.editEmail.text(), self.editId.text()) )
       
        elif(self.editNome.text()=="" and self.editEmail.text()=="" and self.editTelefone.text()!=""):
            cursor.execute("update CLIENTES set TELEFONEcliente=%s where CLIENTESid=%s",
                           (self.editTelefone.text(), self.editId.text()) )
        else:
            cursor.execute("update CLIENTES set NOMEcliente=%s, EMAILcliente=%s, TELEFONEcliente=%s where CLIENTESid=%s",
                           (self.editNome.text(), self.editEmail.text(), self.editTelefone.text(),self.editId.text()))
            
        cx.commit()
        print("Atualizado")
if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarClientes()
    tela.show()
    sys.exit(app.exec_())