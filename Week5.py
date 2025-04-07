from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox,
    QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QFormLayout
)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
import re
import sys

class ValidasiForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validasi Form - Abdul Aqil Murtadho, F1D022029")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.colmNama = QLineEdit()
        form_layout.addRow("Nama:", self.colmNama)

        self.colmInput = QLineEdit()
        form_layout.addRow("Email:", self.colmInput)

        self.colmUsia = QLineEdit()
        form_layout.addRow("Usia:", self.colmUsia)

        self.colmNoHP = QLineEdit()
        self.colmNoHP.setInputMask("+62 000 0000 0000")
        form_layout.addRow("No. HP:", self.colmNoHP)

        self.colmAlamat = QTextEdit()
        form_layout.addRow("Alamat:", self.colmAlamat)

        self.colmGender = QComboBox()
        self.colmGender.addItems(["Pilih Gender", "Laki-laki", "Perempuan"])
        form_layout.addRow("Jenis Kelamin:", self.colmGender)

        self.colmPendidikan = QComboBox()
        self.colmPendidikan.addItems(["Pilih Pendidikan", "SMA", "Diploma", "Sarjana", "Magister"])
        form_layout.addRow("Pendidikan:", self.colmPendidikan)

        layout.addLayout(form_layout)

        layoutTombol = QHBoxLayout()
        self.tombolSimpan = QPushButton("Simpan")
        self.tombolSimpan.clicked.connect(self.validasi_form)
        self.tombolClear = QPushButton("Bersihkan")
        self.tombolClear.clicked.connect(self.clearForm)
        layoutTombol.addWidget(self.tombolSimpan)
        layoutTombol.addWidget(self.tombolClear)

        layout.addLayout(layoutTombol)

        cttKaki = QLabel("© Abdul Aqil Murtadho (F1D02202)")
        cttKaki.setAlignment(Qt.AlignCenter)
        layout.addWidget(cttKaki)

        self.setLayout(layout)

    def validasi_form(self):
        nama = self.colmNama.text().strip()
        email = self.colmInput.text().strip()
        usia = self.colmUsia.text().strip()
        nomor_hp = self.colmNoHP.text().strip()
        alamat = self.colmAlamat.toPlainText().strip()
        gender = self.colmGender.currentText()
        pendidikan = self.colmPendidikan.currentText()

        if not nama.isalpha():
            self.printPesan("Nama hanya boleh berisi huruf.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.printPesan("Masukkan alamat email yang valid.")
            return

        if not usia.isdigit():
            self.printPesan("Usia harus berupa angka.")
            return

        digit_nomor = re.sub(r"\D", "", nomor_hp)
        if len(digit_nomor) != 13:
            self.printPesan("Nomor HP harus terdiri dari 13 digit.")
            return

        if not alamat:
            self.printPesan("Alamat tidak boleh kosong.")
            return

        if gender == "Pilih Gender":
            self.printPesan("Silakan pilih jenis kelamin.")
            return

        if pendidikan == "Pilih Pendidikan":
            self.printPesan("Silakan pilih tingkat pendidikan.")
            return


        if int(usia) < 17:
            self.printPesan("Usia minimal 17 tahun.")
            return

        self.printPesan("Data berhasil disimpan.", sukses=True)
        self.clearForm()

    def printPesan(self, pesan, sukses=False):
        msg_box = QMessageBox()
        msg_box.setText(pesan)
        msg_box.setIcon(QMessageBox.Information if sukses else QMessageBox.Warning)
        msg_box.exec_()

    def clearForm(self):
        self.colmNama.clear()
        self.colmInput.clear()
        self.colmUsia.clear()
        self.colmNoHP.clear()
        self.colmAlamat.clear()
        self.colmGender.setCurrentIndex(0)
        self.colmPendidikan.setCurrentIndex(0)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ValidasiForm()
    window.show()
    sys.exit(app.exec_())
