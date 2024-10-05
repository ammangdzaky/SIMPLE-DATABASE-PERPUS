from ..read import database
import string
import random
import time

def create(judul,penulis,tahun):
    
    data = database.TEMPLATE.copy()

    data["pk"] = "".join(random.choice(string.ascii_letters) for i in range(6))
    data["date_add"] = time.strftime("%Y:%m:%d-%H:%M:%S:%Z", time.gmtime())
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun
    
    all_data = f"\n{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}"
    
    try:
        with open(database.DB_NAME, mode="a", encoding="utf-8") as f:
            f.write(all_data)
            print("\nBerhasil")
    except:
        print("GAGAL BJIR")






