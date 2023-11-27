from bot import moura, router, dp, F, types, FSMContext, ReplyKeyboardRemove, ParseMode
from bot import c, conn
from states import User
import dboper
import consts
import keyboards
import logging
from unpack_ad import unpack_ad
import asyncio
import random


@dp.message(F.text == "Look at my likes!💟")
async def look_at_like(message: types.Message, state: FSMContext):
    res = dboper.find_like(conn, c, message.from_user.id)
    if res is not None:  # we have likes left
        match_id = res[0]
        await state.update_data(awaiting=match_id)
        match_data = dboper.get_match_data(conn, c, match_id)
        await message.answer_photo(str(match_data[9]), unpack_ad(match_data), reply_markup=keyboards.likes_keyboard)
    else:  # no likes left
        await state.set_state(User.awaiting)
        await message.answer(consts.no_likes_caption,
                             reply_markup=keyboards.awaiting_keyboard)

        # SPECIAL LINES TO CHECK INACTIVITY EACH 10 MINUTES
        while True:
            await asyncio.sleep(600)
            try:
                data = await state.get_data()
                if data['awaiting']:
                    pass
            except KeyError:
                await message.answer(random.choice(consts.inactivity_caption))



@dp.message(F.text == "Match 💟")
async def match(message: types.Message, state: FSMContext):
    data = await state.get_data()
    dboper.update_reaction(conn, c, data["awaiting"], 2)
    # later here will be some actions - choose context, choose place.
    logging.info("MATCHID: "+str(int(data['awaiting'])))
    await message.answer(f"Write to [your new match\!](tg://user?id={int(data['awaiting'])})",
                         parse_mode=ParseMode.MARKDOWN_V2)
    # TODO: message.from_user.username -> TO DATABASE -> TO MATCH
    # TODO X2: send a message to match, no usernames will be saved or given.
    #  There you will be able to showcase your own username -> prebuilt scripts (share your username, set location, etc)
    await look_at_like(message, state)  # view next like
    # to the one with whom we matched, will happen nothing. everything is on our initiative.


@dp.message(F.text == "No 🚫")
async def no_match(message: types.Message, state: FSMContext):
    data = await state.get_data()
    dboper.update_reaction(conn, c, data["awaiting"], 0)
    await message.answer(consts.dislike_caption)
    await look_at_like(message, state)  # view next like


@dp.message(F.text == 'Complain ‼️')
async def match_complain(message: types.Message, state: FSMContext):
    data = await state.get_data()
    dboper.update_reaction(conn, c, data["awaiting"], 0)
    await message.answer(consts.complain_caption)
    await look_at_like(message, state)  # view next like

