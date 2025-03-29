from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from typing import List
import requests
import os

class PreviewDialog(QMainWindow):
    def __init__(self, parent=None, file_link: str = ""):
        super().__init__(parent)
        self.setWindowTitle("预览")
        self.resize(400,302)

        # 支持的图片、音频格式列表
        web_formats: List[str] = ["jpg", "png", "jpeg", "gif", "svg", "wav", "mp3", "ogg", "html", "htm"]
        # 支持的文本格式列表
        text_formats: List[str] = ["txt", "py", "java", "c", "cpp", "css", "js", "markdown", "md", "xml", "json"]

        # 获取文件扩展名
        file_extension: str = file_link.split(".")[-1]

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        if file_extension in web_formats:
            # 如果是图片格式，使用QWebEngineView来显示
            self.PreviewWidget = QWebEngineView(self)
            self.PreviewWidget.setUrl(QUrl(file_link))
            self.PreviewWidget.setObjectName(u"PreviewWidget")
            layout.addWidget(self.PreviewWidget)
        elif file_extension in text_formats:
            # 如果是文本格式，使用QTextBrowser来显示
            self.PreviewWidget = QTextBrowser(self)
            try:
                response = requests.get(file_link)
                response.raise_for_status()
                text: str = response.content.decode("utf-8")
                self.PreviewWidget.setText(text)
            except requests.RequestException as e:
                self.PreviewWidget.setText(f"无法加载文件: {str(e)}")
            self.PreviewWidget.setObjectName(u"PreviewWidget")
            layout.addWidget(self.PreviewWidget)
        elif file_extension == "pdf":
            # 如果是PDF格式，使用QPdfWidget来显示
            pdfdocument = QPdfDocument(self)
            with open("tmp.pdf", "wb") as f:
                response = requests.get(file_link)
                response.raise_for_status()
                f.write(response.content)
            pdfdocument.load("tmp.pdf")
            self.PreviewWidget = QPdfView(self)
            self.PreviewWidget.setDocument(pdfdocument)
            self.PreviewWidget.setObjectName(u"PreviewWidget")
            layout.addWidget(self.PreviewWidget)
        else:
            # 如果文件格式不受支持，显示提示信息
            self.PreviewWidget = QLabel(self)
            self.PreviewWidget.setText("暂不支持预览该文件类型")
            self.PreviewWidget.setObjectName(u"PreviewWidget")
            layout.addWidget(self.PreviewWidget)
        
        central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication()
    preview_dialog = PreviewDialog(file_link="https://livefile.xesimg.com/programme/python_assets/2e954073e199186d50f1890ae3ab5694.pdf")
    preview_dialog.show()
    app.exec()