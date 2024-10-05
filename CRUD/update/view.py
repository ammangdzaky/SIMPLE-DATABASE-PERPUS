from ..read import view
from . import operasi

def update_console():
    
    view.read_console()
    
    while True:
        print("\n","="*110)
        no_buku = int(input("\nMASUKKAN NO. BUKU YANG INGIN DIUPDATE : "))
        data_buku = operasi.read(index=no_buku)
        if data_buku:
            break
        else:
            print("NOMOR BUKU TIDAK VALID!!! COBA LAGI")
    
    data_break = data_buku.split(",")
    
    # Cek jumlah elemen dalam data_break
    if len(data_break) < 5:
        print("Data buku tidak lengkap, tidak dapat melakukan update.")
        return  # Keluar dari fungsi jika data tidak lengkap

    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4]
    
    while True:
        
        print(f"\nDATA BUKU KE-{no_buku} :")
        print(f"1. JUDUL\t= {judul:.40}")
        print(f"2. PENULIS\t= {penulis:.40}")
        print(f"3. TAHUN TERBIT\t= {tahun:4}")
        
        #option
        opsi = input("\nSILAHKAN PILIH BAGIAN YANG INGIN ANDA UBAH [1/2/3] : ")

        match opsi:
            case "1" : judul = input("\nMASUKKAN PERUBAHAN JUDUL\t: ")
            case "2" : penulis = input("\nMASUKKAN PERUBAHAN PENULIS\t: ")
            case "3" : 
                while True:
                    try:
                        tahun = int(input("\nMASUKKAN PERUBAHAN TAHUN TERBIT\t: "))
                        if len(str(tahun)) != 4:
                            print(f"\YAKIN TAHUNNYA TIDAK EMPAT DIGIT??")
                        else:
                            break
                    except:
                        print(f"MASUKKAN TAHUN DALAM INTEGER!!")
        
        print(f"\nDATA BUKU KE-{no_buku} TERBARU")
        print(f"1. JUDUL\t= {judul:.40}")
        print(f"2. PENULIS\t= {penulis:.40}")
        print(f"3. TAHUN TERBIT\t= {tahun:4}\n")
                        
        is_done = input("APAKAH ANDA INGIN BERHENTI MENGUPDATE DATA BUKU? (y/n) : ")
        if is_done == "y" or is_done == "Y":
            break
    
    operasi.update(no_buku,pk,date_add,judul,penulis,tahun)

        
    
    
    
    
    
    