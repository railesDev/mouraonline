import logging


def parse_ad(data):
    sdata = ""
    photoid = ""
    logging.info("DATA to parse ad: "+str(data))
    for key, value in data.items():
        if key not in ["id", "ad_text", "goals", "photo_id", "gender_goals"]:
            sdata += "<b>"+key[0].upper()+key[1:]+":</b> "+(value if key != "gender" else "male" if value == 1 else "female")+"\n"
        else:
            if key == "ad_text":
                sdata = "<b>Description:</b>\n"+value+"\n\n\n" + sdata
            if key == "goals":
                sdata += "<b>"+key[0].upper()+key[1:]+":</b> "+', '.join(value)+"\n"
            if key == "gender_goals":
                sdata += "<b>Preferences:</b> " + ('Ladies ‍👩' if value == 0
                                                                    else ('Both 🤷' if value == 2
                                                                          else ('Guys 👨' if value == 1
                                                                                else None))) + "\n"
            if key == "photo_id":
                photoid = value
    return sdata, photoid