import CRUD as crud
import os

if __name__ == "__main__":
    
    system_operation = os.name
    match system_operation:
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")
        
    print("SELAMAT DATANG CUI".center(110))
    print("DATABASE PERPUSTKAAN SEDERHANA".center(110))
    print("="*110)
    
    # membuat database.txt jika belum add
    crud.init_console()

    while True:
        
        system_operation = os.name

        match system_operation:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
            
        #header
        print("SELAMAT DATANG CUI".center(110))
        print("DATABASE PERPUSTAKAAN SEDERHANA".center(110))
        print("="*110)
        # print("SELAMAT DATANG CUI".center(30))
        # print("DATABASE PERPUSTKAAN SEDERHANA")
        # print("==============================")
        
        #opsi
        print("\nOPSI YANG TERSEDIA: \n")
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        
        opsi_user = input("\nSilahkan pilih opsi : ")
        print('\n')
        
        #condition
        # print("\n==============================\n")
        
        match opsi_user:
            case "1" : crud.read_console()
            case "2" : crud.create_console()
            case "3" : crud.update_console()
            case "4" : crud.delete_console()
            case _ : print("Masukkan input yang valid!! (1/2/3/4)")
        
        # print("\n==============================\n")
        
        #break
        is_break = input("\nAPAKAH ANDA INGIN KELUAR DARI PROGRAM DATABASE PERPUSTAKAAN? (y/n) : ")
        if is_break == "y" or is_break == "Y":
            break
    
    print("\nOKEE, SEMOGA HARIMU SELALU BERJALAN MULUS ORANG BAIK\n")