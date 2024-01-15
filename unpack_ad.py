def hide_id(id):
    return id[:4]+"-00"+id[4:6]+"/"+id[6:]

def unpack_ad(data):
    return (data[10]+"\n\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"+("Парень, " if data[1] == 1 else "Леди, ")+"MouraID: "+hide_id(str(data[0]))+"\n"+data[2] +
            ", "+data[3] + ", " +data[4][0]+" курс\n\nПредпочтения: "+", ".join(["допускает дейты"*bool(data[5]),
            "нетворкинг"*bool(data[6]),("дружба"*data[7])]))
