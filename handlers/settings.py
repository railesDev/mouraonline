from bot import moura
from bot import dp, router, F, types, FSMContext
from bot import asyncio
import keyboards
from states import User
from bot import c, conn
import consts
import logging
import dboper
from handlers.parse_ad import parse_ad

@router.message(
    F.text == consts.setup | F.text == consts.pause_likes
)
async def setup(message: types.Message, state: FSMContext):
    # show ad, display buttons
    user_data = dboper.extract_ad(conn, c, message.from_user.id)
    logging.info("USER SETUP DATA: " + str(user_data) + "\n\n\n")
    keys = ['id', 'gender', 'campus', 'program', 'course', 'frd_goal', 'dts_goal', 'ntw_goal', 'gender_goals', 'photo_id', 'ad_text']
    data = dict(zip(keys, user_data))
    parsed, photo_id = parse_ad(data)
    await message.answer_photo(photo_id,
                               consts.setup_caption+'\n'+parsed,
                               reply_markup=keyboards.settings_keyboard)
