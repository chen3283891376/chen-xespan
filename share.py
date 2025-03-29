from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import Ui_ShareDialog
from typing import Dict
import download
import json

class ShareDialog(QDialog, Ui_ShareDialog):
    def __init__(self, parent=None, file_info: Dict[str, str]=None):
        super().__init__(parent)
        self.setupUi(self)
        self.shareURL = json.dumps(file_info)
        self.clipboard = QClipboard()

        if file_info:
            self.lineEdit.setText(str(self.shareURL))
            self.pushButton.clicked.connect(self.copyLink)
        else:
            self.pushButton.setEnabled(False)
            self.lineEdit.setEnabled(False)
        self.pushButton_3.clicked.connect(self.downloadFile)
    
    def copyLink(self) -> None:
        self.clipboard.setText(str(self.shareURL))
    
    def downloadFile(self) -> None:
        if not self.lineEdit_2.text():
            QMessageBox.warning(self, "错误", "请先输入分享链接！")
            return
        file_path = QFileDialog.getExistingDirectory(self, "下载文件", "")
        if file_path:
            download_dialog = download.DownloadDialog(
                parent=self,
                file_info=json.loads(self.lineEdit_2.text()),
                download_path=file_path
            )
            download_dialog.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    preview_dialog = ShareDialog(
        file_info={
            'link': 'https://livefile.xesimg.com/programme/python_assets/ba44a9e13264e6310378f6e8e24ede81.zip', 
            'name': 'pygame.zip',
            'size': '5MB'
        }
    )
    preview_dialog.show()
    sys.exit(app.exec())
