def unpack_ad(data):
    return (data[8]+"\n\n"+("Guy, " if data[1] == 1 else "Lady, ")+"MouraID: "+str(data[0])+"\nStudies at "+data[2] +
            " on "+data[3] + ", course - "+data[4][0]+"\nSearches for: "+("dates, " if data[5][1] else "") +
            ("networking, " if data[5][2] else "")+("friendship" if data[5][0] else ""))