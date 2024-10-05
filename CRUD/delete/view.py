from ..read import view
from . import operasi

def delete_console():
    
    view.read_console()
    
    while True:
        
        print("\n","="*110)
        no_buku = int(input("\nMASUKKAN NO. BUKU YANG INGIN DIDELETE : "))
        data_buku = operasi.read(index=no_buku)
        
        if data_buku:
            
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4]
            
            print(f"\nDATA BUKU KE-{no_buku} :")
            print(f"1. JUDUL\t= {judul:.40}")
            print(f"2. PENULIS\t= {penulis:.40}")
            print(f"3. TAHUN TERBIT\t= {tahun:4}")
            
            while True:
                try:
                    is_done = input("\nAPAKAH ANDA YAKIN INGIN MENGHAPUS BUKU INI? (y/n) : ")
                    if is_done == "y".lower():
                        break
                    elif is_done == "n".lower():
                        return
                    else:
                        print("MASUKKAN INPUT YANG VALID!!")
                        continue
                except :
                    print("MASUKKAN INPUT YANG VALID (y/n)!!")
                    
                        
                
            
            break
        else:
            print("NOMOR BUKU TIDAK VALID!!! COBA LAGI")
            
    operasi.delete(no_buku)