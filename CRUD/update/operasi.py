from ..read import database

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
    

def update(no_buku,pk,date_add,judul,penulis,tahun):
    
    data = database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add + database.TEMPLATE["date_add"][len(date_add):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis+ database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    all = f"\n{data["pk"]},{data["date_add"]},{data['judul']},{data['penulis']},{data['tahun']}"
    panjang_all = len(all)

    try:
        with open(database.DB_NAME, "r+", encoding="utf-8") as f:
            f.seek(panjang_all*(no_buku - 1))
            f.write(all)
    except:
        print("GAGAL LU BJIR")