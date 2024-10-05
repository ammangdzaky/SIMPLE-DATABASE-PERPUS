from . import operasi

def read_console():
    
    database = operasi.read()
    
    index = "NO"
    judul = "JUDUL"
    penulis = "PENULIS"
    tahunn = "TAHUN TERBIT"
    
    #tabel header
    
    print("="*110)
    print(f"| {index.center(5)} | {judul.center(40)} | {penulis.center(40)} | {tahunn.center(11)} |")
    print("="*110)

    for index,data in enumerate(database):
        # data_break = data.split(",")
        data_break = [item.strip() for item in data.split(",")]

        pk = data_break[0]
        date_add = data_break[1]
        # judul = data_break[2]
        # penulis = data_break[3]
        # tahun = data_break[4]
        judul = data_break[2][:40]  
        penulis = data_break[3][:40]  
        tahun = data_break[4][:11]
        print(f"| {str(index + 1).center(5)} | {(judul.center(40)).title()} | {(penulis.center(40)).title()} | {tahun.center(12)} |")

    #footer table
    print("="*110)
    


