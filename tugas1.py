class Orang:
    def __init__(self, namadepan, namabelakang, nomer_id):
        self.namadepan = namadepan
        self.namabelakang = namabelakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print(f"Nama: {self.namadepan} {self.namabelakang}")
        print(f"Nomer ID: {self.nomer_id}")


class Mahasiswa(Orang):
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"

    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, matakuliah):
        self.matkul.append(matakuliah)

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenjang: {self.jenjang}")
        print(f"Mata Kuliah: {', '.join(self.matkul) if self.matkul else 'Belum mengambil mata kuliah'}")


class Karyawan(Orang):
    TETAP = "Tetap"
    TDK_TETAP = "Tidak Tetap"

    def __init__(self, status_karyawan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_karyawan = status_karyawan

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Status Karyawan: {self.status_karyawan}")


class Dosen(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Mata Kuliah yang Diajarkan: {', '.join(self.matkul_diajar) if self.matkul_diajar else 'Belum mengajar mata kuliah'}")


class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, matakuliah):
        self.matkul.append(matakuliah)


class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)


class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, *args, **kwargs):
        Orang.__init__(self,*args, **kwargs)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

    def tampilkan_info(self):
        super().tampilkan_info()  
        print(f"Mata Kuliah yang Diambil: {', '.join(self.matkul) if self.matkul else 'Belum mengambil mata kuliah'}")
        print(f"Mata Kuliah yang Diajarkan: {', '.join(self.matkul_diajar) if self.matkul_diajar else 'Belum mengajar mata kuliah'}")


if __name__ == "__main__":
    bowo = Mahasiswa(Mahasiswa.SARJANA, "Bowo", "Nugroho", "987654")
    bowo.enrol("Basis Data")
    bowo.tampilkan_info()

    print()


    rizki = Dosen(Karyawan.TETAP,"Rizki", "Setiabudi", "456789")
    rizki.mengajar("Statistik")
    rizki.tampilkan_info()

    print()

    uswatun = Asdos("Uswatun", "Hasanah", "456456")
    uswatun.enrol("Big Data")
    uswatun.mengajar("Kecerdasan Artifisial")
    uswatun.tampilkan_info()
