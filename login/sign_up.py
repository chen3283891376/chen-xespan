from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui_SignUpDialog import Ui_SignUpDialog
from ..utils import cloudvar
import hashlib

TOKEN = "3dfa59e8-84a8-4129-85e9-5cb2d9b12ebd"

class SignUpDialog(QDialog, Ui_SignUpDialog):
    def __init__(self, parent=None):
        super(SignUpDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.pushButton.clicked.connect(self.sign_up)

    def sign_up(self):
        if self.lineEdit_2.text() != self.lineEdit_3.text():
            QMessageBox.warning(self, "警告", "两次输入的密码不一致！")
            return
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "":
            QMessageBox.warning(self, "警告", "请填写所有信息！")
            return
        user_list = cloudvar.get_var("cloudpan-login")["data"]["data"]
        pwd = hashlib.sha256(self.lineEdit_2.text().encode('utf-8')).hexdigest()
        user_info = {
            "user": self.lineEdit.text(),
            "password": pwd
        }
        for user in user_list:
            if user["user"] == self.lineEdit.text():
                QMessageBox.warning(self, "警告", "用户名已存在！")
                return
        user_list.append(user_info)
        cloudvar.set_var("cloudpan-login", {"data": user_list}, TOKEN)
        QMessageBox.information(self, "提示", "注册成功！")
        self.accept()

if __name__ == '__main__':
    app = QApplication()
    app.setStyle('windows11')
    dialog = SignUpDialog()
    dialog.show()
    app.exec()