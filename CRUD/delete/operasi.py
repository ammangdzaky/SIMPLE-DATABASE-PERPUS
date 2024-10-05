from ..read import database
import os

def read(**kwargs):
    try:
        with open(database.DB_NAME, "r") as f:
            content = f.readlines()
            panjang_data = len(content)
            if "index" in kwargs:
                indeks = kwargs["index"] - 1
                if indeks < 0 or indeks > panjang_data:
                    return False
                else:
                    return content[indeks]
            else:
                return content
    except:
        print("EROR")
        return False
    
    
def delete(no_buku):
    try:
        with open(database.DB_NAME, "r") as f:
            count = 0
            
            while True:
                content = f.readline()
                if len(content) == 0:
                    break
                elif count == no_buku - 1:
                    pass
                else:
                    with open("sementara.txt", "a", encoding="utf-8") as f_sementara:
                        f_sementara.write(content)
                count += 1
        print("\nBUKU BERHASIL DIHAPUS")
    except:
        print("GAGAL AWOAKWOAK")

    os.replace("sementara.txt",database.DB_NAME)

