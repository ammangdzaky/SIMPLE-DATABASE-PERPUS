from . import operasi
from ..read import view


def create_console():
    
    print("="*110,"\n")
    
    print("MEMBUAT DATA BUKU BARU!!\n")

    judul = input("MASUKKAN JUDUL\t\t: ")
    penulis = input("MASUKKAN PENULIS\t: ")
    while True:
        try:
            tahun = int(input("MASUKKAN TAHUN TERBIT\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("YAKIN SEKARANG TAHUNNYA BUKAN DIGIT 4?")
        except:
            print("TAHUN HARUS ANGKA")
            
    operasi.create(judul,penulis,tahun)
    
    print("\nDATA BUKU BERHASIL DITAMBAHKAN, BERIKUT DATA BUKU TERBARU\n")
    
    view.read_console()
    
