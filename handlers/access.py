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


def generate_secret_code(length=6):
    return (''.join(random.choice('0123456789ABCDEF') for _ in range(length)))+'MU27'


def download_image(url):
    # Set a user-agent header to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    request = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            image_data = response.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            return image_base64
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None


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

    text = f"Привет! Введи этот код в ответ боту: {secret_code}"
    
    html = f"""\
    <html>
      <head></head>
      <body>
        <p>Привет! Введи этот код в ответ боту:<br>
        <h1 style="color:blue;">{secret_code}</h1></p>
        <img src="cid:image1" alt="Image">
      </body>
    </html>
    """

    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    image_base64 = download_image(consts.letter_image)
    image = MIMEImage(base64.b64decode(image_base64), name="image1")
    image.add_header('Content-ID', '<image1>')
    image.add_header('Content-Disposition', 'inline', filename="image1")
    msg.attach(image)

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(username, app_password)
        server.sendmail(username, message.text, msg.as_string())

    message.answer_photo(consts.code_sent_photo,
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

