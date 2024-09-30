import os

if __name__ == "__main__":
    
    while True:
        
        system_operation = os.name

        match system_operation:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
            
        #header
        print("SELAMAT DATANG CUI".center(30))
        print("DATABASE PERPUSTKAAN SEDERHANA")
        print("==============================")
        
        #opsi
        print("\nOPSI YANG TERSEDIA: \n")
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        
        opsi_user = input("\nSilahkan pilih opsi : ")
        
        #condition
        print("\n==============================\n")
        
        match opsi_user:
            case "1" : print("read")
            case "2" : print("create")
            case "3" : print("update")
            case "4" : print("delete")
            case _ : print("Masukkan input yang valid!! (1/2/3/4)")
        
        print("\n==============================\n")
        
        #break
        is_break = input("Apakah anda ingin berhenti (y/n) : ")
        if is_break == "y" or is_break == "Y":
            break
    
    print("\nOKEE, TERIMA KASIH ORANG BAIK\n")