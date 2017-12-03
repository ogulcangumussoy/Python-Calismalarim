from PyQt5.QtWidgets import QDesktopWidget,QApplication,QRadioButton,QLineEdit,QWidget,QMainWindow,QAction,qApp,QHBoxLayout,QVBoxLayout,QFileDialog,QPushButton,QTextEdit,QLabel
from PyQt5 import QtGui
import sys,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Uygulama(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.resim=QLabel()
        self.resim.setPixmap(QtGui.QPixmap("gmail.png"))
        self.gondericiL=QLabel("Gönderici Eposta:")
        self.gonderici=QLineEdit("kaynakMail@gmail.com")
        self.aliciL=QLabel("Alıcı Eposta:")
        self.alici=QLineEdit()
        self.baslikL=QLabel("Başlık:")
        self.baslik=QLineEdit()
        self.mesajL=QLabel("Mesajınız:")
        self.mesaj=QTextEdit("")
        self.bilgiL=QLabel("Gönderi Durumunuz: ")
        self.gonder=QPushButton("Gönder")

        picture_box=QHBoxLayout()
        picture_box.addStretch()
        picture_box.addWidget(self.resim)
        picture_box.addStretch()

        secenekler_box=QHBoxLayout()
        secenekler_box.addStretch()
        secenekler_box.addWidget(self.gonder)

        v_box=QVBoxLayout()
        v_box.addLayout(picture_box)
        v_box.addWidget(self.gondericiL)
        v_box.addWidget(self.gonderici)
        v_box.addWidget(self.aliciL)
        v_box.addWidget(self.alici)
        v_box.addWidget(self.baslikL)
        v_box.addWidget(self.baslik)
        v_box.addWidget(self.mesajL)
        v_box.addWidget(self.mesaj)
        v_box.addWidget(self.bilgiL)
        v_box.addLayout(secenekler_box)
        self.setLayout(v_box)
        self.setWindowTitle("Mail Gönder -- ©SilverMail")
        self.setGeometry(500,100,500,500)
        self.show()
        self.gonder.clicked.connect(self.mail_gonder)

    def mail_gonder(self):
        mesaj=MIMEMultipart()
        mesaj["From"]=self.gonderici.text()
        mesaj["To"]=self.alici.text()
        mesaj["Subject"]=self.baslik.text()
        yazi=self.mesaj.toPlainText()
        mesaj_govdesi=MIMEText(yazi,"plain")
        mesaj.attach(mesaj_govdesi)
        #Gmail Bağlantısı
        try:
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("mailAdresiniz@gmail.com","sifre")
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            self.bilgiL.setText("Gönderi Durumunuz: Mail Başarıyla gönderidli.")
            mail.close()
        except:
            self.bilgiL.setText("Mail Gönderiminde hata oluştu. Tekrar Deneyiniz.")
app=QApplication(sys.argv)
uygulama=Uygulama()
sys.exit(app.exec_())






