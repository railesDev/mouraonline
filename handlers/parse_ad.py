import logging
database = {"id": "ID", "gender": "<b>Пол:</b> ", "campus": "<b>Корпус:</b> ", "program": "<b>ОП:</b> ", "course": "<b>Курс:</b> ", "ad_text": "<b>Описание:</b>\n", "goals": "<b>Цели:</b> ", "photo_id": "photo_id", "gender_goals": "<b>Предпочтения:</b> "}

def parse_ad(data):
    sdata = ""
    photoid = ""
    logging.info("DATA to parse ad: "+str(data))
    for key, value in data.items():
        if key not in ["id", "ad_text", "goals", "photo_id", "gender_goals", "awaiting", "action", "matched"]:
            sdata += database[key]+(value if key != "gender" else "мужской" if value == 1 else "женский")+"\n"
        else:
            if key == "ad_text":
                sdata = "<b>Описание:</b>\n"+value+"\n\n\n" + sdata
            if key == "goals":
                sdata += "<b>"+database[key]+":</b> "+', '.join(value)+"\n"
            if key == "gender_goals":
                sdata += "<b>Предпочтения:</b> " + ('Девушки ‍👩' if value == 0
                                                                    else ('Без разницы 🤷' if value == 2
                                                                          else ('Парни 👨' if value == 1
                                                                                else None))) + "\n"
            if key == "photo_id":
                photoid = value
    return sdata, photoid
