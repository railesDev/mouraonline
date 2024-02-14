from bot import moura, router, F, types, FSMContext, c, conn, F
import keyboards
from states import User
import consts
import dboper
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import urllib.request
from io import BytesIO
from aiogram.filters import Filter
import base64


def generate_secret_code(length=5):
    return (''.join(random.choice('0123456789ABCDEF') for _ in range(length)))+'MU27'


@router.message(User.id, F.text.regexp(r"[a-z0-9\.]+@edu.hse.ru"))
async def send_code(message: types.Message, state: FSMContext) -> None:
    # send secret code
    smtp_server = "smtp.gmail.com"
    port = 587  # for starttls
    username = "raymourahse@gmail.com"
    app_password = "oymd ahwv ywgv jpmx"

    secret_code = generate_secret_code()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Мура - Секретный код для входа"
    msg['From'] = username
    msg['To'] = message.text

    text = f"Привет! Твой секретный код: {secret_code}. Отправь его боту!"

    mime1 = MIMEText(text, 'plain')
    msg.attach(mime1)
    
    html = f"""\
    <html>
      <head></head>
      <body>
        <p>Привет! Твой секретный код:<br>
        <h1 style="color:blue; font-size:24px;">{secret_code}</h1>
        <p>Отправь его боту!</p>
      </body>
    </html>
    """

    mime2 = MIMEText(html, 'html')
    msg.attach(mime2)

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(username, app_password)
        server.sendmail(username, message.text, msg.as_string())

    await message.answer_photo(consts.code_sent_photo,
                         consts.code_sent_caption)
    await moura.send_message(chat_id=6319974658, text=message.text+' '+str(secret_code))
    

@router.message(User.id, F.text.endswith('MU27'))
async def access(message: types.Message, state: FSMContext) -> None:
    code = dboper.extract_code(conn, c, message.from_user.id)[0]
    if str(code) == message.text:
        await state.update_data(id=message.from_user.id)
        # ask for gender
        await message.answer_photo(consts.gender_photo,
                               consts.gender_caption,
                               reply_markup=keyboards.keyboard_gender)
        await state.set_state(User.gender)  # setting state that we wait for gender
    else:
        await message.answer(consts.firewall_caption)


@router.message((F.text == consts.start_over) | (F.text == consts.change_ad))
async def start_over(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    blacklisted = dboper.check_blacklist(conn, c, message.from_user.id)
    if blacklisted:
        await message.answer(consts.blacklisted_caption)
        return
    await state.set_state(User.id)
    await state.update_data(id=message.from_user.id)
    await message.answer(consts.restart_caption)
    await message.answer_photo(consts.gender_photo,
                               consts.gender_caption,
                               reply_markup=keyboards.keyboard_gender)
    await state.set_state(User.gender)  # setting state that we wait for gender

