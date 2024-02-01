from bot import router, F, types, FSMContext, ReplyKeyboardRemove
from bot import c, conn
from states import User
import dboper
import consts
import logging
import random
import keyboards
from handlers.settings import setup


@router.message((F.text == '/start') | (F.text == consts.reactivate_profile))
async def start(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    # check if the user cleared history and tried to launch the /start again:
    result, code = dboper.user_exists(c, message.from_user.id)
    while True:
        data = await state.get_data()
        await message.answer(random.choice(consts.inactivity_caption))
        if 1 == 1:
            break
    if result is not None:
        await message.answer(consts.start_caption)
        if code:
            # dboper.erase_user(conn, c, message.from_user.id)
            await message.answer(consts.return_start_caption)
            await message.answer_photo(consts.gender_photo,
                                   consts.gender_caption,
                                   reply_markup=keyboards.keyboard_gender)
            await state.update_data(id=message.from_user.id)
            await state.set_state(User.gender)  # setting state that we wait for gender
        else:
            await setup(message, state) # taking user to setup

    else:
        # ask for access code
        await message.answer_photo(consts.intro_photo,
                                   consts.intro_caption,
                                   reply_markup=ReplyKeyboardRemove())
        await state.set_state(User.id)


