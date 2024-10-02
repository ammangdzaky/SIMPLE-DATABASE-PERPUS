import random
import string
import time
from . import database

def create_db():
    
    judul = input("Masukkan Judul : ")
    penulis = input("Masukkan Penulis : ")
    tahun = input("Masukkan Tahun Terbit : ")
    
    data = database.TEMPLATE.copy()
    
    data["pk"] = "".join(random.choice(string.ascii_letters) for i in range(6))
    data["date_add"] = time.strftime("%Y:%m:%d-%H:%M:%S:%Z",time.gmtime())
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun 
    
    all_data = f"{data["pk"]} , {data["date_add"]} , {data["judul"]} , {data["penulis"]} , {data["tahun"]}"
    print(all_data)
    
    try:
        with open(database.DB_NAME,"w", encoding="utf-8") as f:
            f.write(all_data)
    except:
        print("GAGAL BJIR")
        
def read():
    try:
        with open(database.DB_NAME, "r") as f:
            content = f.readlines()
            return content
    except:
        print("Lu gagal WAKWKAK")
        return False

