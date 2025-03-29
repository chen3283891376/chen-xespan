from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .ui_login import Ui_Dialog
from . import cloudvar
import hashlib

class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.name = ""

        self.pushButton.clicked.connect(self.login)
    
    def login(self):
        username = "unnamed_user-not found"
        password = self.lineEdit_2.text()
        if username == "" or password == "":
            QMessageBox.warning(self, "提示", "请输入用户名和密码")
            return
        password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        user_list = cloudvar.get_var("cloudpan-login")["data"]["data"]
        for i in user_list:
            if i["user"] == self.lineEdit.text():
                userinfo = i
                username = i["user"]
                break
        if username == "unnamed_user-not found":
            QMessageBox.warning(self, "提示", "未找到该用户，请先去注册")
            return
        if userinfo["password"] != password:
            QMessageBox.warning(self, "提示", "用户名或密码不正确，请再确认一遍")
            return
        self.name = username
        QMessageBox.information(self, "提示", "登录成功")
        self.accept()

if __name__ == '__main__':
    app = QApplication()
    app.setStyle("windows11")
    login = LoginDialog()
    login.show()
    app.exec()