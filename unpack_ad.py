def hide_id(id):
    return id[:4]+"-00"+id[4:6]+"/"+id[6:]

def unpack_ad(data):
    pref = []
    if data[5]:
        pref.append("допускает дейты")
    if data[6]:
        pref.append("нетворкинг")
    if data[7]:
        pref.append("дружба")
        
    return (data[10]+"\n\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"+("Парень, " if data[1] == 1 else "Леди, ")+"MouraID: "+hide_id(str(data[0]))+"\n"+data[2] +
            ", "+data[3] + ", " +data[4][0]+" курс\n\nПредпочтения: "+', '.join(pref))
