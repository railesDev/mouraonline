def unpack_ad(data):
    return (data[10]+"\n\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"+("Парень, " if data[1] == 1 else "Леди, ")+"MouraID: "+str(data[0])+"\n"+data[2] +
            ", "+data[3] + ", " +data[4][0]+" курс\n\nПредпочтения: "+", ".join(["допускает дейты"*bool(data[5]),
            "нетворкинг"*bool(data[6]),("дружба"*data[7])]))
