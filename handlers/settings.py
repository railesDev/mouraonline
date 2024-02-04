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
    (F.text == consts.setup) | (F.text == consts.pause_likes) | (F.text == consts.deactivate_no)
)
async def setup(message: types.Message, state: FSMContext):
    blacklisted = dboper.check_blacklist(conn, c, message.from_user.id)
    if blacklisted:
        await message.answer(consts.blacklisted_caption)
        await state.clear()
        return
    # show ad, display buttons
    await state.set_state(User.awaiting)
    user_data = dboper.extract_ad(conn, c, message.from_user.id)
    logging.info("USER SETUP DATA: " + str(user_data) + "\n\n\n")
    keys = ['id', 'gender', 'campus', 'program', 'course', 'frd_goal', 'dts_goal', 'ntw_goal', 'gender_goals', 'photo_id', 'ad_text']
    data = dict(zip(keys, user_data))
    parsed, photo_id = parse_ad(data)
    await message.answer_photo(photo_id,
                               consts.setup_caption+'\n'+parsed,
                               reply_markup=keyboards.settings_keyboard)
