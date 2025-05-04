from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import Ui_MainWindow
from login import LoginDialog
from preview import PreviewDialog
from download import DownloadDialog
from share import ShareDialog
from typing import List, Dict
from datetime import datetime
import utils.cloudvar as cloudvar
from utils.utils import get_size
import os
import upload
import sys

# 创建应用
app = QApplication()
# 获取用户ID和云盘数据
try:
    user_id: str = sys.argv[1].split("stu_id=")[1].split("; ")[0]
except IndexError:
    QMessageBox.critical(None, "错误", "看来你不是xes用户，先登录/注册吧！")
    login = LoginDialog()
    login.show()
    if login.exec():
        user_id: str = login.name
    else:
        sys.exit()
    del app, login
token: str = ""
files: List[Dict[str, str]] = []
pan_data = cloudvar.get_var(f"cloudpan-{user_id}")

if pan_data["status"] == "error":
    QMessageBox.information(None, "你好！", "很好，这是你第一次使用云盘，点击确定，我们将为您注册（")
    new_data = cloudvar.new_var(f"cloudpan-{user_id}", {"files": [], "token": ""})
    token = new_data["token"]
    files = []
    cloudvar.set_var(f"cloudpan-{user_id}", {"files": [], "token": token}, token)
else:
    QMessageBox.information(None, "欢迎回来", "看来是故地重游啊（")
    token = pan_data["data"]["token"]
    files = pan_data["data"]["files"]

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.selected_file = None
        self.populate_file_tree()

        self.pub_1.clicked.connect(self.upload_file)
        self.pub_2.clicked.connect(self.preview_file)
        self.pub_3.clicked.connect(self.download_file)
        self.pub_4.clicked.connect(self.delete_file)
        self.pub_5.clicked.connect(self.share_file)
        self.treeWidget.currentItemChanged.connect(self.update_file_name)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """拖放文件到窗口"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event: QDropEvent):
        """拖放文件到窗口"""
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if os.path.isfile(file_path):
                    if os.path.getsize(file_path) > 1024**3 * 2:  # 限制文件大小
                        print("不支持上传超过2GB的文件")
                        return
                    self.upload_file_name = file_path
                    self.upload_file_size = get_size(os.path.getsize(self.upload_file_name))
                    self.link = ""
                    upload_dialog = upload.UploadDialog(self, self.upload_file_name)
                    upload_dialog.finished.connect(self.upload_finished)
                    upload_dialog.show()


    def populate_file_tree(self):
        """将文件添加到树形控件中"""
        for file in files:
            item = QTreeWidgetItem([file["name"], file["size"], file["time"]])
            item.setFont(0, QFont("微软雅黑", 12))
            item.setFont(1, QFont("微软雅黑", 12))
            item.setFont(2, QFont("微软雅黑", 12))
            self.treeWidget.addTopLevelItem(item)

    def upload_file(self):
        """上传文件并更新树形控件和云盘数据"""
        self.upload_file_name, _ = QFileDialog.getOpenFileName(self, "上传文件", "", "All Files (*)")
        if self.upload_file_name:
            if os.path.getsize(self.upload_file_name) > 1024**3 * 2:  # 限制文件大小
                print("不支持上传超过2GB的文件")
                return
            self.upload_file_size = get_size(os.path.getsize(self.upload_file_name))
            self.link = ""
            upload_dialog = upload.UploadDialog(self, self.upload_file_name)
            upload_dialog.finished.connect(self.upload_finished)
            upload_dialog.show()
    
    def upload_finished(self, link: str):
        """上传完成后更新文件信息"""
        file_info = {
            "name": os.path.basename(self.upload_file_name),
            "size": self.upload_file_size,
            "time": str(datetime.now().date()),
            "link": link
        }
        files.append(file_info)

        self.add_file_to_tree(file_info)
        cloudvar.set_var(f"cloudpan-{user_id}", {"files": files, "token": token}, token)

        del self.upload_file_name, self.upload_file_size, self.link

    def add_file_to_tree(self, file_info: Dict[str, str]):
        """在树形控件中添加文件信息"""
        item = QTreeWidgetItem([file_info["name"], file_info["size"], file_info["time"]])
        item.setFont(0, QFont("微软雅黑", 12))
        item.setFont(1, QFont("微软雅黑", 12))
        item.setFont(2, QFont("微软雅黑", 12))
        self.treeWidget.addTopLevelItem(item)

    def download_file(self):
        """下载所选文件"""
        file_path = QFileDialog.getExistingDirectory(self, "下载文件", "")
        if file_path:
            dialog = DownloadDialog(self, self.selected_file, file_path)
            dialog.show()

    def delete_file(self):
        """删除所选文件"""
        if QMessageBox.question(self, "删除文件", "确认删除该文件吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            del files[self.treeWidget.currentIndex().row()]
            self.treeWidget.takeTopLevelItem(self.treeWidget.currentIndex().row())
            cloudvar.set_var(f"cloudpan-{user_id}", {"files": files, "token": token}, token)

    def preview_file(self):
        """预览所选文件"""
        dialog = PreviewDialog(self, self.selected_file["link"])
        dialog.show()
    
    def share_file(self):
        """分享所选文件"""
        dialog = ShareDialog(self, self.selected_file if self.selected_file else None)
        dialog.show()

    def update_file_name(self):
        """更新当前选中的文件信息"""
        try:
            self.selected_file = files[self.treeWidget.currentIndex().row()]
        except IndexError:
            pass
        self.pub_2.setEnabled(True)
        self.pub_3.setEnabled(True)
        self.pub_4.setEnabled(True)


if __name__ == "__main__":
    # import qdarkstyle
    app.setStyle("windows11")
    # app.styleHints().setColorScheme(Qt.ColorScheme.Dark)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    window = MainWindow()
    window.show()
    app.exec()
