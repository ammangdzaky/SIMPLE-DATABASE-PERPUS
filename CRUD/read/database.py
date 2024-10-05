from . import operasi

DB_NAME = "database.txt"

TEMPLATE = {
    "pk" : "xxxxxx",
    "date_add" : "yyyy-mm-dd",
    "penulis" : " "*255,
    "judul" : " "*255,
    "tahun" : "xxxxx"
}

def init_console():
    try:
        with open(DB_NAME,"r") as f:
            print("berhasil")
    except:
        print("file database tidak ditemukan, akan membuat file baru")
        operasi.create_db()

