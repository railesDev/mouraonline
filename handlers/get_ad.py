from bot import moura
from bot import dp, router, F, types, FSMContext
from bot import asyncio
import keyboards
from states import User
from bot import c, conn
import consts
import logging
import dboper
import random
from unpack_ad import unpack_ad


@router.message(
    User.awaiting,
    (F.text == consts.show_ad) | (F.text == consts.backto_ads)
)
async def get_new_ad(message: types.Message, state: FSMContext):
    await state.update_data(awaiting=0) # user decided to wait for a new ad
    logging.info("WARNING: WARNING: WARNING: Started searching for matches\n\n\n")
    # extract our current user info
    user_data = dboper.extract_user(conn, c, message.from_user.id)
    logging.info("USER DATA: " + str(user_data) + "\n\n\n")
    while True:
        data = await state.get_data()
        if not data or data["awaiting"] == -1:
            break
        # try to find a match for him if any left
        match_id = dboper.find_match(conn, c, user_data)
        logging.info("tried to find a recommendation.")
        if match_id is not None:
            match_data = dboper.get_match_data(conn, c, match_id[0])
            await message.answer_photo(str(match_data[9]), unpack_ad(match_data),
                                       reply_markup=keyboards.tinder_keyboard)
            await state.set_state(User.action)
            await state.update_data(awaiting=match_id[0])
            logging.info("found a recommendation.")
            break
        else:
            data = await state.get_data()
            try:
                if data["awaiting"] == 0:
                    await message.answer(consts.no_ads_caption,
                                         reply_markup=keyboards.awaiting_keyboard)
                    await state.update_data(awaiting=-1)
            except KeyError:
                await message.answer(consts.no_ads_caption,
                                     reply_markup=keyboards.awaiting_keyboard)
                await state.update_data(awaiting=-1)
        await asyncio.sleep(200)  # wait for 200 seconds before checking again
